# Search Intent Classification Framework

Comprehensive system for categorizing search queries by intent, funnel stage, and optimal response strategy.

## The Four Intent Categories

### 1. Navigational Intent

**Definition**: User wants to reach a specific website or page

**Signals:**
- Brand name + product/service
- Brand name + "login", "account", "support"
- Specific URL fragments
- "Official", "website", "site"

**Examples:**
```
nike running shoes
amazon prime login
spotify customer service
apple store near me
```

**Funnel Stage**: Bottom (if your brand) / N/A (if competitor)

**Recommended Actions:**
| Scenario | Action |
|----------|--------|
| Your brand | High bids, protect position #1 |
| Competitor | Evaluate conquest ROI, often exclude |
| Brand + support | Consider excluding (existing customers) |
| Brand + product | Strong bid, exact landing page |

**Landing Page**: Direct match to query intent
- Brand searches → Homepage or brand landing page
- Brand + product → Specific product page
- Brand + category → Category page

### 2. Transactional Intent

**Definition**: User ready to take action (buy, sign up, download)

**Signals:**
- "Buy", "purchase", "order"
- "Price", "pricing", "cost", "quote"
- "Subscribe", "sign up", "register"
- "Download", "get", "try"
- Product + specification (color, size, model)
- "Near me", "open now" (local)
- "Discount", "deal", "coupon" (price-sensitive buyer)

**Examples:**
```
buy nike air max 90 black size 10
crm software pricing
sign up for gym membership
download adobe acrobat
pizza delivery near me open now
```

**Funnel Stage**: Bottom

**Recommended Actions:**
- **Bid Strategy**: Highest bids, maximum visibility
- **Ad Copy**: Strong CTA, price/offer when available
- **Landing Page**: Direct to conversion page (product, pricing, signup)
- **Keyword Strategy**: Add as exact match, isolate in dedicated campaign

**Conversion Expectations:**
- CVR: 2-5x average
- ROAS: Often highest
- Priority: Scale aggressively

### 3. Commercial Investigation Intent

**Definition**: User researching before purchase decision

**Signals:**
- "Best", "top", "leading"
- "Review", "reviews", "rated"
- "Compare", "comparison", "vs"
- "Alternative", "alternatives to"
- Product + "for [use case]"
- "[Category] for [persona]"

**Examples:**
```
best crm for small business
iphone vs samsung review
mailchimp alternatives
project management software comparison
running shoes for flat feet
```

**Funnel Stage**: Middle

**Recommended Actions:**
- **Bid Strategy**: Moderate bids (lower than transactional)
- **Ad Copy**: Value propositions, differentiators, social proof
- **Landing Page**: Comparison pages, review aggregation, use-case specific pages
- **Content Strategy**: Create content addressing these queries

**Conversion Expectations:**
- CVR: 50-80% of average
- Value: Often higher intent leads
- Strategy: Nurture to transaction

### 4. Informational Intent

**Definition**: User seeking knowledge, not ready to buy

**Signals:**
- "How to", "what is", "why"
- "Guide", "tutorial", "tips"
- "Definition", "meaning", "explained"
- Question format queries
- "Learn", "understand", "basics"

**Examples:**
```
how to improve seo
what is machine learning
project management best practices
running tips for beginners
why is my website slow
```

**Funnel Stage**: Top / Awareness

**Recommended Actions:**

| Business Model | Recommended Action |
|----------------|-------------------|
| Content marketing | Target with blog content |
| High-touch B2B | Target for lead magnets |
| Transactional eComm | Usually exclude |
| Service business | Evaluate (may indicate need) |

**Conversion Expectations:**
- CVR: 10-30% of average (direct conversion)
- Value: Top-of-funnel awareness
- Strategy: Content marketing or exclude

## Intent Classification Decision Tree

```
Query Analysis Start
│
├── Contains brand name?
│   ├── Yes → NAVIGATIONAL
│   │   ├── Your brand → Protect, high bid
│   │   └── Competitor → Evaluate conquest or exclude
│   │
│   └── No → Continue
│
├── Contains action/transaction signals?
│   │ (buy, order, price, pricing, subscribe, download,
│   │  near me, [product + spec])
│   ├── Yes → TRANSACTIONAL (High priority)
│   └── No → Continue
│
├── Contains comparison/research signals?
│   │ (best, top, review, vs, compare, alternative, for [use])
│   ├── Yes → COMMERCIAL INVESTIGATION (Medium priority)
│   └── No → Continue
│
├── Contains information-seeking signals?
│   │ (how, what, why, guide, tutorial, tips, learn)
│   ├── Yes → INFORMATIONAL (Low priority or exclude)
│   └── No → Continue
│
└── Ambiguous → Analyze query context and performance data
```

## Intent-Based Campaign Structure

### Recommended Structure

```
Account
├── Brand Campaigns (Navigational)
│   ├── Brand - Exact
│   ├── Brand - Products
│   └── Brand - Defense
│
├── High-Intent Campaigns (Transactional)
│   ├── Product - Buy Intent
│   ├── Service - Purchase Ready
│   └── Location - Near Me
│
├── Mid-Funnel Campaigns (Commercial)
│   ├── Comparison Keywords
│   ├── Best/Top Keywords
│   └── Alternative Keywords
│
└── Top-Funnel Campaigns (Informational) [Optional]
    ├── How-To Keywords
    └── Guide Keywords
```

