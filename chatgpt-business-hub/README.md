# Claim Vetro Power in ChatGPT (Business Hub)

OpenAI launched Business Hub on 10 Nov 2026 (beta). It lets you claim your brand's profile inside ChatGPT, keep its details current, add products with prices, and see how often ChatGPT mentions you and sends clicks to your site. Claiming is free.

Sources: [OpenAI help article](https://help.openai.com/en/articles/20001635-setting-up-your-business-on-chatgpt), [product page](https://openai.com/business/businesses-in-chatgpt/).

## What works for an Indian store today

| Feature | Vetro Power (India) |
| --- | --- |
| Claim profile, edit details, blue check | Yes, if verification is supported in India |
| Insights (mentions, clicks, topics) | Yes, after Persona approval |
| Product feed | Try it. OpenAI says standard uploads target the US; other markets need OpenAI to confirm first |
| Business Agent (chatbot) | No. US businesses only for now |

Claiming does not push you up in ChatGPT's answers. It makes what ChatGPT shows about you accurate.

## Steps (about 15 minutes, plus review time)

1. **Sign in** to ChatGPT with the account that should own the brand (use a company account, not a personal one). Open <https://chatgpt.com/business-hub> or **Business Hub** in the sidebar.
2. **Search** "Vetro Power". If a listing shows, select it. If not, choose to add your business → **Through an online store** → enter `vetropower.in`.
3. **Verify** with **Shopify store** → Connect Shopify → log in to the vetropower.in store. This is the quickest. Backup: **Website domain** (add the TXT record it shows to vetropower.in DNS).
4. **Wait** for OpenAI's email approving the claim.
5. **Persona identity check**: Business overview → *Complete verification with Persona* → Verify. Keep ready:
   - Your government ID (PAN/Aadhaar/passport)
   - Zyax Chem Pvt Ltd registration (CIN / GST certificate). The name and address must match these records exactly.
   - Proof you can act for the company (director listing on MCA, or an authorisation letter)
   - Note: for a new profile, Persona approval publishes it right away, and a published profile can't be deleted. Fill in the profile details first if offered.
6. **Fill the profile** with the text in [profile.md](profile.md). Upload the logo and a cover photo.
7. **Product feed**: under Products, connect Shopify, or upload `vetropower-feed.csv` (87 items, INR prices). If India isn't accepted yet, keep the file for when it opens.
8. **Add teammates** (optional): Business Hub → team settings. Each person uses their own ChatGPT account.

## Check results

- Business Hub → **Insights** shows the last 28 days. Blank means not enough data yet, not zero.
- You can already track ChatGPT traffic: links from ChatGPT carry `utm_source=chatgpt.com`. Filter for it in Shopify analytics or Google Analytics.

## Refresh the feed

Export products from Shopify with the Admin GraphQL query below, save as `shopify_products.json`, then run:

```bash
python3 make_feed.py shopify_products.json vetropower-feed.csv
```

```graphql
{ products(first: 100, query: "status:active") { nodes { handle title description onlineStoreUrl
  featuredMedia { preview { image { url } } }
  variants(first: 20) { nodes { id sku title price availableForSale } } } } }
```

The script skips unpublished items and anything priced 0.00, and prints what it skipped.

## Store issues found while building the feed

Fix these in Shopify, then rebuild the feed:

- **6 products priced ₹0.00** (skipped): Plastic Protectant 5L, Glass Ceramic Coating 5L, Stainless Steel Coating 5L, Anti-Termite Wood Protector 5L, Moss Prevention Stone Sealer 5L, Textile Nano Coating Concentrate. Set a price, or set them to "price on request" off the store.
- **Fabric & Upholstery Protector Pro Plus 5L is ₹1,00,000**, while similar 5L products are ₹10,000. Check for an extra zero.
- **Wrong product type**: 8 non-shoe products (patio furniture, outdoor fabric, outerwear, baby fabric, bag, car fabric, marine fabric and clothing protectors) are typed "Footwear Protection". ChatGPT may use this for categorising.
- **Shoe Bag** is active but not published to the online store, so it's left out.
