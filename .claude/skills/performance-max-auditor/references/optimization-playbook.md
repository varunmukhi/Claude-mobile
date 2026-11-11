# Performance Max Optimization Playbook

Tactical playbook for addressing common Performance Max issues with step-by-step implementation guides and expected impact ranges.

## Goal & Conversion Optimization Tactics

### Tactic 1: Implement Conversion Value Rules

**When to Use:**
- All conversions currently set to equal value ($1 or same value)
- Different conversion types have different business value
- Product catalog has varying margins or LTV

**Implementation Steps:**
1. Audit all conversion actions in Google Ads
2. Assign values based on:
   - eCommerce: Transaction value (automatic if tracking set up)
   - Lead gen: Lead value = (Close rate × Avg deal size) OR (LTV × conversion rate)
   - Multi-product: Weighted average by product/category
3. In Google Ads: Goals → Conversion Actions → Select action → Edit → Value
4. For dynamic values: Set up conversion value rules or import from CRM
5. Allow 14-21 days for algorithm to adjust to new values

**Expected Impact:**
- ROAS improvement: 20-40% within 30 days
- Conversion volume: May decrease 10-20% as focus shifts to higher value
- Overall revenue: +15-35%

**Monitoring:**
- Check daily: Conversion mix (are high-value conversions increasing?)
- Weekly: ROAS trend (should stabilize at higher level)
- Monthly: Revenue per conversion (should increase)

### Tactic 2: Consolidate Conversion Goals

**When to Use:**
- Multiple conversion goals competing for optimization
- Primary goal getting <50% of total conversion volume
- Inconsistent performance week-to-week

**Implementation Steps:**
1. Identify primary business goal (what drives revenue/profit?)
2. Secondary goals: Set as "Secondary" in conversion action settings
3. Alternative: Create separate campaigns for fundamentally different goals
4. Remove micro-conversions from optimization (page views, scrolls, etc.)
5. If keeping secondary: Assign value weights (e.g., lead = $50, demo = $200, sale = $500)

**Expected Impact:**
- Primary goal efficiency: +15-30%
- Campaign stability: Reduced week-to-week variance
- Learning phase: May reset temporarily (7-14 days)

**Edge Cases:**
- If primary goal volume <20 conversions/week: Keep secondary goals to maintain volume
- Seasonal businesses: Adjust goal priority by season

### Tactic 3: Fix Tracking Implementation

**Common Tracking Issues:**

**Issue: Duplicate Conversions**
- Symptom: Conversion rate >10%, conversions > clicks
- Cause: Tag firing multiple times per page load
- Fix: Implement tag sequencing, use single tag container
- Impact: Accurate data → proper optimization

**Issue: Missing Enhanced Conversions**
- Symptom: Match rate <60%, limited first-party data
- Cause: Enhanced conversions not implemented
- Fix: Enable enhanced conversions in Google Ads, hash user data client-side
- Impact: +20-40% match rate, better attribution

**Issue: Server-Side Tracking Gaps**
- Symptom: iOS 14+ traffic shows 30-50% lower conversion rate
- Cause: Client-side tracking blocked by privacy features
- Fix: Implement Google Tag Manager server-side container
- Impact: Recover 20-40% of "lost" conversions

## Asset Group Optimization Tactics

### Tactic 4: Rebalance Asset Group Budgets

**When to Use:**
- One asset group consuming >70% of spend
- Multiple asset groups with <5% impression share each
- Wide ROAS variance between groups (5x+ difference)

**Rebalancing Strategy:**

**Scenario A: One dominant high-performer**
```
Current State: Asset Group A = 85% spend, 6x ROAS
               Asset Groups B,C,D = 5% spend each, 3-4x ROAS

Action Plan:
1. Don't throttle the winner - let it spend
2. Investigate why others underperform:
   - Weak audience signals? → Add signals from Group A
   - Poor assets? → Replicate winning creative themes
   - Wrong targeting? → Review final URL destinations
3. Give 2-3 weeks to improve
4. If still no improvement: Consolidate into Group A

Expected: Maintain high ROAS while potentially unlocking new volume
```

**Scenario B: Multiple groups, no clear winner**
```
Current State: 4 asset groups, 15-35% spend each, 2-4x ROAS variance

Action Plan:
1. Analyze what differentiates high performers:
   - Audience signals (custom lists vs broad)
   - Creative themes (benefits vs features)
   - Landing pages (product pages vs category pages)
2. A/B test insights: Replicate winning elements to weak groups
3. Pause groups that can't reach 3x target ROAS after 30 days

Expected: 15-25% efficiency improvement through elimination
```

### Tactic 5: Combat Creative Fatigue

