# Negative Keyword Miner - Usage Examples

## Example 1: B2B SaaS Company - First Month Optimization

### Context

**Company**: Project management software for enterprises  
**Monthly Budget**: $15,000  
**Industry**: B2B SaaS  
**Campaign Goal**: Free trial signups  
**Current CPA**: $180 (goal: $120)

### User Input

```
I need help finding negative keywords for my project management software.

Here's my situation:
- Running Google Ads for 45 days
- Spending $15K/month
- Getting lots of clicks but low conversions
- Current CPA is $180, want to get to $120

Top search terms with zero conversions:
- "project management jobs" - 234 clicks, $1,234 spent
- "free project management software" - 189 clicks, $945 spent
- "project management definition" - 156 clicks, $678 spent
- "project management certification" - 145 clicks, $723 spent
- "project management template" - 134 clicks, $589 spent
- "project management tools comparison" - 98 clicks, $567 spent

We're a B2B SaaS, not free, and definitely not hiring.
```

### Skill Output (Abbreviated)

```markdown
## Analysis Summary

**Analysis Period**: 45 days  
**Estimated Monthly Waste**: $4,736 (32% of spend)  
**Potential Monthly Savings**: $4,500  
**Recommended Negatives**: 23 keywords

---

## Priority Tier 1: CRITICAL

### Exact Match Negatives

| Negative Keyword | Match Type | Monthly Cost | Est. Savings | Reason |
|------------------|------------|--------------|--------------|--------|
| project management jobs | Exact | $1,234 | $1,172 | Job seekers, zero business intent |
| project management certification | Exact | $723 | $687 | Educational content, not software buyers |
| project management definition | Exact | $678 | $644 | Informational query, wrong funnel stage |
| free project management software | Exact | $945 | $898 | Price sensitive, your product isn't free |

**Tier 1 Total Savings**: $3,401/month

### Broad Match Negatives

| Negative Keyword | Match Type | Monthly Cost | Est. Savings | Reason |
|------------------|------------|--------------|--------------|--------|
| jobs | Broad | ~$1,500 | $1,425 | Blocks all job-related searches |
| free | Broad | ~$1,100 | $1,045 | You don't offer free version |

**Implementation**: Add these TODAY. Risk level: LOW

---

## Pattern Analysis

### Top Cost-Wasting Patterns

1. **Job Seeker Pattern** ($1,500/month waste)
   - "jobs", "careers", "hiring", "salary"
   - Recommendation: Broad match negative "jobs"

2. **Free Seeker Pattern** ($1,100/month waste)
   - "free", "no cost", "free trial" (if you don't offer)
   - Recommendation: Broad match negative "free"

3. **Informational Intent** ($900/month waste)
   - "definition", "what is", "meaning", "guide"
   - Recommendation: Create separate content campaign OR block

---

## Implementation Roadmap

**Day 1**: 
- Add Tier 1 exact match negatives (4 keywords)
- Expected immediate savings: $3,400/month

**Day 3**: 
- Monitor: Check impressions haven't dropped >20%
- Add broad match "jobs" and "free"

**Week 2**: 
- Calculate actual savings
- Expected CPA improvement: $180 → $135
- Add Tier 2 negatives
```

### Results After Implementation

- **Month 1**: CPA dropped to $138 (23% improvement)
- **Cost Savings**: $3,200/month (slightly below forecast due to conservative implementation)
- **Conversion Rate**: Improved from 1.8% to 2.9%
- **Quality Score**: Increased from 6/10 to 8/10 (better relevance)

---

## Example 2: E-commerce Store - Product Category Optimization

### Context

**Company**: Online fitness equipment store  
**Monthly Budget**: $8,000  
**Industry**: E-commerce  
**Campaign**: Yoga mats category  
**Goal**: Direct purchases  

### User Input

```
Help me optimize negative keywords for my yoga mat campaign.

Account info:
- Selling premium yoga mats ($60-$120)
- Not cheap/budget positioning
- Don't offer wholesale

Problem search terms (all zero sales):
- "cheap yoga mats" - 456 clicks, $234
- "yoga mat wholesale" - 234 clicks, $567
- "diy yoga mat" - 123 clicks, $89
- "yoga mats for gyms bulk order" - 89 clicks, $456
- "yoga mat images" - 234 clicks, $45
- "how to clean yoga mat" - 345 clicks, $123

Also getting traffic from wrong colors/sizes we don't carry.
```

### Skill Output (Abbreviated)

