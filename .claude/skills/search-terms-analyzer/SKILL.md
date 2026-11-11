---
name: search-terms-analyzer
description: Analyze search query data to identify high-intent winners, wasted spend, negative keyword opportunities, and new keyword discoveries. Use when analyzing Google Ads search terms reports, identifying wasteful queries, finding negative keywords, discovering keyword opportunities, refining match types, mapping search intent, or aligning search insights to bidding, ads, and landing pages.
---

# Search Terms Analyzer

Comprehensive search query analysis that transforms raw search term data into actionable insights: high-intent winners to scale, wastage to eliminate, negatives to add, and new keywords to capture.

## What This Skill Does

Analyzes search term reports across 6 dimensions:

1. **Winner Identification** - High-converting, scalable queries to prioritize
2. **Wastage Detection** - Zero-value queries draining budget
3. **Negative Keyword Mining** - Systematic negative list generation by theme
4. **Keyword Discovery** - New opportunities from query patterns
5. **Match Type Optimization** - Refinement recommendations for precision
6. **Intent Mapping** - Align queries to funnel stage and landing pages

**Output**: Prioritized action list with negative keywords, new keyword opportunities, match type changes, and bid/landing page alignment recommendations.

## Required Data

### Google Ads Search Terms Export (Preferred)

Export from Google Ads covering 30-90 days:
- Search term
- Match type
- Impressions, clicks, CTR
- Cost, conversions, conv. value
- Campaign/ad group (optional but valuable)

### Minimum Columns Required
```
search_term, impressions, clicks, cost, conversions
```

### Enhanced Analysis (Additional Columns)
```
conv_value, campaign, ad_group, match_type, quality_score
```

## How to Use

### Quick Analysis (Find Wastage Fast)
```
Analyze these search terms for wastage and negative keywords
[attach search terms export]
```

### Comprehensive Analysis
```
Full search terms analysis with keyword opportunities

Context:
- Business: [eCommerce/Lead Gen/SaaS]
- Target CPA: [$X] or Target ROAS: [X]
- Monthly spend: [$X]
- Primary goal: [conversions/revenue/leads]

[attach search terms data]
```

### Focused Analysis
```
Find negative keywords and match type issues in this data
[attach search terms]
Focus: Brand protection and competitor traffic
```

## Analysis Framework

### 1. Winner Identification

**High-Intent Winners** (Scale These):
- Conversions ≥3 with CVR ≥2x average
- ROAS/CPA significantly above target
- Consistent performance (not one-time spikes)
- Volume headroom available

**Actions for Winners:**
- Add as exact match keywords (if not already)
- Increase bids 15-25%
- Create dedicated ad copy
- Ensure best landing page alignment

### 2. Wastage Detection

**Zero-Value Queries** (Eliminate):
- 10+ clicks, 0 conversions
- Cost >2x target CPA with no conversions
- Clearly irrelevant intent

**Low-Value Queries** (Monitor/Exclude):
- CVR <50% of average, significant spend
- ROAS <50% of target
- Declining trend over 30+ days

**Wastage Categories:**
- Informational ("how to", "what is", "tutorial")
- Job seekers ("jobs", "careers", "salary", "hiring")
- Competitor brands (if not intentionally targeting)
- DIY/Free seekers ("free", "cheap", "DIY", "template")
- Wrong products/services
- Geographic mismatches

### 3. Negative Keyword Mining

**Negative Keyword Themes:**

| Theme | Example Negatives | Typical Savings |
|-------|-------------------|-----------------|
| Informational | how, what, why, when, guide, tutorial | 5-15% |
| Job Related | jobs, careers, salary, hiring, internship | 3-8% |
| Free/Cheap | free, cheap, discount, coupon (if premium) | 5-12% |
| Competitor | [competitor names] | 5-15% |
| DIY | DIY, homemade, make your own | 2-6% |
| Wrong Product | [unrelated product terms] | 3-10% |

**Negative Match Type Selection:**
- **Exact**: Only block specific query (conservative)
- **Phrase**: Block query + variations (moderate)
- **Broad**: Block any query containing term (aggressive)

**Rule**: Start with phrase match negatives; use exact for borderline cases, broad for clearly irrelevant themes.

### 4. Keyword Discovery

**Discovery Sources:**
- Converting queries not in keyword list
- Long-tail variations of winners
- New intent patterns emerging
- Seasonal/trending queries

**Evaluation Criteria:**
- Minimum 3 conversions (or 10 clicks for new terms)
- Relevance to products/services
- Search volume potential
- Competition level

**Priority Matrix:**
- **High Priority**: Converting, relevant, not currently targeted
- **Medium Priority**: High volume, relevant, untested
- **Low Priority**: Low volume variants of existing keywords

### 5. Match Type Optimization

**Match Type Issues:**

| Problem | Symptom | Solution |
|---------|---------|----------|
| Too Broad | Many irrelevant queries | Add negatives, tighten to phrase |
| Too Exact | Missing valuable variations | Test phrase match |
| Cannibalization | Same query, multiple keywords | Consolidate, set priorities |
| Overlap | Broad stealing exact's traffic | Negative in broad campaign |

