# Negative Keyword Best Practices

## Strategic Principles

### 1. Start Conservative, Scale Aggressively

**Why**: Over-excluding is worse than under-excluding initially

**Approach**:
- Week 1: Add only exact match negatives with 100% certainty
- Week 2: Add phrase match negatives after monitoring Week 1 impact
- Week 3+: Add carefully selected broad match negatives
- Always prefer exact > phrase > broad when in doubt

### 2. Data Before Decisions

**Minimum Data Thresholds**:
- 100+ impressions: Required to identify patterns
- 50+ clicks: Needed for CTR analysis
- 10+ conversions: Ideal for CPA analysis (if available)
- 30+ days: Minimum time period for seasonal patterns

**Exception**: Zero-conversion terms with $100+ spend can be negatives immediately

### 3. Think in Patterns, Not Just Keywords

**Good Pattern Thinking**:
- "Every term with 'free' is converting at 0%" → Broad match negative "free"
- "All job-related searches waste money" → Multiple job-related negatives
- "Competitor research queries don't convert" → Pattern-based exclusions

**Bad Individual Thinking**:
- "This one weird search term showed up" → Not enough for negative keyword
- "Got 3 clicks, no conversion" → Need more data
- "I don't like this keyword" → Feelings ≠ data

### 4. Balance Reach vs Efficiency

**The Tradeoff**:
- More negative keywords = Higher efficiency, lower reach
- Fewer negative keywords = Lower efficiency, higher reach

**Optimal Balance**:
- Early stage accounts: Be aggressive with negatives (efficiency matters more)
- Mature accounts: Be cautious (may already be optimized)
- Limited budgets: Focus on high-waste negatives only
- Large budgets: Can afford exploratory traffic

### 5. Match Type Hierarchy

**Use this decision tree**:

Is it a single exact search term that's definitely bad?
→ YES: Exact match negative
→ NO: Continue...

Is it a phrase that always signals bad intent regardless of what comes before/after?
→ YES: Phrase match negative
→ NO: Continue...

Is it a single word that's bad in ANY query?
→ YES: Broad match negative (but monitor closely!)
→ NO: Don't add as negative yet

## Industry-Specific Strategies

### B2B SaaS