**Detection:**
- CTR declining 20%+ over 30 days
- Same 2-3 combinations serving 80%+ impressions
- Engagement rate dropping
- ROAS stable or declining with CTR drop

**Refresh Strategies:**

**Quick Refresh (2-3 hours work):**
1. Add 5-10 new headline variations
   - Test different value propositions
   - Add urgency/scarcity elements
   - Test question-based headlines
2. Upload 3-5 new image variations
   - Different colors/backgrounds
   - New angles/compositions
   - Lifestyle vs product-only
3. Add 1-2 new description blocks
4. Expected impact: 10-20% CTR recovery in 7-14 days

**Comprehensive Refresh (1-2 days work):**
1. Full creative audit: What's working vs. not?
2. Develop new creative themes (3-4 distinct angles)
3. Create 15+ headlines, 5+ descriptions per theme
4. Produce 10+ new images/graphics
5. Add video if not present (15s, 30s versions)
6. Rotate in 50% new assets, keep 50% existing winners
7. Expected impact: 20-40% performance boost

**Frequency Recommendations:**
- B2C eCommerce: Refresh every 30-45 days
- B2B: Refresh every 60-90 days
- Seasonal/Promotional: Refresh with each season/promotion

### Tactic 6: Improve Asset Strength Scores

**Score Improvement Roadmap:**

**Poor → Average:**
- Add assets to minimum: 10 headlines, 4 descriptions, 4 images
- Ensure headlines vary in length (short/medium/long)
- Add at least 1 video (even stock footage with overlay text)
- Include business name in 2-3 headlines
- Time to impact: 24-48 hours for review

**Average → Good:**
- Expand to 15 headlines, 5 descriptions, 10 images
- Add 2-3 videos (different lengths)
- Diversify headlines: features, benefits, questions, CTAs
- Include popular keywords in headlines
- Add logo if not present
- Time to impact: 48-72 hours

**Good → Excellent:**
- Max out assets: 20 headlines, 5 descriptions, 20 images
- Add 5+ videos covering different themes
- Ensure headline diversity: 30% features, 30% benefits, 20% social proof, 20% CTAs
- High-quality, unique images (not stock photos)
- Square AND landscape images for all placements
- Time to impact: 3-7 days

**Impact on Performance:**
- Poor → Good: 10-20% impression share increase
- Good → Excellent: 5-10% additional reach, minor efficiency gain

## Audience Signal Optimization Tactics

### Tactic 7: Build High-Value Customer Lists

**Customer List Strategy:**

**Segmentation Tiers:**
1. **Tier 1 - High Value** (30-day purchasers, top 20% LTV)
   - Highest signal weight
   - Tightest targeting
   - Premium messaging
   
2. **Tier 2 - Recent Buyers** (90-day purchasers)
   - Medium signal weight
   - Moderate targeting
   - Retention/upsell messaging
   
3. **Tier 3 - All Customers** (365-day)
   - Lower signal weight
   - Expansion allowed
   - Win-back messaging

**Upload Process:**
1. Export customer data with: email, phone, first name, last name, zip
2. Hash data (SHA-256) before upload OR let Google Ads hash
3. Upload to Google Ads: Audience Manager → Audience Lists → Customer List
4. Wait 24-48 hours for processing
5. Check match rate (need >40%, ideal >60%)
6. Add to PMax campaign as audience signal

**Match Rate Optimization:**
- Include multiple identifiers (email + phone + name)
- Format phone numbers consistently (+1XXXXXXXXXX)
- Use customer's actual email (not company alias)
- Upload 1,000+ users minimum for reliable matching

**Expected Impact:**
- Customer list ROAS: 2-4x higher than cold audiences
- Overall campaign ROAS: +15-30% when properly weighted

### Tactic 8: Layer High-Intent Audiences

**High-Intent Signal Stack:**

**Website Visitors (Intent Signals):**
- Product page viewers (90 days)
- Cart abandoners (30 days)
- High-engagement visitors (3+ pages, 2+ minutes)
- Checkout initiators

**Custom Segments:**
- In-market audiences (currently researching)
- Affinity audiences (relevant interests)
- Life events (weddings, new parents, new homeowners)

**Demographics (When Relevant):**
- Household income (if price-sensitive)
- Parental status (if family products)
- Education/occupation (if B2B)

**Layering Strategy:**
```
Asset Group A: Warm (50% weight) + In-Market (30%) + Demographics (20%)
Asset Group B: Cart Abandoners (70%) + Lookalike (30%)
Asset Group C: Product Viewers (40%) + Affinity (30%) + Expansion (30%)
```

