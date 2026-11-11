# Negative Keyword Miner

**Version**: 1.0.0  
**Author**: Jabberwocky  
**Category**: PPC Optimization / Paid Search

## Overview

Extract high-impact negative keywords from search term reports to eliminate wasted ad spend. This skill analyzes search query patterns, identifies cost-wasting terms, and provides prioritized implementation recommendations with estimated savings.

## What This Skill Does

- **Pattern Recognition**: Identifies recurring themes in non-converting searches
- **Cost Analysis**: Calculates monthly waste and prioritizes by savings potential
- **Match Type Intelligence**: Recommends exact, phrase, or broad match negatives
- **Risk Assessment**: Flags high-risk exclusions to prevent over-blocking
- **Implementation Roadmap**: Provides step-by-step rollout strategy

## Key Features

✅ **Automated Pattern Detection** - Finds waste patterns across thousands of search terms  
✅ **Priority Tiers** - Ranks negatives from Critical to Low priority  
✅ **Savings Forecasting** - Estimates monthly cost savings per negative  
✅ **Match Type Recommendations** - Suggests optimal match type for each exclusion  
✅ **Risk Mitigation** - Identifies potential over-blocking issues  
✅ **Implementation Guide** - Platform-specific upload instructions  

## Time Savings

**Manual Analysis**: 4-6 hours per account per month  
**With This Skill**: 15-20 minutes  
**Time Saved**: ~5 hours per month  

## Typical ROI

**Small Accounts** (<$5K/month): 15-25% cost reduction  
**Medium Accounts** ($5K-50K/month): 10-20% cost reduction  
**Large Accounts** (>$50K/month): 5-15% cost reduction  

## Who Should Use This

- **PPC Managers**: Running Google Ads, Microsoft Ads, or other paid search
- **Marketing Agencies**: Managing multiple client accounts
- **Solo Founders**: Optimizing ad spend without an agency
- **E-commerce Brands**: Reducing wasted product ad spend
- **SaaS Companies**: Improving lead quality and CAC

## Prerequisites

- Access to search terms report from your ad platform
- 30+ days of search term data (minimum 14 days)
- CSV export with columns: Search Term, Impressions, Clicks, Cost, Conversions
- Basic understanding of negative keywords and match types

## Installation

1. Download the `negative-keyword-miner.skill` file
2. Copy to your Claude Skills directory: `~/.config/claude/skills/`
3. Restart Claude or refresh skills
4. Verify installation: Type "negative keyword miner" in Claude

## Usage

### Quick Start

```
I need help finding negative keywords.

Here's my search terms report data:
[Paste CSV data or describe your ad account]

Account details:
- Monthly budget: $[amount]
- Industry: [your industry]
- Business type: [B2B/B2C/Local/E-commerce]
```

### Recommended Workflow

**Step 1**: Export search terms report (30+ days)  
**Step 2**: Provide to skill with context about your business  
**Step 3**: Review Tier 1 recommendations (critical negatives)  
**Step 4**: Implement Tier 1 negatives first  
**Step 5**: Monitor for 3-7 days  
**Step 6**: Implement Tier 2 negatives  
**Step 7**: Re-run analysis monthly  

### Analysis Types

#### Quick Scan (5-10 minutes)
Best for: Immediate wins, obvious waste
```
Run a quick scan for negative keywords. Focus on zero-conversion terms with spend over $50.
```

#### Deep Analysis (20-30 minutes)
Best for: Comprehensive optimization, pattern discovery
```
Perform a deep analysis of my search terms. I want pattern-based recommendations with match type strategies.
```

#### Competitive Comparison (30-40 minutes)
Best for: Benchmarking, identifying gaps
```
Analyze my negative keyword strategy compared to industry benchmarks. Where am I missing opportunities?
```

## Input Format

### CSV Structure (Preferred)

```csv
Search Term,Impressions,Clicks,Cost,Conversions,Conv. Rate,CPA
"project management software",1250,87,$543.21,0,0%,--
"free project management",890,45,$123.45,0,0%,--
"project management jobs",2340,134,$789.23,0,0%,--
```

### Alternative Input

If you don't have a CSV, you can describe:
- Top spending search terms with zero conversions
- Common patterns you've noticed
- Your industry and business model
- Monthly ad spend level

## Output Format

The skill provides:

1. **Executive Summary**
   - Total waste identified
   - Estimated monthly savings
   - Number of recommended negatives

2. **Priority Tiers** (Critical → Low)
   - Negative keyword
   - Match type recommendation
   - Monthly cost impact
   - Reason for exclusion
   - Implementation level (account vs campaign)

