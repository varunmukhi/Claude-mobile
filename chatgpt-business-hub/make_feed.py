#!/usr/bin/env python3
"""Turn a Shopify products export (Admin GraphQL JSON) into a ChatGPT Business Hub product feed CSV.

Spec: https://developers.openai.com/commerce/specs/file-upload/products (9 required fields).
Usage: python3 make_feed.py shopify_products.json vetropower-feed.csv
Skips products that are unpublished (no store URL) or priced 0.00, and lists them as problems.
"""
import csv, json, re, sys

SELLER = "Vetro Power India"
BRAND = "Vetro Power"
CURRENCY = "INR"
FIELDS = ["item_id", "item_group_id", "title", "description", "url", "brand",
          "seller_name", "image_url", "price", "availability"]

src, out = sys.argv[1], sys.argv[2]
nodes = json.load(open(src))["data"]["products"]["nodes"]
rows, problems = [], []

for p in nodes:
    url, img = p.get("onlineStoreUrl"), ((p.get("featuredMedia") or {}).get("preview") or {}).get("image", {}).get("url")
    if not url:
        problems.append(f"{p['handle']}: not on the online store, skipped")
        continue
    if not img:
        problems.append(f"{p['handle']}: no image, skipped")
        continue
    desc = re.sub(r"\s+", " ", p["description"]).strip()[:5000] or p["title"]
    variants = p["variants"]["nodes"]
    for v in variants:
        price = float(v["price"])
        if price <= 0:
            problems.append(f"{p['handle']} [{v['title']}]: price is 0.00, skipped")
            continue
        title = p["title"] if v["title"] == "Default Title" else f"{p['title']} - {v['title']}"
        vid = v["id"].rsplit("/", 1)[-1]
        rows.append({
            "item_id": v["sku"] or f"vp-{vid}",
            "item_group_id": p["handle"],
            "title": title[:150],
            "description": desc,
            "url": url if len(variants) == 1 else f"{url}?variant={vid}",
            "brand": BRAND,
            "seller_name": SELLER,
            "image_url": img,
            "price": f"{price:.2f} {CURRENCY}",
            "availability": "in_stock" if v["availableForSale"] else "out_of_stock",
        })

ids = [r["item_id"] for r in rows]
dupes = {i for i in ids if ids.count(i) > 1}
if dupes:
    problems.append(f"duplicate item_id (fixed by using variant id): {sorted(dupes)}")
    for r in rows:
        if r["item_id"] in dupes:
            r["item_id"] = "vp-" + r["url"].split("variant=")[-1] if "variant=" in r["url"] else r["item_id"] + "-" + r["item_group_id"]

with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(rows)

print(f"{len(rows)} items written to {out}")
print("\n".join(problems) if problems else "no problems found")
