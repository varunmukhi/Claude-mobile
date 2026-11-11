# Performance Max Auditor - Usage Examples

Real-world examples showing how to use the Performance Max Auditor skill for different scenarios and business types.

## Example 1: eCommerce Brand Scaling

**Scenario:**
- Online apparel brand
- Monthly spend: $50K
- Goal: Increase revenue while maintaining 4.5x ROAS
- Campaign: 6 months old, performance plateauing

**User Input:**
```
Run comprehensive Performance Max audit

Business context:
- Type: eCommerce (fashion/apparel)
- Monthly budget: $50,000
- Target ROAS: 4.5x
- Primary KPI: Revenue
- Avg order value: $85
- Current ROAS: 4.2x

[Attaches Google Ads exports: campaign overview, asset groups, search terms, landing pages]
```

**Audit Findings:**

**Health Score: 72/100 (Fair)**

**Top Wastage Areas:**
1. **Irrelevant Search Traffic** - $8,400/month (17% of search budget)
   - Queries: "fashion jobs", "how to style", "DIY clothing"
   - 47 high-volume zero-conversion queries
   - Action: Add negative keywords

2. **Asset Group Concentration** - $4,200/month opportunity cost
   - 1 asset group consuming 82% of budget
   - 3 other groups starved of volume
   - Creative fatigue in dominant group (CTR down 24% in 30 days)
   - Action: Refresh creative, rebalance signals

3. **Underutilized Customer Lists** - $3,100/month
   - Customer list uploaded but only 380 matched users (8% match rate)
   - Missing: High-value buyer segments, email hashing
   - Action: Enhance data quality, segment by LTV

**Quick Wins (Week 1):**
1. Add 52 negative keywords → Save $8,400/mo (1.5 hours)
2. Upload enhanced customer list → +$2,400/mo (2 hours)
3. Add 10 new creative assets to main group → +10-15% CTR (3 hours)

**Expected Impact:**
- Month 1: Eliminate $8.4K wastage + $2.4K lift = $10.8K improvement
- Month 2-3: Asset rebalancing + creative refresh = additional $4.2K
- Total: $15K monthly revenue increase, 5.2x ROAS

---

## Example 2: B2B Lead Generation Campaign

**Scenario:**
- SaaS company selling project management software
- Monthly spend: $15K
- Goal: Reduce cost per qualified lead
- Campaign: 3 months old, CPA rising

**User Input:**
```
Audit this PMax campaign - cost per lead is creeping up

Context:
- Business: B2B SaaS (project management)
- Budget: $15,000/month
- Target CPA: $45
- Current CPA: $62
- Lead value: $180 (20% close rate, $900 avg deal)

Main concern: CPA started at $48, now at $62 despite no changes

[Attaches campaign data]
```

**Audit Findings:**

**Health Score: 58/100 (Poor)**

**Critical Issues:**

1. **Conversion Goal Conflict** - Severe
   - Campaign optimizing for 4 different goals simultaneously
   - Primary goal (Demo Requests): Only 32% of conversions
   - Micro-conversions (Newsletter, PDF download): 68% of volume
   - Algorithm confused, optimizing for wrong actions
   - Action: Consolidate to primary goal only

2. **Landing Page Issues** - $3,800/month waste
   - Main landing page: 1.2% CVR (vs 3.8% site average)
   - Issues: Slow load (5.2s), unclear CTA, mobile broken
   - 61% of traffic going to this poor performer
   - Action: Fix technical issues, clarify messaging

3. **Weak Audience Signals** - Efficiency loss
   - No audience signals added (pure automation)
   - Missing: Remarketing, customer match, in-market
   - Action: Layer high-intent audiences

**Immediate Actions:**

1. **Consolidate Conversion Goals** (Day 1)
   - Set Demo Requests as primary
   - Remove micro-conversions from optimization
   - Expected: CPA drop to $48-52 within 14 days

2. **Fix Landing Page** (Week 1)
   - Optimize images → Load time <3s
   - Add clear above-fold CTA
   - Fix mobile responsive issues
   - Expected: CVR improvement 1.2% → 2.5%+

3. **Add Audience Signals** (Week 1)
   - Upload customer list (existing customers)
   - Add website visitors (product pages, pricing)
   - Add in-market segment (project management software)
   - Expected: 20-30% CPA improvement