```markdown
## Priority Tier 1: CRITICAL

### Price Sensitivity Negatives

| Negative Keyword | Match Type | Est. Savings | Reason |
|------------------|------------|--------------|--------|
| cheap | Broad | $234 | Wrong price positioning, you're premium |
| wholesale | Broad | $567 | B2B intent, you're B2C only |
| bulk order | Phrase | $456 | B2B intent, minimum quantities |

### DIY/Information Negatives

| Negative Keyword | Match Type | Est. Savings | Reason |
|------------------|------------|--------------|--------|
| diy | Broad | $89 | Looking to make, not buy |
| how to clean | Phrase | $123 | Post-purchase support query |
| images | Broad | $45 | Looking for pictures, not products |

**Tier 1 Total Savings**: $1,514/month

## Product Attribute Negatives

Add these campaign-level negatives for attributes you don't carry:

**Colors** (if you don't sell):
- "pink yoga mat" - Exact
- "camo yoga mat" - Exact

**Sizes** (if you don't offer):
- "extra large yoga mat" - Phrase
- "travel size yoga mat" - Phrase

**Materials** (if you don't carry):
- "cork yoga mat" - Exact (if you only sell TPE/rubber)

## Expected Impact

- Monthly savings: $1,514
- CPA improvement: 19%
- Conversion rate: Expected +1.2% lift
```

### Implementation Notes

User implemented:
1. Day 1: All price sensitivity negatives
2. Day 3: DIY and information negatives  
3. Week 2: Product attribute negatives

Result: 23% cost reduction, 2.1% conversion rate improvement

---

## Example 3: Local Service Business - Geographic Targeting

### Context

**Company**: Plumbing service in Los Angeles  
**Monthly Budget**: $3,500  
**Industry**: Local services  
**Service Area**: LA County only (not OC, not Riverside, not Ventura)  
**Problem**: Getting clicks from areas they don't serve

### User Input

```
I'm a plumber in Los Angeles and I'm wasting money on clicks from areas I don't serve.

My service area: Los Angeles County ONLY

Problem searches (all outside my area):
- "plumber in orange county" - $345 wasted
- "san diego plumber" - $234 wasted  
- "riverside emergency plumber" - $178 wasted
- "ventura plumber near me" - $167 wasted
- "santa barbara plumbing service" - $123 wasted

Also getting:
- "plumber salary" - people looking for jobs
- "how to fix toilet" - DIY people

Total wasted: ~$1,200/month out of $3,500 budget (34%!)
```

### Skill Output (Abbreviated)

```markdown
## Geographic Negative Keywords - CRITICAL PRIORITY

### Cities/Counties to Block (Outside Service Area)

**Add as ACCOUNT-LEVEL negatives**:

| Negative Keyword | Match Type | Monthly Waste | Reason |
|------------------|------------|---------------|--------|
| orange county | Phrase | $345 | Outside service area |
| san diego | Phrase | $234 | Outside service area |
| riverside | Phrase | $178 | Outside service area |
| ventura | Phrase | $167 | Outside service area |
| santa barbara | Phrase | $123 | Outside service area |

**Additional Cities to Block**:
- "long beach" (if not serving)
- "pasadena" (if not serving)
- "glendale" (if not serving)

Match Type: Phrase (not exact, to catch variations like "plumber in orange county", "orange county plumber")

**Total Geographic Savings**: $1,047/month

## DIY Intent Negatives

| Negative Keyword | Match Type | Monthly Waste | Reason |
|------------------|------------|---------------|--------|
| how to fix | Phrase | $156 | DIY intent |
| diy | Broad | $89 | DIY intent |
| salary | Broad | $78 | Job seeker |

**Total DIY Savings**: $323/month

## TOTAL POTENTIAL SAVINGS: $1,370/month (39% of budget!)

## Implementation Strategy for Local Business

**Week 1**: Add all geographic negatives
- Risk: LOW (you definitely don't serve these areas)
- Expected: 30% cost reduction immediately

**Week 2**: Add DIY and job negatives  
- Risk: LOW
- Expected: Additional 9% savings

**Result**: Keep 100% of budget focused on LA County service area

## Radius Targeting Recommendation

Consider also:
- Setting up radius targeting (20-mile radius from LA)
- Will automatically exclude most far locations
- Combined with negatives = maximum efficiency
```

### Results

- **Immediate Impact**: 37% cost reduction in Week 1
- **Lead Quality**: Improved dramatically (all leads now in service area)
- **Conversion to Booked Jobs**: Up 45% (leads are serviceable)
- **Overall ROI**: Budget went from 34% waste to <5% waste

---

## Example 4: Agency Managing Multiple Clients

### Context

**Agency**: Managing 15 PPC accounts  
**Use Case**: Build shared negative keyword list  
**Goal**: Apply universal negatives across all B2B clients  

### User Input

```
I'm an agency managing 15 B2B SaaS clients. 

I want to create a shared negative keyword list that applies to ALL accounts to prevent common waste.

Common patterns I'm seeing across accounts:
- Job searches ("jobs", "careers", "salary")
- Free seekers (all clients are paid products)
- Academic/student searches
- Wrong product types (we do software, getting hardware searches)

Can you create a universal B2B SaaS negative keyword list I can apply to all 15 accounts?
```

