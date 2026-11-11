---
name: negative-keyword-miner
description: Extract negative keywords from search term reports to eliminate wasted ad spend through intelligent pattern recognition and cost analysis
---

# Negative Keyword Miner

Extract high-impact negative keywords from search term reports to eliminate wasted ad spend.

## Core Workflow

When user provides search term report data:

1. **Load Analysis Framework** - Call `view` on `/mnt/skills/user/negative-keyword-miner/references/analysis-framework.md`

2. **Analyze Search Terms** - Identify patterns in:
   - Low-converting search queries
   - High-cost, zero-conversion terms
   - Irrelevant traffic patterns
   - Brand vs non-brand performance
   - Match type inefficiencies

3. **Generate Negative Keyword List** - Provide:
   - Exact match negatives (specific bad queries)
   - Phrase match negatives (pattern blockers)
   - Broad match negatives (category exclusions)
   - Priority tiers (critical vs nice-to-have)
   - Estimated monthly savings per keyword

4. **Create Implementation Guide** - Include:
   - Upload instructions by platform
   - Campaign-level vs account-level recommendations
   - Match type justifications
   - Expected impact analysis

## Input Formats Accepted

- CSV export from Google Ads, Microsoft Ads, or other PPC platforms
- Columns needed: Search Term, Impressions, Clicks, Cost, Conversions, Conv. Rate, CPA
- Minimum 30 days of data recommended for pattern recognition

## Output Format

Use the template from `/mnt/skills/user/negative-keyword-miner/references/output-template.md`

## Analysis Workflows

### Quick Scan (5-10 minutes)
For immediate wins - identify obvious negative keywords with zero conversions and significant spend.

### Deep Analysis (20-30 minutes)  
For comprehensive optimization - pattern analysis, match type recommendations, and strategic exclusions.

### Competitive Comparison (30-40 minutes)
Compare your negative keyword strategy against industry benchmarks and identify gaps.

## Key Features

✅ **Pattern Recognition** - Identifies recurring themes in wasted spend
✅ **Cost Prioritization** - Ranks negatives by potential savings
✅ **Match Type Intelligence** - Recommends optimal match type for each negative
✅ **Strategic Exclusions** - Balances blocking waste vs preserving reach
✅ **Impact Forecasting** - Estimates monthly savings from implementation

## Important Notes

- Always review before implementing - some "bad" terms may have strategic value
- Start with exact match negatives to avoid over-blocking
- Monitor performance 7 days post-implementation for unintended impacts
- Re-run analysis monthly as search behavior evolves

## Reference Materials

- Analysis Framework: `/mnt/skills/user/negative-keyword-miner/references/analysis-framework.md`
- Output Template: `/mnt/skills/user/negative-keyword-miner/references/output-template.md`
- Best Practices: `/mnt/skills/user/negative-keyword-miner/references/best-practices.md`
- Pattern Library: `/mnt/skills/user/negative-keyword-miner/references/pattern-library.md`
