# Diagnostic Framework

## Systematic Performance Analysis Methodology

### The 5-Layer Diagnostic Model

```
Layer 1: BUSINESS OUTCOMES (ROAS, CPA, Revenue)
         ↓
Layer 2: CONVERSION PERFORMANCE (CVR, Lead Quality)
         ↓
Layer 3: TRAFFIC QUALITY (CTR, Engagement)
         ↓
Layer 4: REACH & VISIBILITY (Impressions, IS)
         ↓
Layer 5: ACCOUNT STRUCTURE (Setup, Targeting)
```

Diagnose from top to bottom. Each layer depends on the layers below it.

---

## Layer 1: Business Outcome Analysis

### ROAS (Return on Ad Spend) Diagnostic

**Healthy ROAS Ranges by Industry:**
| Industry | Break-Even | Good | Excellent |
|----------|------------|------|-----------|
| E-commerce | 2.0x | 4.0x | 6.0x+ |
| B2B SaaS | 3.0x | 5.0x | 8.0x+ |
| Lead Gen | 2.5x | 4.0x | 6.0x+ |
| Local Services | 3.0x | 5.0x | 7.0x+ |

**If ROAS is Below Target:**

**Diagnosis Tree:**
1. Is conversion rate adequate? 
   - NO → Problem is Layer 2 (landing page/offer)
   - YES → Continue

2. Is traffic cost reasonable (CPC)?
   - NO → Problem is Layer 3 (CTR/Quality Score)
   - YES → Continue

3. Is traffic volume sufficient?
   - NO → Problem is Layer 4 (reach/budget)
   - YES → Problem is Layer 1 (pricing/LTV)

**Layer 1 Solutions:**
- Increase product prices (if market allows)
- Add upsells/cross-sells
- Improve LTV through retention
- Reduce fulfillment costs
- Target higher-value customers

### CPA (Cost Per Acquisition) Diagnostic

**Healthy CPA Benchmarks:**
| Business Type | Target CPA | Max Acceptable |
|---------------|------------|----------------|
| B2B ($50K ACV) | $500-1,500 | $3,000 |
| B2B ($5K ACV) | $100-500 | $1,000 |
| E-commerce ($100 AOV) | $15-40 | $60 |
| Lead Gen (home services) | $30-80 | $150 |

**CPA Too High - Diagnosis Path:**

```
High CPA
├─ Low Conversion Rate?
│  ├─ Poor landing page → Fix Layer 2
│  ├─ Wrong audience → Fix Layer 4
│  └─ Weak offer → Fix Layer 1
│
├─ High CPC?
│  ├─ Low Quality Score → Fix Layer 3
│  ├─ Overbidding → Fix bidding strategy
│  └─ High competition → Fix targeting
│
└─ Both issues?
   └─ Fundamental mismatch → Revisit Layer 5
```

---

## Layer 2: Conversion Performance Analysis

### Conversion Rate Diagnostic

**Benchmark Conversion Rates by Traffic Source:**
| Source | Cold Traffic | Warm Traffic | Retargeting |
|--------|--------------|--------------|-------------|
| Google Search | 2-5% | 5-10% | 10-20% |
| Meta/Social | 1-3% | 3-7% | 8-15% |
| Display | 0.5-1% | 1-3% | 3-8% |
| LinkedIn | 1-2% | 2-5% | 5-12% |

**If CVR is Below Benchmark:**

**Diagnosis Checklist:**

1. **Traffic Quality Issues** (most common)
   - [ ] Are clicks from the target audience?
   - [ ] Is search intent aligned with offer?
   - [ ] Are negative keywords implemented?
   - [ ] Is geographic targeting appropriate?

2. **Landing Page Problems**
   - [ ] Does page load in <3 seconds?
   - [ ] Is mobile experience optimized?
   - [ ] Does headline match ad promise?
   - [ ] Are trust signals present?
   - [ ] Is CTA clear and prominent?

3. **Offer/Product Issues**
   - [ ] Is value proposition clear?
   - [ ] Is pricing competitive?
   - [ ] Are objections addressed?
   - [ ] Is the offer compelling?

4. **Friction in Conversion Path**
   - [ ] Are there too many form fields?
   - [ ] Is checkout process simple?
   - [ ] Are there unexpected costs?
   - [ ] Is there cart abandonment?

