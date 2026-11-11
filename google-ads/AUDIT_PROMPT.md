# Google Ads audit prompt

Paste this into Claude Code after running `setup.sh`. Customer IDs come from Windsor.ai's account list:
Zyax Chem `5113090982`, Flagstone Fix `9475023456`.

```text
Run google-ads-weekly-audit for customer ID 5113090982.

Use the configured Google Ads MCP server to retrieve account data.
Use the most recent 28 complete days in the account's reporting time zone.
State the exact start date, end date, currency and time zone before analysis.

My primary conversion is an online purchase on zyax.in (Shopify).
My target CPA or ROAS is YOUR_TARGET.
My landing page is https://zyax.in/collections/pool-care-products

Read and analyze only. Do not create assets, edit labels or apply account changes.

First retrieve total account spend for the selected dates.
Ask me to compare it with Google Ads before continuing.
Stop if the account or totals do not match.

Run the four base audit phases.
Mark missing or unsupported fields as unavailable.
Separate observed spend from estimated savings.
Return evidence and a proposed action for each issue.
Require human review before any negative keywords or budget changes.

If this account runs PMax, also run performance-max-auditor.
Merge its supported checks into the same report.
Skip unsupported PMax checks and explain which data is missing.
```

Reports are saved as `google-ads-weekly-audit-YYYY-MM-DD.md` and are git-ignored.