**Common Negative Patterns**:
- "free", "open source", "free trial" (if you don't offer these)
- "jobs", "career", "salary", "hiring"
- "reviews", "comparison" (unless in research campaign)
- Student-related: "project", "assignment", "thesis"

**Watch Out For**:
- "demo" and "trial" might be high-intent if you offer these
- Some "review" terms convert if your reviews are strong

### E-commerce

**Common Negative Patterns**:
- "wholesale", "bulk order", "trade" (unless you serve B2B)
- "diy", "homemade", "how to make"
- "images", "clipart", "wallpaper" (for product images)
- Wrong colors/sizes: "plus size" for standard sizing brands

**Watch Out For**:
- "cheap" and "affordable" might convert for price-sensitive products
- "reviews" can be high-intent for e-commerce

### Local Services

**Common Negative Patterns**:
- Wrong locations: Cities/states you don't serve
- "jobs", "careers" (unless hiring)
- "diy", "how to" (people wanting to do it themselves)
- "salary", "cost" (if you don't show pricing upfront)

**Watch Out For**:
- "near me" is high-intent, don't block
- "cheap" might work for budget service positioning

### Legal Services

**Common Negative Patterns**:
- "free consultation" (if you don't offer this)
- "pro bono", "volunteer"
- "salary", "jobs"
- "jokes", "meme", "funny" (for serious practices)

**Watch Out For**:
- "question" and "how to" might be high-intent educational searches

## Common Mistakes to Avoid

### Mistake 1: Adding Negatives Too Quickly

**Problem**: Insufficient data leads to wrong exclusions

**Example**: 
- Keyword "enterprise software demo" gets 5 clicks, no conversions
- Marketer adds "demo" as broad match negative
- Now blocks "request demo", "schedule demo", "demo video" (all converters!)

**Solution**: 
- Require minimum 30 days + 50 clicks before negative keyword decision
- Use exact or phrase match, not broad, for specific terms

### Mistake 2: Ignoring Assisted Conversions

**Problem**: Negative keywords that assist later conversions

**Example**:
- "software comparison" has 0% direct conversion rate
- Gets added as negative keyword
- Later analysis shows it has 35% assisted conversion rate!

**Solution**: 
- Check assisted conversions report before excluding research terms
- Consider adding to separate research campaign with lower bids instead

### Mistake 3: Over-Using Broad Match Negatives

**Problem**: Unintended blocking of good traffic

**Example**:
- Broad match negative "free" added
- Now blocks "free shipping", "free returns", "risk-free trial" (all legitimate)

**Solution**: 
- Use broad match negatives only for universally bad terms
- Most negatives should be exact or phrase match

### Mistake 4: Not Reviewing Existing Negatives

**Problem**: Outdated negative keywords block current opportunities

**Example**:
- 2 years ago: Added "mobile app" as negative (didn't have one)
- Now: Launched mobile app, negative keyword still active
- Result: Missing all mobile app searches!

**Solution**: 
- Quarterly review of all negative keyword lists
- Remove negatives that are no longer relevant

### Mistake 5: Identical Negatives at Multiple Levels

**Problem**: Redundancy and confusion

**Example**:
- "jobs" added as:
  - Account-level negative
  - Campaign-level negative (3 campaigns)
  - Ad group-level negative (12 ad groups)

**Solution**: 
- Add universal negatives at account level ONLY
- Use campaign/ad group negatives only for specific exclusions

### Mistake 6: Conflicting Negatives and Targets

**Problem**: Negative keywords blocking your own target keywords

**Example**:
- Target keyword: "best project management software"
- Negative keyword: "software" (broad match)
- Result: Your own target keyword gets blocked!

**Solution**: 
- Cross-reference negative list with target keyword list
- Use KeyWord Conflict Checker tool before implementing

## Advanced Strategies

### Strategy 1: Negative Keyword Sculpting

**Concept**: Use negatives to force traffic to the right campaigns

**Example**:
- Campaign A (Brand): Target "YourBrand"
- Campaign B (Competitor): Target "CompetitorBrand"
- Add negative "CompetitorBrand" to Campaign A
- Add negative "YourBrand" to Campaign B
- Result: Clean traffic separation, better Quality Scores

### Strategy 2: Geographic Negative Keywords

**For Local Businesses**:
- Add all cities/states outside service area as negatives
- Use exact match for city names (avoid blocking "new york style pizza" if in California)

**Example Structure**:
```
Campaign: Los Angeles Plumber
Negatives: 
- "san francisco" (phrase)
- "san diego" (phrase)  
- "sacramento" (phrase)
[All other major CA cities]
```

### Strategy 3: Life Cycle Stage Negative Keywords

**Separate campaigns by buyer stage, exclude wrong stages**:

Top-of-Funnel (Research) Campaign:
- Target: "what is [product category]", "how does [product] work"
- Negatives: "buy", "price", "best", "vs" (people actively comparing)

Middle-of-Funnel (Consideration) Campaign:
- Target: "[brand] vs [competitor]", "best [product]"
- Negatives: "how to", "what is", "definition" (too early stage)

Bottom-of-Funnel (Purchase) Campaign:
- Target: "buy [product]", "[product] price", "discount"
- Negatives: "how to", "vs", "review" (comparison shoppers)

### Strategy 4: Quality Score Improvement via Negatives

**Concept**: Remove irrelevant traffic to boost Quality Score

**Process**:
1. Identify ad groups with Quality Score <7
2. Review search terms for those ad groups
3. Aggressively add negatives for any slightly irrelevant terms
4. Tighten match types
5. Quality Score improves due to better CTR
6. CPC decreases automatically

**Expected Results**:
- Quality Score improvement: +1 to +3 points
- CPC reduction: 15-30%
- Better ad positions at lower cost

### Strategy 5: Seasonal Negative Keyword Adjustments

**Concept**: Negatives that are only bad during certain seasons

**Example (Tax Prep Software)**:
- January-April: "jobs" converts well (tax season hiring)
- May-December: "jobs" waste (off-season)

**Solution**:
- Create seasonal negative keyword schedules
- Add/remove via scripts or manual calendar reminders

## Monitoring & Maintenance

### Daily Monitoring (First Week Post-Implementation)

**Check these metrics**:
- Total impressions (should not drop >20%)
- Conversion volume (should maintain or improve)
- Average position (should improve slightly)
- Cost per conversion (should decrease)

**Alert Thresholds**:
- 🚨 Impressions drop >30%: Investigate immediately
- ⚠️ Conversions drop >15%: Review negative keywords added
- ✅ CPC drops >10% with stable conversions: Success!

### Weekly Monitoring (Weeks 2-4)

**Review**:
- Search Terms Report: Any new waste patterns?
- Negative keyword performance: Calculate actual savings
- Quality Score changes: Did relevance improve?

### Monthly Maintenance

**Tasks**:
1. **New Negative Keyword Analysis**: Run skill on last 30 days
2. **Negative List Audit**: Remove outdated negatives
3. **Cross-Campaign Check**: Any negatives needed in other campaigns?
4. **Competitor Check**: New competitor terms to exclude?
5. **Performance Documentation**: Track cumulative savings

### Quarterly Deep-Dive

**Strategic Review**:
- Are negative keywords too restrictive now?
- Has business strategy changed (new products, services, locations)?
- Review assisted conversions: Are we blocking early-stage traffic?
- Competitive landscape changes: New competitors to add as negatives?

## Reporting Framework

### Executive Summary Template

**Negative Keyword Optimization Report**  
*Period: [Month/Quarter]*

**Cost Savings**: $[amount] saved this period  
**Efficiency Improvement**: [X]% decrease in wasted spend  
**Conversion Rate Impact**: +[X]% improvement  
**New Negatives Added**: [number] keywords  

**Top 3 Wins**:
1. [Pattern eliminated]: $[amount] saved
2. [Pattern eliminated]: $[amount] saved
3. [Pattern eliminated]: $[amount] saved

**Next Month Focus**:
- [Area to analyze]
- [New negative keyword opportunity]

### Detailed Metrics to Track

| Metric | Before Negatives | After Negatives | Change | Goal |
|--------|------------------|-----------------|--------|------|
| Total Spend | $[amount] | $[amount] | [+/-%] | Maintain |
| Wasted Spend | $[amount] | $[amount] | [-X%] | -50% |
| Conversions | [number] | [number] | [+/-%] | +10% |
| Cost per Conv | $[amount] | $[amount] | [-X%] | -25% |
| Avg Quality Score | [score] | [score] | [+/-] | +1-2 points |

## Tools & Resources

### Recommended Tools

1. **Google Ads Editor**: Bulk negative keyword management
2. **Search Term Analysis Scripts**: Automated pattern detection
3. **Negative Keyword Conflict Checker**: Prevents blocking own keywords
4. **Shared Negative Lists**: Manage negatives across accounts

### Useful Formulas

**Wasted Spend**:
```
Wasted Spend = (Clicks × Avg CPC) where Conversions = 0
```

**Negative Keyword Priority Score**:
```
Priority = (Monthly Cost × Conversion Rate Deficit) / Implementation Risk
```

**Expected Savings**:
```
Monthly Savings = Current Monthly Cost × 0.95 (95% confidence)
```

**ROI of Negative Keyword Optimization**:
```
ROI = (Monthly Savings × 12) / Time Invested
```

## Skill-Specific Best Practices

### Working with This Skill

**Before Running**:
- Export complete search terms report (30+ days)
- Include all columns: impressions, clicks, cost, conversions
- Note any recent account changes (new campaigns, bid changes)

**During Analysis**:
- Provide context about business (B2B vs B2C, products, goals)
- Mention any known issues or concerns
- Flag any terms you want the skill to specifically evaluate

**After Analysis**:
- Review all Tier 1 negatives before implementing (5-min sanity check)
- Start with exact match negatives only
- Wait 3-7 days before adding phrase/broad negatives
- Keep the analysis document for future reference

**Common User Errors**:
- Uploading partial data (missing columns) → Leads to incorrect analysis
- Implementing all tiers at once → Can't track what caused impact
- Not monitoring after implementation → Miss issues or opportunities
- Forgetting to re-run monthly → New waste patterns emerge

## Success Stories & Benchmarks

### Typical Results by Account Size

**Small Accounts (<$5K/month)**:
- Average savings: 15-25% of spend
- Time to positive ROI: 7-14 days
- Recommended review frequency: Monthly

**Medium Accounts ($5K-$50K/month)**:
- Average savings: 10-20% of spend
- Time to positive ROI: 3-7 days
- Recommended review frequency: Weekly

**Large Accounts (>$50K/month)**:
- Average savings: 5-15% of spend
- Time to positive ROI: 1-3 days
- Recommended review frequency: Daily monitoring, weekly deep-dive

### Industry Benchmarks

| Industry | Avg % Wasted Spend | Expected Savings After Negatives |
|----------|-------------------|----------------------------------|
| B2B SaaS | 20-30% | 70% reduction in waste |
| E-commerce | 15-25% | 60% reduction in waste |
| Legal Services | 25-35% | 75% reduction in waste |
| Local Services | 20-30% | 65% reduction in waste |
| Healthcare | 15-20% | 55% reduction in waste |

## Frequently Asked Questions

**Q: How often should I run negative keyword analysis?**  
A: Monthly for most accounts, weekly for high-spend accounts (>$50K/month)

**Q: Will negative keywords hurt my impression share?**  
A: Yes, slightly, but that's the point - you're removing bad impressions that waste money

**Q: Should I add competitor brands as negatives?**  
A: Usually yes for your main campaigns, but consider a separate competitor campaign

**Q: Can I add too many negative keywords?**  
A: Yes - if your impressions drop >30% you've over-excluded

**Q: What if I accidentally block good terms?**  
A: Easy fix - remove the negative keyword, performance resumes within 24 hours

**Q: Do negative keywords affect my Quality Score?**  
A: Indirectly yes - by improving CTR and relevance, your Quality Score increases

**Q: Should I tell my boss how much we were wasting before?**  
A: Focus on the improvement and savings, not past waste 😉

---

*Remember: Negative keywords are about efficiency, not restriction. The goal is to maximize ROI, not minimize spend.*