**Conversion Rate Improvement Framework:**

| Issue | Typical Lift | Timeline | Difficulty |
|-------|--------------|----------|------------|
| Page speed optimization | 10-30% | 1 week | Medium |
| Form field reduction | 15-40% | 1 day | Easy |
| Trust signal addition | 5-15% | 1 week | Easy |
| Headline optimization | 10-25% | 1 week | Medium |
| Mobile optimization | 20-50% | 2 weeks | Hard |
| Checkout simplification | 15-35% | 2 weeks | Hard |

### Lead Quality Analysis

**For Lead Generation Campaigns:**

Beyond volume, assess quality:

**Lead Quality Scoring:**
- **Tier 1 (Hot)**: Contacted sales within 24h, qualified budget/timeline
- **Tier 2 (Warm)**: Engaged but slower response or partial qualification
- **Tier 3 (Cold)**: Minimal engagement or not qualified

**Healthy Lead Mix:**
- Tier 1: 20-40%
- Tier 2: 30-50%
- Tier 3: 20-30%

**If Lead Quality is Poor:**
- Tighten targeting (less broad match)
- Add negative keywords
- Increase bid on high-quality sources
- Improve pre-qualification on landing page
- Add friction to filter out tire-kickers

---

## Layer 3: Traffic Quality Analysis

### CTR (Click-Through Rate) Diagnostic

**Benchmark CTRs by Platform & Format:**

**Google Search:**
| Position | Branded | High Intent | Low Intent |
|----------|---------|-------------|------------|
| 1-3 | 8-15% | 5-10% | 2-5% |
| 4-7 | 3-8% | 2-5% | 1-3% |
| 8-10 | 1-3% | 0.5-2% | 0.3-1% |

**Google Display:**
- Standard Display: 0.35-0.50%
- Remarketing: 0.50-1.00%

**Meta (Feed/Story):**
- Feed Ads: 0.90-1.50%
- Story Ads: 1.50-2.50%
- Reel Ads: 2.00-3.00%

**LinkedIn:**
- Sponsored Content: 0.40-0.80%
- InMail: 2.00-5.00%

**Low CTR Diagnosis Tree:**

```
Low CTR
├─ Poor Ad Creative?
│  ├─ Weak headline → Rewrite hook
│  ├─ Generic copy → Add specificity
│  ├─ No clear benefit → Lead with value
│  └─ Poor visual → Refresh creative
│
├─ Wrong Audience?
│  ├─ Targeting too broad → Narrow focus
│  ├─ Not relevant → Refine targeting
│  └─ Ad fatigue → Expand audience
│
├─ Low Ad Position?
│  ├─ Insufficient bid → Increase bids
│  ├─ Low Quality Score → Fix QS issues
│  └─ High competition → Find less competitive keywords
│
└─ Platform/Placement Issues?
   ├─ Poor placement → Exclude low performers
   ├─ Wrong device → Adjust device bidding
   └─ Bad time/day → Implement ad scheduling
```

**CTR Improvement Strategies by Issue:**

| Root Cause | Solution | Expected Lift | Timeline |
|------------|----------|---------------|----------|
| Weak headline | A/B test 5 new headlines | 20-50% | 1-2 weeks |
| Generic ad copy | Add numbers, specifics | 15-30% | 3-7 days |
| Wrong audience | Narrow targeting | 30-100% | Immediate |
| Ad fatigue | Refresh creative | 25-75% | 1 week |
| Low position | Increase bids 20% | 10-30% | Immediate |
| Poor Quality Score | Fix QS factors | 15-40% | 2-4 weeks |

### Engagement Rate Analysis (Meta)

**Benchmark Engagement Rates:**
- Excellent: >4%
- Good: 2-4%
- Average: 1-2%
- Poor: <1%

**Low Engagement Causes:**
1. **Creative Issues** (70% of cases)
   - Not thumb-stopping
   - Doesn't resonate with audience
   - Over-branded/salesy
   - Poor video hook (first 3s)

2. **Audience Issues** (20% of cases)
   - Wrong demographic
   - Audience fatigue
   - Too broad targeting

3. **Platform/Placement** (10% of cases)
   - Wrong placements selected
   - Wrong ad format for objective

---

## Layer 4: Reach & Visibility Analysis

### Impression Share Diagnostic (Google Ads)