### Skill Output (Abbreviated)

```markdown
## Universal B2B SaaS Negative Keyword List

### Account-Level Negatives (Safe for ALL B2B SaaS)

#### Job Seeker Pattern
- jobs (Broad)
- careers (Broad)
- career (Broad)
- hiring (Broad)
- salary (Broad)
- employment (Broad)

#### Free Seeker Pattern
- free (Broad) *If none offer freemium
- free trial (Phrase) *If none offer trials
- free version (Phrase)
- free download (Phrase)
- cracked (Broad)
- pirated (Broad)

#### Academic Pattern
- thesis (Broad)
- dissertation (Broad)
- homework (Broad)
- assignment (Broad)
- student project (Phrase)
- school project (Phrase)

#### Information Seeker Pattern
- definition (Broad)
- meaning (Broad)
- what is (Phrase)
- wikipedia (Broad)

#### DIY Pattern
- diy (Broad)
- how to build (Phrase)
- open source (Phrase)
- github (Broad) *Unless targeting developers

#### Wrong Product Type
- hardware (Broad) *For pure software companies
- physical (Broad)
- on premise (Phrase) *For cloud-only

#### Post-Purchase Searches
- login (Broad)
- sign in (Phrase)
- support (Broad)
- customer service (Phrase)
- help desk (Phrase)

### Implementation for Agency

**Create Shared List**: "Universal B2B SaaS Negatives"

**Apply to**:
- All B2B SaaS accounts
- Account-level (not campaign-level)
- Review quarterly for outdated terms

**Expected Impact**:
- 8-15% cost reduction across portfolio
- Better lead quality
- Higher overall ROAS
- Time saved: 30+ hours/month (2 hours per account)

### Client-Specific Additions

Then customize per client:
- Geographic negatives (if local)
- Competitor names (varies by client)
- Product-specific negatives
- Industry-specific patterns

### Monitoring Dashboard

Track across all 15 accounts:
- Total savings from shared list
- Impact on CPL
- Any unintended blocking
- New patterns to add quarterly
```

---

## Example 5: Emergency Spend Reduction

### Context

**Situation**: Went 40% over budget, need immediate cuts  
**Account**: SaaS marketing tool  
**Problem**: Broad match keywords out of control  

### User Input

```
URGENT: I'm 40% over budget this month and need to cut waste IMMEDIATELY.

Current spend: $21,000 (budget was $15,000)
Days left in month: 8

I can't pause campaigns entirely (need the leads), but I need to cut ~$6,000 in waste in the next 8 days.

Biggest wasters from search terms:
- "marketing jobs" - $2,345 (zero conversions)
- "free marketing tools" - $1,876 (zero conversions)
- "marketing definition" - $1,234 (zero conversions)
- Various "[competitor] vs [us]" terms - $1,500 combined
- "marketing memes" / "marketing jokes" - $456

What negatives can I add TODAY to stop the bleeding?
```

### Skill Output (Emergency Mode)

```markdown
## EMERGENCY NEGATIVE KEYWORDS - Add in Next 2 Hours

### Critical Block List (Immediate Implementation)

**Add RIGHT NOW** (in order of urgency):

1. **jobs** (Broad Match Negative)
   - Current waste: $2,345/month = $78/day
   - Will save ~$624 over next 8 days
   - Risk: ZERO (you're not hiring via PPC)

2. **free** (Broad Match Negative)  
   - Current waste: $1,876/month = $63/day
   - Will save ~$504 over next 8 days
   - Risk: LOW (verify you don't have "free trial" campaign)

3. **definition** (Broad Match Negative)
   - Current waste: $1,234/month = $41/day
   - Will save ~$328 over next 8 days
   - Risk: ZERO (informational intent)

4. Add competitor names as PHRASE match negatives:
   - "[competitor1]" (Phrase)
   - "[competitor2]" (Phrase)
   - Saves: ~$188 over 8 days

5. **meme, memes, joke, jokes, funny** (Broad Match)
   - Current waste: $456/month = $15/day
   - Saves: ~$120 over 8 days
   - Risk: ZERO (not buying intent)

**TOTAL 8-DAY SAVINGS: ~$1,764**

## Hour 2-4: Review and Add These

6. **what is, how to, guide, tutorial** (Phrase Match)
   - Estimated additional savings: $400 over 8 days

7. **review, reviews, comparison** (Phrase Match)
   - CAUTION: Review if these sometimes convert
   - If not: Savings of ~$300 over 8 days

## Day 2: If Still Over Budget

8. Consider pausing lowest-performing ad groups entirely
9. Reduce bids on high-CPC, low-conversion terms by 40%
10. Implement more aggressive negative keywords from Tier 2

## Expected Impact

**Immediate** (Hours 1-24):
- Spend reduction: $200-250/day
- Should prevent $1,600-2,000 additional overspend

**Days 2-8**:
- Cumulative savings: $1,760+
- Gets you closer to budget
- Preserves lead flow (not pausing campaigns)

## Post-Emergency Actions

After month ends:
- Run full 30-day negative keyword analysis
- Identify why broad match got out of control
- Implement long-term negative keyword strategy
- Set up budget alerts for future
```