**Expected Impact:**
- Week 2-3: CPA $48-52 (goal consolidation)
- Week 4-6: CPA $38-42 (landing page + audiences)
- Month 3: CPA $35-40 (sustained), 40% more leads at target cost

---

## Example 3: App Install Campaign

**Scenario:**
- Mobile game developer
- Goal: Acquire users under $15 CPA
- Campaign: Recently launched (6 weeks old)
- Stuck in learning phase

**User Input:**
```
Why is my Performance Max campaign stuck in learning phase?

Campaign details:
- Goal: App installs
- Target CPA: $15
- Budget: $1,000/day ($30K/month)
- Current status: "Learning" for 42 days
- Current CPA: $22 (budget limited 6/7 days)

[Provides campaign data]
```

**Audit Findings:**

**Health Score: 52/100 (Poor)**

**Root Causes:**

1. **Budget Insufficient for Target**
   - Target CPA: $15
   - Daily budget: $1,000
   - Required for learning: $1,500/day minimum (100 installs/day needed)
   - Campaign constantly budget-limited
   - Can't gather enough conversion data

2. **Weak Creative Variety**
   - Only 3 asset groups, each with <8 combinations
   - No video assets (critical for app installs)
   - Asset strength: 2 "Poor", 1 "Average"
   - Low engagement, high CPM

3. **No Value Optimization**
   - All installs treated equally
   - No data on in-app purchases or engagement
   - Algorithm can't distinguish quality users
   - Action: Implement value-based bidding

**Solutions:**

**Option A: Increase Budget**
- Raise to $1,800/day for 14 days
- Allows 100+ installs/day at current CPA
- Exits learning, then optimize down
- Risk: Higher spend during learning

**Option B: Loosen Target**
- Temporarily raise target CPA to $20
- Maintains $1,000/day budget
- Exits learning with volume, then tighten
- Risk: Habituates to higher CPA

**Option C: Hybrid (Recommended)**
- Raise budget to $1,400/day
- Raise target CPA to $18 temporarily
- Add video assets immediately (boosts performance)
- Implement app event values (purchases, level completion)
- After learning exit: Gradually tighten to $15 CPA

**Implementation:**

Week 1:
- Create 5 video assets (15s, 30s variations)
- Implement app event tracking (revenue value)
- Increase budget to $1,400/day
- Raise target CPA to $18

Week 2-3:
- Monitor for learning exit
- Should achieve 100+ installs/day
- CPA: $16-18 during learning

Week 4+:
- Exit learning
- Gradually lower target CPA by $1 every 5 days
- Reach $15 CPA by Week 6-7
- Scale budget back to $1,000/day (now efficient)

**Expected Outcome:**
- Learning exit: Week 2-3
- Stable $15 CPA: Week 7
- 2x install volume at target CPA

---

## Example 4: Quick Audit for Wastage Check

**Scenario:**
- CMO wants quick check before Q4 budget increase
- Just needs wastage identification

**User Input:**
```
Quick audit for wastage - planning to increase budget 50% next month

[Attaches 90-day campaign export]
```

**Audit Focuses On:**
- Search term wastage (primary)
- Asset group efficiency
- Landing page performance
- Budget constraints

**Findings (15 minute audit):**

**Wastage: $6,200/month (12% of spend)**

1. Search Terms: $3,800/mo
   - 23 competitor brand queries
   - "cheap" and "free" modifiers (premium product)
   - Job/career searches

2. Landing Pages: $1,900/mo
   - 1 page with 0.6% CVR getting 18% of traffic
   - Page intended for existing customers, not new

3. Asset Groups: $500/mo
   - 1 group with consistent 1.2x ROAS (target: 4x)
   - Recommend pause/rebuild

**Recommendation:**
"Clean up wastage first (2-3 hours work), then increase budget. This will save $6.2K/month and ensure budget increase goes to productive traffic. Scaling wasteful campaign amplifies waste."

**Quick Fixes:**
1. Add negative keywords (1 hour)
2. Exclude poor landing page (5 minutes)
3. Pause weak asset group (5 minutes)
4. Then proceed with 50% budget increase

---

## Example 5: Seasonal Campaign Audit

**Scenario:**
- Preparing for Black Friday/Cyber Monday
- Want to ensure campaign optimized for peak season

**User Input:**
```
Audit this campaign before Black Friday - want to make sure it's ready to scale

Current state:
- Running for 4 months
- Performance good (5.2x ROAS)
- Planning 3x budget increase for BFCM week
- Concerned about maintaining efficiency at scale

[Provides data]
```