**Impression Share Categories:**

| IS Lost to... | What It Means | Solution |
|---------------|---------------|----------|
| Budget | Not enough $ for all auctions | Increase budget or narrow targeting |
| Rank | Bid/QS too low | Increase bids and/or improve Quality Score |
| Both | Multiple issues | Address budget AND bids/QS |

**Healthy Impression Share Targets:**
- **Brand Terms**: 95-100% (defend your brand)
- **High-Intent Commercial**: 70-90%
- **Generic Terms**: 50-70%
- **Competitor Terms**: 30-50%

**Low Impression Share - Action Plan:**

**If Lost to Budget:**
1. Analyze top-performing hours/days
2. Implement ad scheduling
3. Focus budget on best performers
4. Pause/reduce low performers
5. Consider budget increase

**If Lost to Rank:**
1. Check Quality Score by keyword
2. Improve QS components (see Layer 3)
3. Test bid increases (10-20%)
4. Improve ad relevance
5. Enhance landing pages

### Frequency Analysis (Meta)

**Frequency Benchmarks:**
- **Optimal**: 1.5-2.5 (fresh creative, engaged audience)
- **Warning**: 3.0-4.0 (creative fatigue beginning)
- **Critical**: 4.0+ (urgent creative refresh needed)

**High Frequency Issues:**

**At 3.0-4.0 Frequency:**
- CTR typically drops 30-50%
- CPC increases 20-40%
- Relevance score decreases

**Solutions:**
1. **Immediate** (0-3 days):
   - Pause highest frequency ad sets
   - Launch new creative
   - Expand audience size

2. **Short-term** (1-2 weeks):
   - Develop creative rotation schedule
   - Test new hooks/angles
   - Exclude converters

3. **Long-term** (monthly):
   - Build creative production pipeline
   - Test lookalike expansions
   - Implement dynamic creative

---

## Layer 5: Account Structure Analysis

### Campaign Setup Diagnostic

**Common Structural Issues:**

1. **Poor Campaign Organization**
   - Mixing objectives in one campaign
   - No clear theme/audience per campaign
   - Too many campaigns (dilutes learning)

2. **Targeting Problems**
   - Too broad (wastes budget)
   - Too narrow (limits scale)
   - Audience overlap (self-competition)

3. **Bidding Strategy Misalignment**
   - Wrong strategy for objective
   - Insufficient conversion volume for smart bidding
   - No conversion tracking

4. **Keyword Issues** (Google Ads)
   - Too many broad match keywords
   - No negative keyword list
   - Poor match type distribution
   - Irrelevant keywords in ad groups

### Account Hygiene Checklist

**Weekly:**
- [ ] Review search terms, add negatives
- [ ] Check for budget pacing issues
- [ ] Identify ad fatigue (high frequency)
- [ ] Pause zero-conversion ad sets

**Monthly:**
- [ ] Audit Quality Scores
- [ ] Review placement performance
- [ ] Analyze device performance
- [ ] Check geographic performance
- [ ] Assess audience overlap

**Quarterly:**
- [ ] Full account restructure if needed
- [ ] Competitive analysis
- [ ] Landing page refresh
- [ ] Creative overhaul
- [ ] Budget reallocation

---

## Advanced Diagnostic Techniques

### Statistical Significance Testing

**Minimum Sample Sizes for Valid Analysis:**
| Metric | Minimum Sample |
|--------|----------------|
| CTR | 100+ clicks |
| Conversion Rate | 30+ conversions |
| ROAS | 50+ conversions |
| Quality Score | 30 days of data |

**Before making changes, ensure statistical validity.**

### Correlation Analysis

**Common Correlations to Check:**
- CTR vs. Position
- Quality Score vs. CPC
- Frequency vs. CTR (Meta)
- Time of day vs. CVR
- Device vs. CVR

### Segmentation Analysis

**Performance by Segment:**
- Device (mobile vs. desktop vs. tablet)
- Geography (state, city, zip)
- Demographics (age, gender, income)
- Time (hour, day, month)
- Audience type (cold vs. warm vs. hot)

**Identify outliers in each segment for optimization.**

---

## Priority Framework

### Impact vs. Effort Matrix