### Results

- Added all Tier 1 negatives in 1 hour
- Daily spend dropped from $700 → $480 within 24 hours
- Ended month at $17,800 (still over, but much better than $21K+)
- Lead volume stayed strong (only removed waste)
- Lesson learned: Set up negative keywords BEFORE launching broad match!

---

## Example 6: Quality Score Improvement Focus

### Context

**Goal**: Improve Quality Scores to reduce CPC  
**Current State**: Average QS of 5/10, CPCs are high  
**Strategy**: Use negative keywords to improve relevance  

### User Input

```
My Quality Scores are terrible (average 5/10) and my CPCs are through the roof.

I know negative keywords can help improve relevance and QS.

My situation:
- Running campaigns for "email marketing software"
- Getting lots of clicks from:
  - Email-related but not relevant: "email templates", "email signature"
  - Wrong intent: "what is email marketing"
  - Wrong audience: "email marketing for students"

Current metrics:
- CTR: 2.1% (low)
- Conversion rate: 1.3%
- Avg QS: 5/10
- Avg CPC: $8.50

I want to get QS to 7+ and cut CPC by 25%.
```

### Skill Output (QS Focus)

```markdown
## Quality Score Improvement via Negative Keywords

### Strategy: Hyper-Relevant Traffic Only

Goal: Increase CTR → Improve QS → Lower CPC

### Phase 1: Remove Obviously Irrelevant (Week 1)

Block anything not strictly about "email marketing SOFTWARE":

| Negative Keyword | Match Type | Why This Helps QS |
|------------------|------------|-------------------|
| email templates | Phrase | Not software, different product |
| email signature | Phrase | Different product category |
| email design | Phrase | Not software search |
| gmail | Broad | Wrong platform/tool |

**Expected Impact**: CTR improves from 2.1% → 2.8%

### Phase 2: Remove Wrong Intent (Week 2)

Block informational searches:

| Negative Keyword | Match Type | Why This Helps QS |
|------------------|------------|-------------------|
| what is | Phrase | Informational, low intent |
| how to | Phrase | Educational, wrong funnel |
| guide | Broad | Tutorial seekers |
| tutorial | Broad | Learning, not buying |

**Expected Impact**: CTR improves from 2.8% → 3.5%

### Phase 3: Remove Wrong Audience (Week 3)

Block audiences who won't convert:

| Negative Keyword | Match Type | Why This Helps QS |
|------------------|------------|-------------------|
| students | Broad | Not target B2B audience |
| school | Broad | Not target B2B audience |
| free | Broad | Price sensitive, not your market |

**Expected Impact**: CTR improves from 3.5% → 4.2%

## Expected Quality Score Journey

**Week 0** (Before):
- CTR: 2.1%
- QS: 5/10
- CPC: $8.50

**Week 1** (Phase 1 negatives):
- CTR: 2.8% (+33%)
- QS: 6/10
- CPC: $7.80 (-8%)

**Week 2** (Phase 2 negatives):
- CTR: 3.5% (+67%)
- QS: 7/10
- CPC: $6.80 (-20%)

**Week 3** (Phase 3 negatives):
- CTR: 4.2% (+100%)
- QS: 8/10
- CPC: $6.30 (-26%)

**Total Impact**:
- CTR doubled
- QS improved by 3 points
- CPC reduced by 26% (exceeded goal!)

## The QS Virtuous Cycle

Better Negatives → Higher CTR → Higher QS → Lower CPC → Better Ad Position → Even Higher CTR → Even Higher QS

This compounds over time.

## Monitoring Focus

Track these weekly:
- CTR trend (should increase)
- QS trend (should increase) 
- CPC trend (should decrease)
- Impression share (should stay stable or increase)
```

---

## Key Takeaways from Examples

1. **Start Conservative**: Exact match first, then phrase, then broad
2. **Monitor Closely**: First 3-7 days are critical
3. **Expect 10-25% Savings**: Most accounts find this range
4. **Context Matters**: B2B vs B2C, local vs national, etc.
5. **Patterns > Individual Terms**: Think in themes, not just keywords
6. **Quality Score Boost**: Side benefit of better relevance
7. **Review Monthly**: Markets change, negatives need updates

---

Want to see YOUR account analyzed? Export your search terms report and let's find your wasted spend.