3. **Pattern Analysis**
   - Top cost-wasting patterns
   - Example terms
   - Recommended negative keyword strategy

4. **Implementation Roadmap**
   - Week-by-week rollout plan
   - Risk mitigation strategy
   - Monitoring guidelines

## Best Practices

### Do's ✅

- Start with **exact match** negatives (lowest risk)
- Implement **Tier 1 first**, monitor, then add Tier 2
- **Wait 3-7 days** between major negative keyword additions
- **Cross-reference** with your target keyword list
- **Review monthly** and remove outdated negatives
- **Document** what you add and when

### Don'ts ❌

- Don't add all negatives at once (can't track impact)
- Don't use broad match negatives without careful review
- Don't add negatives with insufficient data (<30 days)
- Don't forget to check assisted conversions
- Don't ignore impression drops >20%
- Don't set and forget (markets change)

## Common Use Cases

### Use Case 1: New Account Setup
**Scenario**: Just launched new campaigns, getting irrelevant traffic  
**Approach**: Quick scan for obvious waste, add critical negatives only  
**Expected Impact**: 20-30% immediate cost reduction  

### Use Case 2: Monthly Optimization
**Scenario**: Mature account, routine maintenance  
**Approach**: Deep analysis, pattern-based strategy  
**Expected Impact**: 5-10% ongoing cost reduction  

### Use Case 3: Budget Crisis
**Scenario**: Overspending, need immediate cuts  
**Approach**: Focus on highest-cost zero converters  
**Expected Impact**: 15-25% emergency cost reduction  

### Use Case 4: Quality Score Improvement
**Scenario**: Low Quality Scores, high CPCs  
**Approach**: Aggressive negative keywords to improve relevance  
**Expected Impact**: +1-3 Quality Score points, 15-30% CPC reduction  

## Examples

See `EXAMPLES.md` for detailed scenarios including:
- B2B SaaS account optimization
- E-commerce store negative keywords
- Local service business geographic exclusions
- Agency managing multiple clients

## Troubleshooting

### Issue: Impressions dropped >30%
**Cause**: Over-exclusion, broad match negatives too aggressive  
**Solution**: Remove last batch of negatives, restart with exact match only

### Issue: No cost savings seen
**Cause**: Insufficient data, or negative keywords not capturing patterns  
**Solution**: Re-run analysis with 60+ days of data, look for different patterns

### Issue: Conversions dropped
**Cause**: Accidentally blocked converting terms  
**Solution**: Review recent negatives, check for conflicts with target keywords

### Issue: Analysis finds no negative keywords
**Cause**: Account already well-optimized, or insufficient data  
**Solution**: Celebrate! Check back monthly for new opportunities

## Advanced Features

### Pattern Recognition Engine
Automatically identifies:
- Job seeker queries
- Free/DIY intent
- Academic/student searches
- Wrong geographic locations
- Competitor research terms
- Information-seeking queries

### Match Type Intelligence
Recommends optimal match type based on:
- Specificity of the term
- Risk of over-blocking
- Pattern vs individual keyword
- Account maturity

### Cost Prioritization
Ranks negatives by:
- Current monthly waste
- Implementation risk
- Estimated savings confidence
- Strategic importance

## Integration with Other Skills

Works well with:
- **Campaign Strategy Planning**: Inform campaign structure with negative keyword insights
- **Data Anomaly Detective**: Identify sudden changes in wasted spend
- **Attribution Modeling Advisor**: Understand multi-touch negative keyword impact

## Maintenance

### Monthly Tasks
- Export new search terms report
- Run skill analysis
- Implement new negatives (Tier 1 only)
- Review performance of last month's negatives

### Quarterly Tasks
- Full negative keyword list audit
- Remove outdated negatives
- Strategic review of patterns
- Benchmark against previous quarters

## Support & Feedback

**Issues or questions?**  
- Comment on skill distribution post
- Tag @jabberwocky in Claude community
- Check skill documentation updates

**Feature requests?**  
Open to suggestions for:
- New pattern detection algorithms
- Additional platform support
- Custom reporting formats

## Version History

**v1.0.0** (January 2025)
- Initial release
- Pattern recognition for common waste patterns
- 4-tier priority system
- Match type recommendations
- Implementation roadmap generation

## License

Free for personal and commercial use.  
Attribution appreciated but not required.

## Credits

Created by Jabberwocky as part of the Claude Skills library for marketing automation.

---

**Ready to eliminate wasted ad spend?**

Export your search terms report and let's find those money-wasting keywords.