```
High Impact, Low Effort (DO FIRST)
├─ Add negative keywords
├─ Pause worst performers
├─ Adjust ad scheduling
└─ Exclude poor placements

High Impact, High Effort (PLAN FOR)
├─ Landing page redesign
├─ Account restructure
├─ New creative production
└─ Audience research

Low Impact, Low Effort (QUICK WINS)
├─ Ad copy tweaks
├─ Bid adjustments
├─ Extension additions
└─ Budget shifts

Low Impact, High Effort (DEPRIORITIZE)
├─ Minor copy changes
├─ Over-optimization
├─ Testing low-volume segments
└─ Vanity metric improvements
```

### Expected Timeline for Results

| Change Type | See Results | Full Impact | Confidence |
|-------------|-------------|-------------|------------|
| Bid changes | 1-3 days | 1 week | High |
| Budget changes | 1-3 days | 1 week | High |
| Ad copy tests | 3-7 days | 2 weeks | Medium |
| Creative refresh | 3-7 days | 2 weeks | Medium |
| Quality Score fixes | 1-2 weeks | 4-8 weeks | Low initially |
| Landing page changes | 3-7 days | 2-3 weeks | Medium |
| Account restructure | 1-2 weeks | 4-6 weeks | Low initially |

---

## Platform-Specific Diagnostics

### Google Ads Quality Score Deep Dive

**Component Weights:**
- Expected CTR: ~40%
- Ad Relevance: ~30%
- Landing Page Experience: ~30%

**Diagnosis by Component:**

**Low Expected CTR:**
- Historical CTR below benchmarks
- Ad copy not compelling
- Poor ad extensions
- Low position

**Fix:** A/B test ad copy, add all relevant extensions

**Low Ad Relevance:**
- Keywords don't match ad copy closely
- Ad group too broad (many unrelated keywords)
- Generic ad copy

**Fix:** Tighten ad groups, keyword-to-ad alignment

**Poor Landing Page Experience:**
- Slow load time (>3s)
- Not mobile-friendly
- Low-quality content
- Aggressive ads/pop-ups
- Difficult navigation

**Fix:** Speed optimization, mobile testing, content improvement

### Meta Relevance Diagnostics

**Meta Ad Quality Components:**
- Quality Ranking (compared to ads targeting same audience)
- Engagement Rate Ranking
- Conversion Rate Ranking

**Low Quality Ranking:**
- Creative is low-quality or clickbait
- Too much text in image
- Withholding information
- Sensationalized language

**Low Engagement Rate Ranking:**
- Creative not resonating
- Wrong audience
- Ad fatigue

**Low Conversion Rate Ranking:**
- Landing page issues
- Offer mismatch
- Friction in conversion

---

## Optimization Playbook

### Quick Wins (0-7 Days)

1. **Add Negative Keywords** (Google Ads)
   - Review search terms
   - Add irrelevant terms as negatives
   - Expected savings: 10-20% wasted spend

2. **Pause Worst Performers**
   - Bottom 20% by ROAS/CPA
   - Reallocate to top performers
   - Expected improvement: 15-30%

3. **Adjust Bids on Best Hours**
   - Increase bids +20% on best hours
   - Decrease bids -30% on worst hours
   - Expected improvement: 10-20%

4. **Refresh Fatigued Creative** (Meta)
   - Replace ads with 4.0+ frequency
   - Expected CTR improvement: 50-100%

### Core Optimizations (1-4 Weeks)

1. **Quality Score Improvement Campaign**
   - Focus on keywords with QS 1-5
   - Rewrite ads for relevance
   - Improve landing pages
   - Expected CPC reduction: 20-40%

2. **Landing Page Optimization**
   - Speed optimization (<3s)
   - Mobile responsive design
   - Clear headline-offer match
   - Expected CVR lift: 20-50%

3. **Account Restructure**
   - Create theme-based campaigns
   - Single keyword ad groups (SKAGs) for top terms
   - Expected performance lift: 15-30%

### Advanced Tactics (1-3 Months)

1. **Custom Audience Development**
   - Build first-party audiences
   - Create strategic lookalikes
   - Implement sequential messaging

2. **Sophisticated Bidding**
   - Portfolio bid strategies
   - Value-based bidding
   - Automated rules

3. **Full-Funnel Strategy**
   - Awareness campaigns
   - Consideration campaigns
   - Conversion campaigns
   - Retention campaigns
