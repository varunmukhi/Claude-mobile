# Google Ads Quality Score Deep Dive

## Understanding Quality Score

### What Quality Score Is

Quality Score is Google's 1-10 rating of the quality and relevance of your keywords, ads, and landing pages. It's calculated for each keyword and affects:

**Ad Rank = Max CPC × Quality Score + Ad Extensions**

Higher Quality Score = Higher ad position at lower cost

### Why Quality Score Matters

**Financial Impact:**
| Quality Score | CPC vs QS 5 | Ad Rank Impact |
|---------------|-------------|----------------|
| 10 | -50% | +100% |
| 9 | -44% | +80% |
| 8 | -37% | +60% |
| 7 | -28% | +40% |
| 6 | -17% | +20% |
| 5 | Baseline | Baseline |
| 4 | +25% | -20% |
| 3 | +67% | -40% |
| 2 | +150% | -60% |
| 1 | +400% | -80% |

**Example:**
- Keyword with QS 3 costs $10/click
- Same keyword with QS 8 costs $6.30/click
- **That's 37% savings for the same traffic**

---

## The Three Components

### 1. Expected CTR (40% weight)

**What It Measures:**
How likely your ad is to be clicked when shown, based on historical performance and keyword relevance.

**Rated As:**
- Above average
- Average  
- Below average

**What Affects Expected CTR:**

**Positive Factors:**
- High historical CTR for this keyword
- Keyword in ad headline
- Relevant ad copy
- Strong ad extensions
- Top ad positions
- Match type alignment (exact > phrase > broad)

**Negative Factors:**
- Low historical CTR
- Generic ad copy
- Keyword not in ad
- Few/no extensions
- Bottom positions
- Irrelevant keyword-ad match

**How to Improve:**

**Quick Wins (1-2 weeks):**
1. **Include keyword in headline 1**
   ```
   Bad: "Great Accounting Software"
   Good: "Cloud Accounting Software for SMBs"
   (for keyword: "cloud accounting software")
   ```

2. **Add all relevant extensions**
   - Sitelinks (4 minimum)
   - Callouts (4 minimum)
   - Structured snippets
   - Call extensions
   **Impact**: +10-20% CTR typically

3. **Write compelling CTAs**
   ```
   Bad: "Learn More"
   Good: "Start Free Trial - No Credit Card"
   ```

4. **Test emotional triggers**
   - Urgency: "Limited Time Offer"
   - Scarcity: "Only 5 Spots Left"
   - Social proof: "Join 10,000+ Users"

**Medium-Term (2-4 weeks):**
1. **A/B test ad copy variations**
   - Test 3-5 headlines per ad group
   - Focus on benefit-driven copy
   - Include numbers/stats when possible

2. **Improve ad position**
   - Bid for positions 1-3 temporarily
   - Higher position → higher CTR → better expected CTR rating
   - Once CTR improves, can reduce bids

3. **Use Dynamic Keyword Insertion (carefully)**
   ```
   Headline: "Buy {KeyWord:Shoes} Online"
   Shows as: "Buy Running Shoes Online" (for "running shoes")
   ```

**Expected Results:**
- CTR improvement: 30-100%
- Timeline: 2-4 weeks for full impact
- QS component: "Below average" → "Above average"

---

### 2. Ad Relevance (30% weight)

**What It Measures:**
How closely your ad copy matches the intent of your keyword.

**Rated As:**
- Above average
- Average
- Below average

**What Affects Ad Relevance:**

**Positive Factors:**
- Keyword appears in ad (headline or description)
- Ad specifically addresses keyword intent
- Tight keyword grouping (5-15 related keywords per ad group)
- Match type appropriate to keyword
- Landing page relevance

**Negative Factors:**
- Generic ad copy
- Too many unrelated keywords in ad group
- Broad match keywords with generic ads
- Keyword-ad disconnect

**How to Improve:**