**Expected Impact:**
- Intent-based signals: 1.5-2.5x ROAS vs broad
- Layered approach: 20-35% efficiency improvement

### Tactic 9: Control Audience Expansion

**Expansion Settings:**

**When to Limit Expansion (<20%):**
- Strong existing signals (customer lists, high-intent remarketing)
- Niche products with specific audience
- High CPA tolerance is low
- Already achieving target ROAS

**When to Allow Expansion (30-50%):**
- Weak signals or broad signals only
- Mass-market products
- Scaling phase (need volume)
- ROAS well above target (can afford exploration)

**Optimization Path:**
```
Week 1-2: Start with 40% expansion, monitor performance
Week 3-4: If expansion performs well (ROAS >80% of target), increase to 50%
         If expansion underperforms (<60% of target), reduce to 20%
Month 2+: Adjust based on volume needs and efficiency goals
```

## Bidding & Budget Optimization Tactics

### Tactic 10: Exit Learning Phase Faster

**Stuck in Learning Troubleshooting:**

**Cause: Insufficient Conversion Volume**
- Symptom: <50 conversions in 14 days
- Solutions:
  1. Temporarily loosen target (tROAS from 5x → 4x)
  2. Include secondary conversion goals temporarily
  3. Expand geographic targeting
  4. Increase budget 30-50%
- Timeline: 7-14 days to exit learning

**Cause: Frequent Campaign Changes**
- Symptom: Re-enters learning 3+ times per month
- Solutions:
  1. Batch changes (make edits once per week max)
  2. Avoid budget changes >20% in single day
  3. Don't adjust targets during learning
  4. Use experiments for major tests
- Timeline: 14 days of stability needed

**Cause: Target Too Aggressive**
- Symptom: Very low impression share, limited delivery
- Solutions:
  1. Reduce target by 20-30% temporarily
  2. Switch from tROAS to Maximize Conv Value
  3. Review competitive landscape (are bids high enough?)
- Timeline: Immediate impact on delivery

### Tactic 11: Optimize Bid Strategy Selection

**Decision Tree:**

**Goal: Maximize Revenue, No Efficiency Constraint**
- Strategy: Maximize Conversion Value
- When: Strong margins, can absorb variable CPA
- Setup: No target, let algorithm spend freely within budget
- Expected: Highest revenue, variable ROAS (typically 3-5x)

**Goal: Profitable Revenue Growth**
- Strategy: Target ROAS
- When: Known profitability threshold
- Setup: tROAS = (Avg order value × Margin%) / Target CPA
- Example: $100 order, 40% margin → Break-even = 2.5x ROAS → Target 3.5x for safety
- Expected: Consistent efficiency, scalable

**Goal: Volume at Acceptable Cost (Lead Gen)**
- Strategy: Target CPA
- When: Leads valued equally, cost control critical
- Setup: tCPA = (Lead value × Close rate × Margin)
- Example: Qualified lead worth $500, 20% close, 40% margin → Target $40 CPA
- Expected: Steady lead flow, predictable costs

**Switching Strategies:**
- Allow 14 days after switch for re-optimization
- Expect 10-20% performance variance during transition
- Don't switch back and forth (causes instability)

### Tactic 12: Scale Without Sacrificing Efficiency

**Scaling Playbook:**

**Phase 1: Validate Headroom (Week 1)**
- Check impression share lost to budget
- If >30% IS lost: High confidence in scaling
- If 15-30%: Moderate confidence
- If <15%: Limited headroom, focus on efficiency first

**Phase 2: Conservative Test (Week 2-3)**
- Increase budget 20-30%
- Monitor ROAS daily (should stay within 15% of baseline)
- If ROAS holds: Proceed to Phase 3
- If ROAS drops >20%: Roll back, improve efficiency

**Phase 3: Aggressive Scale (Week 4+)**
- Increase budget 40-60%
- Accept 10-15% ROAS decline as cost of volume
- Monitor absolute profit (revenue - cost) not just ROAS
- Formula: Profitable if (New Revenue × Margin) > (Old Revenue × Margin)

**Example:**
```
Baseline: $10K spend, 5x ROAS = $50K revenue
Scale Test: $15K spend, 4.2x ROAS = $63K revenue

Profit Analysis (assuming 40% margin):
Baseline Profit: ($50K × 0.4) - $10K = $10K
Scaled Profit: ($63K × 0.4) - $15K = $10.2K

Verdict: Scale successful (profit increased despite ROAS drop)
```

**Scaling Limits:**
- Stop scaling if ROAS drops >30% (likely unprofitable)
- Stop if conversion rate drops >25% (quality declining)
- Stop if CPA rises above profitability threshold