**Match Type Progression:**
1. Start broad to discover queries
2. Add negatives to refine
3. Promote winners to exact match
4. Use phrase for middle ground

### 6. Intent Mapping

**Intent Categories:**

| Intent | Signals | Funnel Stage | Recommended Action |
|--------|---------|--------------|-------------------|
| Navigational | Brand + product | Bottom | Protect, high bids |
| Transactional | "buy", "order", "price" | Bottom | Scale, dedicated landing |
| Commercial | "best", "review", "vs" | Middle | Comparison content |
| Informational | "how", "what", "guide" | Top | Blog/content (or exclude) |

**Landing Page Alignment:**
- Transactional → Product/pricing pages
- Commercial → Comparison/review pages
- Brand → Homepage or brand landing page
- Category → Category/collection pages

## Output Format

### Executive Summary
- Total queries analyzed: X
- Wastage identified: $X/month (X% of spend)
- Winners to scale: X queries (potential +$X revenue)
- New keywords discovered: X opportunities
- Negative keywords recommended: X terms

### Wastage Report

**Immediate Exclusions (Add Now)**
| Query | Clicks | Cost | Reason | Negative Type |
|-------|--------|------|--------|---------------|
| [query] | X | $X | [reason] | Phrase |

**Monitor List (Review in 14 days)**
| Query | Clicks | Cost | CVR | Action |
|-------|--------|------|-----|--------|

### Negative Keyword Lists

**By Theme (Copy-Paste Ready)**

```
// Informational (Phrase Match)
"how to"
"what is"
"tutorial"
...

// Job Seekers (Phrase Match)
"jobs"
"careers"
"salary"
...

// Competitors (Exact Match)
[competitor 1]
[competitor 2]
...
```

### Winner Optimization

**Scale These Queries**
| Query | Conv | ROAS/CPA | Action | Expected Impact |
|-------|------|----------|--------|-----------------|
| [query] | X | Xx | Add exact, +20% bid | +$X revenue |

### New Keyword Opportunities

**Add to Campaigns**
| Keyword | Source Query | Match Type | Suggested Bid | Landing Page |
|---------|--------------|------------|---------------|--------------|
| [keyword] | [query] | Exact | $X | /page |

### Match Type Recommendations

| Keyword | Current | Recommended | Reason |
|---------|---------|-------------|--------|
| [keyword] | Broad | Phrase | Too much waste |

### Intent-Landing Page Alignment

| High-Volume Query | Current Page | Recommended Page | Expected Lift |
|-------------------|--------------|------------------|---------------|
| [query] | /generic | /specific | +X% CVR |

## Best Practices

**Before Analysis:**
- Export 30-90 days of data (more data = better patterns)
- Include conversion value if available (enables ROAS analysis)
- Note any known issues or recent changes
- Know your target CPA/ROAS thresholds

**During Analysis:**
- Provide business context (what you sell, who you target)
- Identify any terms that seem irrelevant but are actually valuable
- Flag any brand terms or competitors you intentionally target

**After Analysis:**
- Implement negative keywords within 24 hours
- Add winner keywords with appropriate bids
- Re-analyze monthly (query landscape shifts)
- Track wastage reduction over time

## Integration with Other Skills

This skill works well with:
- **performance-max-auditor** - PMax search term insights feed into this analysis
- **google-ads-copy-generator** - Create ads for discovered keywords
- **landing-page-optimizer** - Improve pages for high-intent queries
- **negative-keyword-miner** - Deep-dive negative extraction

## Advanced Features

### N-Gram Analysis
For large datasets (1000+ queries), request n-gram analysis to find:
- Common word patterns in wasteful queries
- Modifier combinations that convert well
- Theme clusters for ad group restructuring

### Competitor Analysis
If competitor terms are present:
- Conquest performance assessment
- Brand defense recommendations
- Competitor keyword opportunities

### Seasonal Pattern Detection
With 90+ days of data:
- Emerging query trends
- Seasonal term patterns
- Declining queries to pause

## For Detailed Methodologies

Reference files contain comprehensive frameworks:
- `references/wastage-patterns.md` - Common wastage patterns by industry
- `references/negative-templates.md` - Pre-built negative keyword lists
- `references/intent-framework.md` - Detailed intent classification system

## Tips for Maximum Value

1. **Include Cost Data** - Enables wastage quantification ($X savings)
2. **Provide CPA/ROAS Targets** - Calibrates "good" vs "bad" performance
3. **Share Business Context** - Prevents excluding actually-valuable terms
4. **Run Monthly** - Query landscapes change; catch drift early
5. **Implement Quickly** - Wastage compounds; every day costs money

## Limitations

- Cannot access Google Ads directly (you provide exports)
- Search volume estimates require external tools
- Competition data not available from search terms alone
- Requires minimum data volume (100+ queries recommended)

---

**Ready to analyze?** Share your search terms export and I'll identify wastage, winners, and opportunities with ready-to-implement negative keyword lists.