**Immediate Actions:**
1. **Create Single Keyword Ad Groups (SKAGs)**
   - One keyword per ad group (or very close variants)
   - Ad can be perfectly tailored to keyword
   - Maximum relevance
   
   Example SKAG structure:
   ```
   Campaign: Accounting Software
   ├─ Ad Group: cloud accounting software
   │  └─ Keywords: [cloud accounting software] (exact)
   │  └─ Ad: "Cloud Accounting Software | Try Free..."
   ├─ Ad Group: small business accounting
   │  └─ Keywords: [small business accounting] (exact)
   │  └─ Ad: "Small Business Accounting | Simple & Affordable..."
   ```

2. **Mirror keyword in ad copy**
   ```
   Keyword: "crm software for real estate"
   
   Headline 1: CRM Software For Real Estate
   Headline 2: Built for Real Estate Agents
   Description: Real estate CRM trusted by 5,000+ agents...
   ```

3. **Align ad to search intent**
   - Informational intent → Educational ad
   - Commercial intent → Comparison/feature ad
   - Transactional intent → Offer/pricing ad

**Example:**
```
Keyword: "best crm software" (commercial intent)

Bad Ad:
"CRM Software | Try Now"

Good Ad:
"Best CRM Software 2024
Rated #1 by G2 Crowd
Compare Features - See Pricing
Start Free Trial Today"
```

**Advanced Tactics:**
1. **Dynamic Keyword Insertion + backup**
   ```
   {KeyWord:CRM Software} for Sales Teams
   If keyword fits: "Salesforce Alternative for Sales Teams"
   If too long: "CRM Software for Sales Teams"
   ```

2. **Use keyword themes, not individual keywords**
   - Group semantically related keywords
   - Write ads that cover the theme
   
   Example theme: "CRM pricing"
   Keywords: crm pricing, crm cost, crm price, crm subscription cost
   Ad: "CRM Pricing | Plans Starting at $12/user/month"

**Expected Results:**
- Ad Relevance: "Below average" → "Above average"
- Timeline: Immediate impact after restructure
- QS improvement: +1-2 points typically

---

### 3. Landing Page Experience (30% weight)

**What It Measures:**
How relevant, useful, and user-friendly your landing page is for people clicking your ad.

**Rated As:**
- Above average
- Average
- Below average

**What Affects Landing Page Experience:**

**Positive Factors:**
- Fast load time (<3 seconds)
- Mobile-optimized (responsive design)
- Keyword/ad promise on landing page
- Clear, relevant content
- Easy navigation
- Transparent about business
- HTTPS (secure)
- Trust signals (testimonials, reviews, badges)
- Clear CTA
- No excessive ads/pop-ups

**Negative Factors:**
- Slow load time (>5 seconds)
- Not mobile-friendly
- Ad promise doesn't match page
- Thin content
- Pop-ups immediately on arrival
- Difficult navigation
- Not secure (HTTP)
- Generic or irrelevant content

**How to Improve:**

**Priority 1: Page Speed (Biggest Impact)**

**Target: <3 seconds on mobile**

Use Google PageSpeed Insights to audit: https://pagespeed.web.dev/

**Common Issues & Fixes:**
1. **Large images** (>200KB)
   - Compress images (TinyPNG, ImageOptim)
   - Use WebP format
   - Implement lazy loading
   **Impact**: 1-3 second improvement

2. **Render-blocking JavaScript**
   - Defer non-critical JS
   - Minimize third-party scripts
   - Use async loading
   **Impact**: 0.5-2 second improvement

3. **No caching**
   - Enable browser caching
   - Use CDN for static assets
   **Impact**: 0.5-1.5 second improvement

4. **Slow server response**
   - Upgrade hosting
   - Enable server caching
   - Optimize database queries
   **Impact**: 0.5-2 second improvement

**Priority 2: Mobile Optimization**

**Requirements:**
- Responsive design (adapts to screen size)
- Touch-friendly buttons (44x44px minimum)
- Readable text (16px+ font size)
- No horizontal scrolling
- Fast tap-to-call for phone numbers

**Test On:**
- iPhone (most common)
- Android device
- Tablet
- Google's Mobile-Friendly Test

**Priority 3: Content Relevance**

**Checklist:**
- [ ] Headline includes keyword from ad
- [ ] First paragraph addresses ad promise
- [ ] Content is original and substantive (not thin)
- [ ] Internal linking is reasonable
- [ ] Contact information easily findable
- [ ] Clear value proposition above fold
- [ ] Relevant images/videos