### Budget Allocation by Intent

| Intent Type | Budget % | Bid Strategy | Target |
|-------------|----------|--------------|--------|
| Transactional | 50-60% | Aggressive | Maximize conversions |
| Commercial | 25-35% | Moderate | Cost-efficient leads |
| Navigational (brand) | 10-15% | Protective | Defend position |
| Informational | 0-10% | Conservative | Awareness only |

## Intent Signals Reference

### Transactional Signals (High Value)

**Purchase Intent:**
```
buy, purchase, order, shop
get, acquire, obtain
pricing, price, cost, quote
hire, book, reserve, schedule
subscribe, sign up, register
download, install
coupon, discount, deal, promo
[product] + [specification]
```

**Local Intent:**
```
near me, nearby, close to
in [city], [city] [service]
open now, 24 hour
directions to, how to get to
```

**Urgency Signals:**
```
today, now, immediately
fast, quick, same day
emergency, urgent
asap
```

### Commercial Signals (Medium Value)

**Comparison:**
```
best, top, leading, #1
review, reviews, rated, rating
compare, comparison, vs, versus
alternative, alternatives to
better than, cheaper than
```

**Evaluation:**
```
pros and cons, advantages
worth it, should i
good, bad, reliable
features, benefits
for [specific use case]
for [persona/industry]
```

**Social Proof:**
```
popular, trending, recommended
trusted, award winning
customer reviews
case study
```

### Informational Signals (Lower Value)

**Educational:**
```
how to, how do, how does
what is, what are, what does
why, why do, why does
when, when to, when should
where, where to, where can
```

**Learning:**
```
guide, tutorial, tips
learn, learning, beginner
basics, fundamentals, 101
definition, meaning, explained
examples, sample, template
course, class, training
```

## Landing Page Alignment Matrix

| Intent | Landing Page Type | Key Elements |
|--------|------------------|--------------|
| Navigational (brand) | Homepage or brand page | Brand messaging, navigation |
| Transactional | Product/pricing page | CTA, price, buy button |
| Commercial | Comparison/review page | Features, proof, comparison |
| Informational | Blog/resource page | Content, lead magnet |

### Mismatch Impact

| Query Intent | Wrong Page | CVR Impact |
|--------------|------------|------------|
| Transactional | Blog post | -60 to -80% |
| Commercial | Homepage | -40 to -60% |
| Navigational | Category page | -20 to -40% |
| Informational | Product page | -50 to -70% |

## Intent Scoring for Queries

### Automated Scoring Framework

Assign intent scores based on signal presence:

```
Intent Score Calculation:

Transactional Base: 100 points
Commercial Base: 60 points
Informational Base: 20 points
Navigational: Context-dependent

Modifiers:
+ "buy/purchase/order": +40 points
+ "price/pricing/cost": +30 points
+ "near me/local": +25 points
+ "best/top/review": +20 points (commercial)
+ "how to/what is": -30 points (informational)
+ Brand name present: +50 points (navigational)
+ "free/cheap" (if premium): -20 points

Score Interpretation:
> 100: High transactional → Aggressive targeting
70-100: Medium transactional → Standard targeting
40-70: Commercial → Moderate targeting
< 40: Informational → Evaluate or exclude
```

### Manual Classification Criteria

When automated signals are ambiguous:

1. **Context analysis**: What would searcher do next?
2. **SERPs check**: What Google shows (ads, shopping, content)
3. **Performance data**: Historical CVR for similar queries
4. **Business fit**: Does query align with offering?

## Multi-Intent Queries

Some queries contain multiple intent signals:

**Example**: "best crm software pricing"
- "best" → Commercial
- "pricing" → Transactional
- Combined → High-value commercial leaning transactional

**Handling Strategy:**
1. Classify by dominant signal (usually transaction trumps)
2. Create ad copy addressing both intents
3. Landing page should satisfy both needs
4. Bid based on higher-value intent

## Intent Evolution Mapping

Users often progress through intent stages:

```
Informational → Commercial → Transactional

Example Journey:
1. "what is crm software" (Informational)
2. "best crm for small business" (Commercial)
3. "hubspot vs salesforce" (Commercial)
4. "hubspot crm pricing" (Transactional)
5. "hubspot crm sign up" (Transactional)
```

**Strategy Implications:**
- Remarketing: Target informational visitors with commercial/transactional ads
- Content: Create content for early-stage queries
- Attribution: Recognize multi-touch journeys

## Industry-Specific Intent Patterns

### eCommerce
- High transactional: [product] + [size/color/model]
- Common commercial: "best [product] for [use]"
- Exclude: "how to make [product]" (DIY)

### B2B SaaS
- High transactional: [software] + "pricing/demo/trial"
- Common commercial: "[category] software comparison"
- Nurture: "[category] best practices" (content)

### Local Services
- High transactional: [service] + "near me/[city]"
- Commercial: "[service] reviews/ratings"
- Exclude: "how to [DIY service]"

### Healthcare
- Transactional: "[provider] appointment/schedule"
- Commercial: "best [specialist] in [city]"
- Exclude: "[condition] symptoms" (research)

---

**Use this framework to systematically classify queries, align landing pages, and optimize campaigns by intent stage for maximum conversion efficiency.**
