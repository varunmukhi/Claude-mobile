---
name: performance-max-auditor
description: Comprehensive Performance Max campaign audit identifying wastage, missed opportunities, and ROI optimization actions
---

# Performance Max Auditor

Comprehensive audit framework for Google Performance Max campaigns to identify wastage, missed opportunities, and optimization actions that improve ROI and enable profitable scaling.

## What This Skill Does

Analyzes Performance Max campaigns across 7 critical dimensions:
1. **Goal Setup & Conversion Quality** - Validates tracking accuracy and conversion value optimization
2. **Asset Group Performance** - Identifies top/bottom performers and creative gaps
3. **Audience Signals** - Assesses signal strength and expansion opportunities
4. **Bidding Strategy** - Reviews bid strategy effectiveness and pacing
5. **Budget Allocation** - Analyzes spend distribution and scaling potential
6. **Search Term Insights** - Surfaces wasteful queries and negative keyword opportunities
7. **Landing Page Experience** - Evaluates page performance and conversion barriers

**Output**: Executive audit report with prioritized action plan, ROI impact estimates, and implementation roadmap.

## Required Data

Provide Performance Max campaign data in one of these formats:

### Option 1: Google Ads Export (Preferred)
Export from Google Ads UI covering last 30-90 days:
- Campaign overview metrics (impressions, clicks, conversions, cost, conv. value)
- Asset group performance breakdown
- Audience signals performance
- Search term insights report
- Landing page performance
- Conversion actions detail

### Option 2: Spreadsheet/CSV
Include these columns at minimum:
- Campaign metrics: impressions, clicks, CTR, conversions, cost, conv_value, ROAS
- Asset group data: asset_group_name, impressions, clicks, conversions, cost, ROAS
- Audience data: signal_type, impressions, conversions, cost
- Search terms: query, impressions, clicks, cost, conversions
- Landing pages: page_url, sessions, bounce_rate, conversions

### Option 3: Manual Input
Describe your campaign setup and I'll guide you through collecting the necessary data.

## How to Use

### Quick Audit (5 minutes)
```
Audit this Performance Max campaign for wastage and quick wins
[attach campaign data file]
```

### Comprehensive Audit (10-15 minutes)
```
Run full Performance Max audit on this campaign with ROI projections
[attach campaign data file]

Additional context:
- Business goal: [lead gen/ecommerce/app installs]
- Target ROAS: [X]
- Monthly budget: [$X]
- Primary KPI: [conversions/revenue/ROAS]
```

### Focused Audit
```
Audit the asset group performance and audience signals for this PMax campaign
[attach data]
Focus areas: creative fatigue and audience expansion
```

## Audit Framework

The skill applies a systematic 7-point inspection:

### 1. Goal Setup & Conversion Quality (Critical)
- Conversion action validation (primary vs secondary goals)
- Conversion tracking accuracy check
- Value optimization setup review
- Goal conflict detection

**Red Flags**: Multiple conflicting goals, unvalidated conversions, missing value data, micro-conversions weighted equally to sales

### 2. Asset Group Performance Analysis
- Performance distribution across asset groups
- Creative asset utilization rates
- Asset combination effectiveness
- Audience-asset group matching

**Red Flags**: 80%+ spend in 1-2 asset groups, asset groups with <10 asset combinations, declining performance trends, low asset strength scores

### 3. Audience Signals Assessment
- Signal type effectiveness (custom segments, customer lists, demographics)
- Signal strength vs expansion balance
- Audience overlap and cannibalization
- Cold vs warm audience performance

**Red Flags**: No audience signals, over-reliance on broad signals, audience expansion disabled, customer list match rate <40%

### 4. Bidding Strategy Review
- Bid strategy alignment with goals
- Learning phase analysis
- Bid adjustment opportunities
- Pacing and delivery issues

**Red Flags**: Stuck in learning phase, inconsistent daily spend, limited by budget 5+ days/week, target ROAS set too aggressively

### 5. Budget Allocation Analysis
- Daily budget vs impression share
- Budget distribution across asset groups
- Scaling headroom assessment
- Wasted spend identification

**Red Flags**: Budget limited on high-ROAS campaigns, uneven budget distribution, diminishing returns on spend increases

### 6. Search Term Insights
- Query relevance scoring
- Negative keyword opportunities
- Brand vs non-brand performance
- Search theme patterns

**Red Flags**: Irrelevant queries consuming >15% budget, competitor brand terms, low-intent queries, missing negative keyword lists

### 7. Landing Page Experience
- Page-level conversion rate analysis
- Load time and mobile optimization
- Message match assessment
- Conversion barrier identification

**Red Flags**: Pages with <1% CVR getting significant traffic, slow load times (>3s), mobile CR <50% of desktop, unclear CTAs

## Output Format

### Executive Summary
- Overall campaign health score (0-100)
- Top 3 wastage areas with cost impact
- Top 3 growth opportunities with revenue potential
- Quick win recommendations (implement within 7 days)