**Example:**
```
Ad: "Cloud Accounting Software | Free 30-Day Trial"

Landing Page:
❌ Generic "About Us" page
❌ Homepage with 10 different products
✅ Dedicated "Cloud Accounting Software" page
    with:
    - H1: "Cloud Accounting Software for Small Business"
    - CTA: "Start Free 30-Day Trial"
    - Features, pricing, testimonials
```

**Priority 4: User Experience**

**Eliminate Friction:**
1. **Reduce pop-ups**
   - No immediate pop-ups (wait 30+ seconds)
   - Exit-intent only
   - Easy to close

2. **Simplify navigation**
   - Clear menu structure
   - Breadcrumbs for deep pages
   - Search functionality

3. **Add trust signals**
   - Customer testimonials (with photo + name)
   - Security badges (SSL, payment processors)
   - Industry certifications
   - Review stars/ratings
   - Press mentions

4. **Clear CTA**
   - Above the fold
   - Contrasting color
   - Action-oriented ("Start Free Trial" not "Submit")
   - Single primary CTA per page

**Expected Results:**
- Landing Page Experience: "Below average" → "Above average"
- Timeline: 2-4 weeks after implementation
- QS improvement: +2-3 points
- Bonus: Conversion rate typically improves 20-60%

---

## Quality Score Monitoring

### How to Check Quality Score

**In Google Ads:**
1. Go to Keywords tab
2. Click "Columns" icon
3. Select "Quality Score" metrics:
   - Quality Score
   - Landing Page Exp.
   - Exp. CTR
   - Ad Relevance

**Important:** Google only shows QS for keywords with sufficient impressions (typically 100+ in last 90 days)

### Historical Quality Score Tracking

**Set up custom columns:**
- Qual. Score (hist.)
- Landing Page Exp. (hist.)
- Exp. CTR (hist.)
- Ad Relevance (hist.)

This shows QS changes over time to measure improvement efforts.

### QS Reporting Dashboard

**Weekly Monitoring:**
- % of keywords with QS 1-3 (urgent fixes)
- % of keywords with QS 4-5 (improvement opportunities)
- % of keywords with QS 6-7 (good, maintain)
- % of keywords with QS 8-10 (excellent, protect)
- Average QS across account
- QS trend (improving/declining/stable)

**Target Distribution:**
- QS 8-10: 40-60% of keywords
- QS 6-7: 30-40%
- QS 4-5: 10-20%
- QS 1-3: 0-5%

---

## Quality Score Improvement Roadmap

### Phase 1: Triage (Week 1)

**Goal:** Identify and prioritize keywords

1. **Export all keywords with QS data**
2. **Segment into tiers:**
   - **Critical** (QS 1-3): Immediate action
   - **High Priority** (QS 4-5): Fix next
   - **Maintenance** (QS 6-7): Monitor
   - **Protect** (QS 8-10): Don't change

3. **Calculate financial impact:**
   ```
   Potential Savings = 
   (Critical/High Priority Spend) × 
   (Current Avg QS improvement to target QS CPC reduction %)
   ```

### Phase 2: Quick Wins (Week 1-2)

**For Critical QS 1-3 Keywords:**
1. Add keyword to ad headline (if not already)
2. Add all missing extensions
3. Check if landing page relevant (if not, change destination URL)
4. Increase bid to position 1-3 temporarily (boost CTR)

**Expected:** QS 3 → QS 5 within 2 weeks

### Phase 3: Ad Relevance Fix (Week 2-4)

**Goal:** Achieve "Above average" Ad Relevance

1. **Restructure into SKAGs or tight ad groups**
   - Max 10-15 keywords per ad group
   - Keywords should be very similar

2. **Rewrite ads for perfect keyword matching**
   - Keyword in Headline 1
   - Related terms in Headline 2, 3
   - Keyword/theme in description

3. **Use Dynamic Keyword Insertion selectively**

**Expected:** Ad Relevance "Below average" → "Above average"

### Phase 4: Landing Page Optimization (Week 3-6)