## Search Term Optimization Tactics

### Tactic 13: Build Negative Keyword Lists

**Negative Keyword Themes:**

**Category 1: Zero Commercial Intent**
- how, what, why, when, where (as first word)
- tutorial, guide, tips, advice
- learn, course, class, training
- free, cheap, discount, coupon (if high-ticket)
- review, comparison, vs, alternative (sometimes)

**Category 2: Wrong Audience**
- jobs, careers, hiring, employment, salary
- internship, apprentice, entry level
- wholesale, bulk, distributor (if B2C)
- DIY, homemade, recipe (if selling finished product)

**Category 3: Competitor Brands**
- List major competitor brand names
- Competitor product names
- Alternative spellings/misspellings

**Category 4: Irrelevant Modifiers**
- cheap, free, discount (if premium brand)
- used, secondhand, refurbished (if new only)
- rental, lease, rent (if selling)
- size/color specific if out of stock

**Implementation:**
1. Export search terms report (90 days)
2. Flag queries with 0 conversions, >10 clicks
3. Categorize by theme above
4. Create negative keyword lists in Google Ads
5. Apply to all PMax campaigns
6. Review and add 5-10 new negatives monthly

**Expected Impact:**
- Wastage reduction: 10-25% of search spend
- CTR improvement: 5-15% (fewer irrelevant impressions)
- Conversion rate: +10-20% (better traffic quality)

### Tactic 14: Exclude Competitor Brand Traffic

**When to Exclude:**
- Competitor terms >5% of spend
- Competitor terms convert at <30% of avg CVR
- Your brand is not well-known alternative

**When to Keep:**
- Your brand is direct alternative
- Competitor terms convert well
- Conquesting is part of strategy

**Selective Exclusion:**
```
Negative: "[competitor name] + discount/coupon/login/support"
Keep: "[competitor name] + alternative/vs/replacement"
```

**Expected Impact:**
- Spend reallocation: 5-15% budget freed up
- Quality improvement: +10-20% overall CVR

## Landing Page Optimization Tactics

### Tactic 15: Fix High-Traffic Low-Converting Pages

**Diagnostic Process:**
1. Identify pages with >10% traffic, CVR <50% of average
2. Analyze with landing-page-optimizer skill for specific issues
3. Prioritize fixes by traffic volume × CVR gap

**Common Fixes & Impact:**

**Slow Load Time (>3 seconds)**
- Fix: Compress images, enable caching, use CDN
- Expected: 10-30% CVR improvement
- Timeline: Immediate (technical fixes)

**Missing/Unclear CTA**
- Fix: Add prominent above-fold CTA, repeat below fold
- Expected: 15-40% CVR improvement
- Timeline: 1-2 days (design changes)

**Form Friction**
- Fix: Reduce fields (8+ → 4-5), add autofill, inline validation
- Expected: 20-50% form completion improvement
- Timeline: 1-3 days (development)

**Mobile UX Issues**
- Fix: Responsive design, larger tap targets, simplified navigation
- Expected: 30-60% mobile CVR improvement
- Timeline: 3-7 days (redesign)

**Message Mismatch**
- Fix: Align headline/offer with ad messaging
- Expected: 25-50% CVR improvement
- Timeline: 1-2 days (copywriting)

### Tactic 16: A/B Test Landing Page Variants

**Testing Framework:**

**Hypothesis-Driven Testing:**
1. Identify primary conversion barrier (e.g., "unclear value proposition")
2. Develop variant addressing specific barrier
3. Split traffic 50/50 for 2-4 weeks (need 100+ conversions per variant)
4. Measure CVR, bounce rate, time on page
5. Implement winner, test next hypothesis

**High-Impact Test Ideas:**

**Test 1: Long-Form vs Short-Form**
- Short: Headline, 3 bullets, CTA, image
- Long: Detailed explanation, FAQs, testimonials, multiple CTAs
- Best for: Complex products (long-form), impulse purchases (short-form)

**Test 2: Single CTA vs Multiple CTAs**
- Single: One action, one button, no distractions
- Multiple: Different entry points (demo, trial, buy, contact)
- Best for: Single product (single CTA), varied audience intent (multiple)

**Test 3: Social Proof Variations**
- Testimonials vs Statistics vs Logos vs Reviews
- Placement: Above fold vs mid-page vs sidebar
- Best for: Test what builds trust for your audience

**Expected Impact:**
- Winning variant: 10-40% CVR improvement over control
- Compound effect: 3-4 winning tests = 30-80% total CVR improvement

---

**This playbook provides specific, actionable tactics for every common Performance Max challenge. Use in combination with audit findings to prioritize highest-ROI optimizations.**
