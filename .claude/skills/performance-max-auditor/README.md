# Performance Max Auditor - Claude Skill

Comprehensive audit framework for Google Performance Max campaigns that identifies wastage, missed opportunities, and ROI optimization actions.

## Overview

The Performance Max Auditor skill transforms Performance Max campaign data into actionable insights across 7 critical dimensions:

1. **Goal Setup & Conversion Quality** - Conversion tracking validation and value optimization
2. **Asset Group Performance** - Creative performance and distribution analysis
3. **Audience Signals** - Signal strength and expansion assessment
4. **Bidding Strategy** - Bid optimization and learning phase diagnostics
5. **Budget Allocation** - Spend distribution and scaling opportunities
6. **Search Term Insights** - Query relevance and negative keyword mining
7. **Landing Page Experience** - Page performance and conversion barriers

## What You Get

- Overall campaign health score (0-100)
- Top 3 wastage areas with cost impact
- Top 3 growth opportunities with revenue potential
- Prioritized action plan with ROI estimates
- Quick wins (Week 1) + long-term strategy (Month 2+)

## Installation

```bash
# Download and extract
unzip performance-max-auditor.zip

# Copy to Claude skills directory
cp -r performance-max-auditor ~/.config/claude/skills/user/

# Restart Claude
```

## Quick Start

```
Audit this Performance Max campaign for wastage and quick wins
[attach Google Ads export]
```

For comprehensive audit, add context:
- Business type (eCommerce/Lead Gen/App Installs)
- Monthly budget
- Target ROAS or CPA
- Primary KPI

## What to Export from Google Ads

1. Campaign overview metrics (last 30-90 days)
2. Asset group performance
3. Search terms insights
4. Audience signals (optional)
5. Landing pages (optional)

## Example Results

**Health Score**: 68/100 (Fair)
**Wastage Identified**: $8,900/month
- Irrelevant searches: $4,200/mo
- Weak asset groups: $2,800/mo
- Poor landing pages: $1,900/mo

**Quick Wins (Week 1)**
1. Add 67 negative keywords → Save $4,200/mo (1 hour)
2. Pause 2 worst landing pages → Save $1,900/mo (15 min)
3. Fix conversion tracking → Improve attribution (2 hours)

## Integration

Works with:
- `negative-keyword-miner` - Extract negative keywords
- `landing-page-optimizer` - Fix page issues
- `creative-testing-framework` - Test asset variations

## Tips

✅ Include search terms data (reveals biggest wastage)
✅ Provide landing page URLs (10-30% CVR lift potential)
✅ Share business context (margins, LTV, seasonality)
✅ Run quarterly (campaigns evolve significantly)

## Support

Created by Jabberwocky
Questions? Check EXAMPLES.md or references/ folder

---

**MIT License** - Free for personal and commercial use
