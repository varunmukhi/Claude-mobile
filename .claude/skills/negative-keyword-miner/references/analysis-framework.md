# Negative Keyword Analysis Framework

## Core Analysis Methodology

### 1. Data Quality Check

Before analysis, validate:
- **Minimum data threshold**: 30+ days preferred, 14 days minimum
- **Statistical significance**: At least 100 clicks per search term for reliable patterns
- **Date range consistency**: No partial weeks/months (affects conversion attribution)
- **Data completeness**: All required columns present

### 2. Segmentation Strategy

Analyze search terms across multiple dimensions:

#### By Performance Metrics
- **Zero converters**: Terms with clicks but no conversions
- **High CPA outliers**: Cost per acquisition >2x account average
- **Low CTR terms**: Click-through rate <50% of category average
- **High impression, low click**: Relevance issues

#### By Intent Categories
- **Informational queries**: "how to", "what is", "guide", "tutorial"
- **Job-seeking queries**: "jobs", "career", "hiring", "resume"
- **Competitor research**: Competitor brand names, comparison terms
- **Freebie hunters**: "free", "cheap", "discount", "coupon"
- **Students/academics**: "project", "essay", "homework", "assignment"

#### By Match Type Efficiency
- **Broad match waste**: Identify where broad match triggers irrelevant searches
- **Phrase match leakage**: Close variants causing issues
- **Exact match problems**: Even "perfect" matches can underperform

### 3. Pattern Recognition Framework

#### String Pattern Analysis
Look for recurring substrings in poor-performing terms:
- Prefixes: "free", "diy", "homemade", "tutorial"
- Suffixes: "jobs", "salary", "definition", "pdf"
- Middle terms: "vs", "versus", "compared to", "alternative"
- Geographic qualifiers: Wrong locations for local businesses

#### Semantic Pattern Analysis
Identify themes across different wordings:
- Price sensitivity: "cheap", "affordable", "budget", "inexpensive"
- Wrong product type: Searching for related but different products
- Wrong use case: B2C terms for B2B products, vice versa
- Wrong buyer stage: Research queries for bottom-funnel campaigns

### 4. Cost Impact Calculation

For each identified negative keyword pattern:

```
Monthly Waste = (Clicks × Avg CPC) × (Days in analysis period / 30)
Estimated Savings = Monthly Waste × 0.95  (5% buffer for legitimate traffic)
Priority Score = (Estimated Savings / Implementation Risk) × 100
```

**Implementation Risk Factors:**
- Exact match negative = Low risk (1.0 multiplier)
- Phrase match negative = Medium risk (1.5 multiplier)
- Broad match negative = High risk (2.5 multiplier)

### 5. Strategic Filtering

Not all poor performers should be negative keywords:

#### Keep if:
- **Seasonality**: Currently low but historically converts
- **New terms**: <30 days in account, needs more data
- **Testing phase**: Part of deliberate expansion strategy
- **Brand protection**: Negative would expose competitors
- **Conversion lag**: Long sales cycle products (check assisted conversions)

#### Consider campaign restructuring instead of negatives if:
- **Wrong match type**: Move to more restrictive match
- **Wrong ad group**: Term relevant but in wrong campaign
- **Wrong landing page**: Traffic quality fine, conversion issue
- **Bid too high**: Lower bid before excluding

### 6. Match Type Decision Matrix

| Pattern Type | Recommended Match Type | Rationale |
|--------------|----------------------|-----------|
| Exact bad query | Exact Match Negative | Blocks only this specific term |
| 2-3 word phrase pattern | Phrase Match Negative | Blocks phrase and close variants |
| Single problematic word | Broad Match Negative (with caution) | Wide blocking, monitor closely |
| Brand name | Exact or Phrase Match | Avoid over-blocking brand variations |
| Modifier words | Broad Match Negative | "free", "jobs", "diy" across all queries |

### 7. Account Level vs Campaign Level

**Add as Account-Level Negatives:**
- Universal irrelevant terms: "jobs", "salary", "free"
- Competitor brands (unless running competitor campaigns)
- Adult/illegal/brand-unsafe terms
- Wrong geographic locations

**Add as Campaign-Level Negatives:**
- Terms relevant to other campaigns but not this one
- Product-specific exclusions
- Different buyer stages (research terms in purchase campaign)
- Different audience segments

### 8. Validation Checklist

Before finalizing negative keyword list:

- [ ] Cross-reference with current negative keyword lists (avoid duplicates)
- [ ] Check Search Terms Report for legitimate variations that might be blocked
- [ ] Verify no negative keywords conflict with target keywords
- [ ] Estimate traffic loss vs cost savings ratio (aim for <5% impression loss)
- [ ] Review with brand/product team for any strategic concerns
- [ ] Document reasoning for each negative keyword tier

## Analysis Output Requirements

For each recommended negative keyword, provide:

1. **The keyword/phrase**
2. **Recommended match type** (Exact, Phrase, or Broad)
3. **Current monthly cost** (if applicable)
4. **Estimated monthly savings**
5. **Reason for exclusion** (1-2 sentence justification)
6. **Implementation level** (Account vs specific campaigns)
7. **Risk rating** (Low/Medium/High)
8. **Priority tier** (Critical/High/Medium/Low)

## Ongoing Monitoring Framework

Post-implementation, monitor:
- **Days 1-7**: Check for unexpected drops in impression volume
- **Day 14**: Review conversion rate changes
- **Day 30**: Calculate actual savings vs forecast
- **Monthly**: Re-run analysis to identify new negative keyword opportunities