**Goal:** Achieve "Above average" Landing Page Experience

**Week 3: Speed optimization**
- Compress images
- Enable caching
- Minimize scripts

**Week 4: Mobile optimization**
- Responsive design
- Touch-friendly elements
- Readable fonts

**Week 5: Content optimization**
- Add keyword to page title/H1
- Write substantive content (500+ words)
- Add trust signals

**Week 6: UX improvements**
- Remove aggressive pop-ups
- Simplify navigation
- Clear CTAs

**Expected:** Landing Page Exp "Below average" → "Above average"

### Phase 5: Expected CTR Improvement (Week 4-8)

**Goal:** Build historical CTR through testing

1. **A/B test ad variations** (3-5 per ad group)
2. **Maintain top positions** (1-3) during this phase
3. **Run for minimum 2 weeks per test**
4. **Keep winners, test new challengers**

**Expected:** Expected CTR "Below average" → "Above average"

### Phase 6: Maintenance (Ongoing)

**Monthly:**
- Review QS for any drops
- Identify new QS 1-3 keywords
- Test new ad copy
- Refresh landing pages

**Quarterly:**
- Full account QS audit
- Major landing page updates
- Ad copy overhaul
- Structure optimization

---

## Advanced Quality Score Strategies

### Branded vs Non-Branded Keywords

**Branded Keywords:**
- Naturally higher QS (8-10 typical)
- Higher CTR (people looking for you)
- Easier to maintain high QS
- **Action:** Protect these aggressively

**Non-Branded Keywords:**
- More challenging QS (5-7 typical)
- Requires more optimization
- **Action:** Focus improvement efforts here

### Match Type Impact on Quality Score

**Quality Score by Match Type:**
| Match Type | Typical QS | Ad Relevance Impact |
|------------|-----------|---------------------|
| Exact Match | Highest (7-9) | Easiest to optimize |
| Phrase Match | Medium (6-8) | Moderate difficulty |
| Broad Match | Lowest (5-7) | Hardest to maintain |

**Strategy:**
- Use exact match for SKAGs
- Use phrase match for themed ad groups
- Avoid broad match unless budget allows extensive negative keyword management

### Dynamic Search Ads (DSA) & Quality Score

**DSA Characteristics:**
- No keyword-level QS
- Campaign-level quality metrics
- Landing page most important factor

**DSA Best Practices:**
- Excellent landing page experience critical
- Use specific page feeds (not whole website)
- Regular negative keyword additions
- Monitor search terms daily

---

## Troubleshooting Low Quality Score

### "I've done everything but QS won't improve"

**Possible Issues:**

1. **Insufficient time passed**
   - QS updates can take 2-4 weeks
   - Need sustained CTR improvement
   - Solution: Wait, maintain changes

2. **Historical performance too negative**
   - Very low past CTR hard to overcome
   - Solution: Create new ad group with same keywords (fresh start)

3. **Keyword fundamentally not relevant**
   - Account theme doesn't support keyword
   - Landing page can't be made relevant
   - Solution: Pause keyword, find alternative

4. **Severe landing page issues**
   - Page genuinely poor quality
   - Excessive ads/pop-ups
   - Solution: Complete page rebuild

5. **Technical issues**
   - Slow hosting
   - Broken mobile experience
   - Solution: Technical audit & fixes

### When to Pause Low QS Keywords

**Pause if:**
- QS 1-2 after 60 days of optimization efforts
- Keyword not relevant to core business
- Can't create relevant landing page
- CPA >5x target even with high conversion rate

**Don't Pause if:**
- Keyword is highly relevant to business
- Drives qualified leads despite high CPC
- Only optimization issue (fixable)
- Recent launch (give 30 days minimum)

---

## Quality Score Impact Calculator

**Estimate savings from QS improvement:**

```
Current State:
- Average CPC: $5.00
- Average QS: 4
- Monthly spend: $10,000

Target State:
- Improved QS: 7

CPC Reduction: ~28.5%
New Average CPC: $3.58
Same traffic spend: $7,150
Monthly Savings: $2,850
Annual Savings: $34,200
```

**Use this to justify investment in QS optimization efforts.**