**Audit Focuses On:**
- Scalability headroom
- Creative fatigue risk
- Audience saturation
- Landing page capacity

**Findings:**

**Health Score: 83/100 (Good) - Ready to scale with optimizations**

**Scaling Readiness:**

✅ Strong fundamentals (5.2x ROAS sustained)
✅ High impression share loss to budget (38%) - room to grow
⚠️ Creative may fatigue under 3x volume
⚠️ Landing pages not tested at high traffic
❌ No BFCM-specific messaging in assets

**Pre-BFCM Optimizations:**

**Week 1: Creative Preparation**
- Add Black Friday themed assets (headlines, images)
- Create urgency-focused copy ("Limited time", "While supplies last")
- Test at 1.5x budget first
- Expected: Maintains or improves ROAS with seasonal relevance

**Week 2: Landing Page Load Testing**
- Current page load: 2.8s at normal traffic
- At 3x traffic: Could degrade to 5+ seconds
- Action: CDN setup, image compression, caching
- Expected: Prevents 15-25% conversion loss from slow loads

**Week 3: Audience Expansion Prep**
- Current: Tight audience signals (minimal expansion)
- For scale: Allow 40% expansion temporarily
- Add lookalike audiences for reach
- Expected: 2-3x volume available

**Week 4 (BFCM): Scale Execution**
- 3x budget increase
- Monitor hourly for first 2 days
- Accept 10-15% ROAS decline as cost of volume
- Expected: 2.5-3x revenue at 4.5-4.8x ROAS

**Post-BFCM:**
- Remove seasonal creative
- Reduce budget to 1.2-1.5x normal (new baseline)
- Audience signals back to tight targeting
- Resume normal 5x+ ROAS

---

## Data Format Examples

### Minimum CSV Format

**campaign_overview.csv:**
```csv
campaign_name,impressions,clicks,ctr,conversions,cost,conv_value,roas
PMax - Main,1200000,48000,4.0%,856,$45000,$210000,4.67
```

**asset_groups.csv:**
```csv
asset_group_name,impressions,clicks,conversions,cost,roas
Product Benefits,720000,28800,512,$27000,4.8
Product Features,360000,14400,256,$13500,3.6
Seasonal Promo,120000,4800,88,$4500,4.0
```

**search_terms.csv:**
```csv
query,impressions,clicks,cost,conversions
running shoes,45000,1800,$2700,45
nike running shoes,12000,480,$960,2
how to run faster,8000,320,$480,0
running shoes jobs,3000,120,$180,0
```

### Ideal Format (More Data)

Add these columns for deeper insights:

**asset_groups.csv** (enhanced):
```csv
asset_group_name,impressions,clicks,conversions,cost,roas,asset_strength,active_assets,landing_page
Product Benefits,720000,28800,512,$27000,4.8,Good,12,/shop/benefits
Product Features,360000,14400,256,$13500,3.6,Average,8,/shop/features
```

**audiences.csv:**
```csv
signal_type,signal_name,impressions,conversions,cost,roas
Customer List,30-day buyers,180000,156,$6750,6.2
Custom Segment,In-market runners,240000,184,$8100,4.5
Remarketing,Cart Abandoners,120000,98,$4500,5.1
Demographics,High income,660000,418,$25650,3.8
```

**landing_pages.csv:**
```csv
page_url,sessions,bounce_rate,avg_time,conversions,cvr
/shop/running-shoes,24000,38%,125s,612,2.55%
/shop/category/athletic,12000,52%,87s,156,1.30%
/shop/sale,8400,45%,98s,88,1.05%
```

---

## Troubleshooting Examples

### "Not enough data"
**Problem:** Campaign only 2 weeks old
**Solution:** Wait until 30+ days and 20+ conversions, or provide multiple campaigns to analyze collectively

### "Can't assess search terms"
**Problem:** No search terms data provided
**Solution:** In Google Ads: Insights → Search Terms → Download (or note if no data available - PMax requires time to accumulate)

### "Generic recommendations"
**Problem:** Audit feels template-like
**Solution:** Provide business context - industry, margins, goals, competitive landscape, and any known issues

---

**These examples show the skill's flexibility across business types, goals, and audit depths. Adapt the input detail to your needs - from quick wastage checks to comprehensive strategic audits.**