### Detailed Findings

**For each audit dimension:**
- Current state assessment
- Key metrics and benchmarks
- Issues identified (critical/high/medium priority)
- Optimization opportunities
- Expected impact (revenue/cost savings)

### Action Plan

**Immediate Actions (Week 1)**
1. [Specific action] - Impact: [revenue/savings] - Effort: [hours]
2. [Specific action] - Impact: [revenue/savings] - Effort: [hours]
3. [Specific action] - Impact: [revenue/savings] - Effort: [hours]

**Short-term Optimizations (Weeks 2-4)**
- Action items with implementation steps
- Resource requirements
- Success metrics

**Long-term Strategy (Month 2+)**
- Scaling recommendations
- Testing roadmap
- Monitoring framework

### ROI Impact Projection
- Total wastage identified: $X/month
- Quick win potential: $X revenue in 30 days
- Full optimization potential: $X revenue in 90 days
- Implementation cost: X hours

## Best Practices

**Before Running Audit:**
- Ensure campaign has 30+ days of data (90+ preferred)
- Campaign should have meaningful conversion volume (20+ conversions minimum)
- Have access to Google Ads UI for landing page and asset verification
- Know your business KPIs and profitability thresholds

**During Audit:**
- Answer clarifying questions about business goals and constraints
- Provide additional context about seasonal patterns or recent changes
- Identify any known issues or testing in progress

**After Audit:**
- Implement quick wins within 7 days to capture immediate value
- Track impact of changes using campaign experiments where possible
- Re-audit monthly to identify new optimization opportunities

## Example Use Cases

**Ecommerce Brand Scaling PMax**
- Monthly spend: $50K
- Goal: Increase revenue while maintaining 4.5x ROAS
- Audit identified: $8K/month in irrelevant search traffic, underutilized customer lists, asset fatigue in top asset group
- Impact: Reallocated budget to high-intent audiences, added 47 negative keywords, refreshed creative → 5.2x ROAS, +$15K revenue

**B2B Lead Gen Campaign**
- Monthly spend: $15K
- Goal: Reduce cost per qualified lead
- Audit identified: Multiple conversion actions diluting optimization, poor landing page experience, broad audience signals
- Impact: Consolidated to primary conversion goal, A/B tested landing pages, tightened audience signals → -35% CPL, +40% lead volume

**App Install Campaign Underperforming**
- Monthly spend: $30K
- Goal: Acquire users at <$15 CPA
- Audit identified: Limited by budget daily, no value optimization, weak creative variety
- Impact: Increased budget 40%, implemented tROAS with LTV data, added video assets → $11 CPA, 2x install volume

## Integration with Other Skills

This skill works well with:
- **landing-page-optimizer** - Deep-dive landing page analysis and recommendations
- **negative-keyword-miner** - Extract comprehensive negative keyword lists from search terms
- **creative-testing-framework** - Design asset group testing strategy
- **attribution-modeling-advisor** - Validate conversion attribution setup

## Advanced Features

### Competitive Context Analysis
If you provide competitor data or industry benchmarks, the audit includes:
- Performance vs industry standards
- Competitive positioning assessment
- Share of voice opportunities

### Seasonal Adjustment Recommendations
For campaigns with seasonal patterns:
- Budget pacing recommendations by season
- Audience signal adjustments for peak periods
- Asset rotation strategies

### Multi-Campaign Portfolio Review
When auditing multiple PMax campaigns:
- Cross-campaign cannibalization check
- Budget reallocation recommendations
- Portfolio-level optimization strategy

## For Detailed Methodologies

This skill references comprehensive frameworks in:
- `references/audit-framework.md` - Complete audit methodology and scoring system
- `references/benchmarks.md` - Industry benchmarks and performance standards
- `references/optimization-playbook.md` - Detailed optimization tactics by issue type

To access detailed guidance during an audit, I'll automatically reference these files when needed.

## Tips for Maximum Value

1. **Include Search Terms Data**: This single report often reveals $5K-$20K/month in wastage
2. **Provide Landing Page URLs**: Enables conversion barrier analysis worth 10-30% CVR lift
3. **Share Business Context**: Target margins, LTV, seasonality help prioritize actions correctly
4. **Run Before Budget Increases**: Optimize before scaling to avoid amplifying wastage
5. **Quarterly Cadence**: Re-audit every 90 days as PMax campaigns evolve significantly

## Limitations

- Cannot access your Google Ads account directly (you provide data exports)
- ROI projections are estimates based on typical improvement ranges
- Landing page analysis is visual only (cannot run technical performance tests)
- Requires sufficient data volume for statistical confidence (30+ days, 20+ conversions minimum)

---

**Ready to audit your Performance Max campaign?** Share your campaign data and I'll identify wastage, opportunities, and provide a prioritized action plan with ROI estimates.
