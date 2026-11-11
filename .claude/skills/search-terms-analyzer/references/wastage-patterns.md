# Search Term Wastage Patterns by Industry

Comprehensive guide to identifying wasteful search queries with industry-specific patterns and benchmarks.

## Universal Wastage Patterns

These patterns apply across all industries and should be checked first.

### 1. Informational Queries

**Pattern**: Users seeking information, not ready to buy/convert

**Common Modifiers:**
```
how to, what is, why, when, where
guide, tutorial, tips, advice, help
learn, course, class, training, certification
definition, meaning, explained, overview
examples, samples, templates (sometimes)
```

**Industry Exceptions:**
- Education/courses: "course" and "training" may convert
- B2B content marketing: "guide" may be lead magnet traffic
- DIY services: "how to" may indicate need for professional help

**Recommended Action**: Phrase match negatives for most; evaluate exceptions

### 2. Job Seeker Queries

**Pattern**: People looking for employment, not products/services

**Common Modifiers:**
```
jobs, job, careers, career
hiring, employment, work
salary, pay, wages, compensation
internship, apprentice, entry level
resume, interview, application
remote work, work from home (job context)
```

**High-Cost Indicators:**
- "[your brand] jobs" - Very common, often high volume
- "[industry] careers" - Broad match pickup
- "hiring [service type]" - Ambiguous intent

**Recommended Action**: Broad match negatives for theme; exact for brand variations

### 3. DIY/Free Seeker Queries

**Pattern**: Users wanting to do it themselves or get free alternatives

**Common Modifiers:**
```
free, free download, free online
cheap, cheapest, budget, affordable
DIY, do it yourself, homemade
template, printable, download
make your own, build your own
open source, free alternative
```

**Industry Exceptions:**
- Freemium products: "free" may be top-of-funnel
- Template businesses: "template" is core product
- Budget brands: "cheap" is target audience

**Recommended Action**: Evaluate fit; exclude if premium positioning

### 4. Competitor Brand Queries

**Pattern**: Users searching for competitors by name

**Decision Framework:**
- **Exclude if**: Low conversion rate (<30% of avg), high CPC, brand confusion
- **Keep if**: Conquest strategy, competitive product, clear differentiator

**Common Patterns:**
```
[competitor name]
[competitor] alternative
[competitor] vs [your brand]
[competitor] pricing, reviews, login
```

**Recommended Action**: Analyze performance; exclude poor performers as exact match

### 5. Support/Login Queries

**Pattern**: Existing customers seeking support, not new business

**Common Modifiers:**
```
login, sign in, log in, account
support, help desk, customer service
contact, phone number, email
cancel, refund, return
password, reset, forgot
```

**Impact**: High click cost, zero new customer value

**Recommended Action**: Exact match negatives for brand + support terms

## Industry-Specific Wastage Patterns

### eCommerce

**Common Wastage:**
```
// Size/fit queries (often browse, not buy)
size chart, sizing guide, measurements
does [product] fit, will [product] fit

// Review queries (research phase)
[product] reviews, is [product] good
[product] reddit, [product] forum

// Used/secondhand (if selling new)
used [product], secondhand, refurbished
pre-owned, vintage (unless selling)

// Repair/parts (if selling whole products)
[product] repair, fix [product]
[product] parts, replacement [part]

// Wrong category
[product] for [wrong use case]
[product] [wrong size/type]
```

**Benchmarks:**
- Informational queries: Typically 5-12% of spend
- Review queries: 3-8% of spend, may convert at 50% of avg
- Used/secondhand: 2-5% of spend if selling new only

### B2B / SaaS

**Common Wastage:**
```
// Student/learning queries
[software] for students, student discount
learn [software], [software] tutorial
[software] certification, course

// Free tier abuse
[software] free, [software] trial crack
[software] open source alternative
free [category] software

// Enterprise misalignment (if SMB)
[software] enterprise, [software] for large
[software] oracle, [software] SAP integration

// SMB misalignment (if enterprise)
[software] small business, [software] startup
cheap [software], affordable [software]

// Technical/developer queries
[software] API documentation
[software] github, [software] source code
[software] developer, SDK
```

**Benchmarks:**
- Student queries: 3-7% of spend for B2B
- Free-seeker queries: 5-15% of spend
- Wrong segment: 5-10% of spend if targeting mismatch

### Lead Generation (Services)

**Common Wastage:**
```
// DIY queries
how to [service] yourself
DIY [service], [service] tips
[service] checklist, [service] guide

// Price shopping (if premium)
cheap [service], low cost [service]
[service] prices, how much [service]
free [service] estimate (sometimes)

// Licensing/careers
[service] license, become a [provider]
[service] certification, [service] school
[service] salary, [service] jobs

// Geographic mismatch
[service] [wrong city/state]
[service] near [wrong location]

// Wrong service type
[related but different service]
[service] [wrong specialization]
```

**Benchmarks:**
- DIY queries: 5-15% of spend
- Geographic mismatch: 3-10% (if geo-targeting issues)
- Wrong service: 5-12% of spend

### Local Business

**Common Wastage:**
```
// Wrong location
[business] [wrong neighborhood]
[business] near [wrong landmark]
[business] [wrong zip code]

// Chain/franchise confusion
[business] corporate, [business] headquarters
[business] franchise, [business] owner

// Review/research
[business] reviews, is [business] good
[business] yelp, [business] google reviews

// Hours/contact (existing customers)
[business] hours, [business] open
[business] phone, [business] address
[business] menu, [business] prices (restaurants)
```

**Benchmarks:**
- Wrong location: 5-20% if broad geo-targeting
- Review queries: 2-5% of spend
- Hours/contact: 3-8% of spend

### Healthcare / Medical

**Common Wastage:**
```
// Symptom research (not appointment ready)
symptoms of [condition]
what causes [condition]
is [symptom] serious

// Home remedies
home remedies for [condition]
natural treatment [condition]
[condition] cure, [condition] healing

// Insurance/cost queries
does insurance cover [treatment]
[treatment] cost, how much [treatment]
free [treatment], [treatment] assistance

// Medical professional queries
how to become [specialist]
[specialist] salary, [specialist] education
[specialist] certification
```

**Benchmarks:**
- Symptom queries: 10-25% of spend
- Home remedy: 5-15% of spend
- Insurance/cost: 5-12% of spend

### Education / Courses

**Common Wastage:**
```
// Free content seekers
[topic] free course, free [topic] training
[topic] youtube, [topic] tutorial free
[certification] free, [certification] dumps

// Accreditation queries
is [school] accredited
[certification] worth it, [certification] value

// Job queries
[field] jobs, [certification] salary
[field] career, [field] employment

// Competitor research
[competitor school] reviews
[competitor] vs [your school]
```

**Benchmarks:**
- Free seekers: 15-30% of spend for paid courses
- Job queries: 5-10% of spend
- Competitor research: 5-12% of spend

## Wastage Quantification Formula

### Calculating Monthly Wastage

```
Monthly Wastage = Σ (Wasteful Query Cost)

Where Wasteful = Query meets criteria:
- 0 conversions AND (clicks ≥ 10 OR cost ≥ 2x CPA target)
- CVR < 25% of average AND cost > $100
- Clearly irrelevant intent (manual review)
```

### Wastage Severity Scoring

| Score | Criteria | Priority |
|-------|----------|----------|
| Critical | >$500/month, 0 conversions, clearly irrelevant | Exclude immediately |
| High | >$200/month, 0 conversions OR <25% avg CVR | Exclude within 24 hours |
| Medium | >$50/month, <50% avg CVR | Review and decide |
| Low | <$50/month, underperforming | Monitor, batch exclude |

### Industry Benchmarks for Acceptable Wastage

| Industry | Acceptable Wastage | Concerning | Critical |
|----------|-------------------|------------|----------|
| eCommerce | <8% | 8-15% | >15% |
| B2B SaaS | <10% | 10-18% | >18% |
| Lead Gen | <12% | 12-20% | >20% |
| Local Services | <15% | 15-25% | >25% |
| Healthcare | <15% | 15-25% | >25% |

## Red Flag Query Patterns

### Instant Exclusion Triggers

These patterns almost always warrant immediate exclusion:

```
// Job seekers (universal)
*jobs*, *careers*, *hiring*, *salary*

// Explicit free seekers
*free download*, *free online*, *free trial crack*
*torrent*, *pirate*, *crack*, *keygen*

// Legal/compliance issues
*lawsuit*, *class action*, *scam*

// Completely wrong product
[totally unrelated product category]

// Spam/bot indicators
[random character strings]
[excessive length queries with gibberish]
```

### Context-Dependent Patterns

Review these based on business model:

```
// May be wasteful OR valuable
*reviews* - Research phase but high intent
*alternatives* - Comparison shopping
*vs* - Commercial investigation
*cheap* - Price sensitive but may convert
*best* - Research but high intent
*near me* - High intent for local
```

## Negative Keyword Implementation Priority

### Week 1 Priority (Immediate)
1. Job seeker queries (easy win, universal)
2. Support/login queries (existing customer traffic)
3. Obvious irrelevant products/services
4. Geographic mismatches (if local business)

### Week 2 Priority
1. Competitor brands (if not converting)
2. DIY/free seeker queries
3. Wrong customer segment
4. Low-value informational queries

### Ongoing Monitoring
1. Emerging wastage patterns
2. New competitor terms
3. Seasonal irrelevant queries
4. Match type expansion issues

## Wastage Prevention Strategies

### Proactive Negative Lists

Build negative keyword lists BEFORE launching campaigns:

1. **Universal Negatives**: Jobs, careers, free, DIY (as appropriate)
2. **Industry Negatives**: Common wastage for your vertical
3. **Competitor Negatives**: Unless intentionally targeting
4. **Geographic Negatives**: If local/regional business

### Match Type Strategy

Prevent wastage through match type selection:

- **Exact Match**: Zero wastage risk, but limited reach
- **Phrase Match**: Moderate risk, add negatives proactively
- **Broad Match**: High risk, requires robust negative lists

### Regular Review Cadence

| Review Type | Frequency | Focus |
|-------------|-----------|-------|
| High-spend queries | Weekly | Top 50 by cost |
| Zero-conversion | Bi-weekly | All 0-conversion queries |
| Full audit | Monthly | Complete search term analysis |
| Deep dive | Quarterly | N-gram analysis, restructuring |

---

**Use these patterns to systematically identify and eliminate wasteful search queries, reducing spend on low-value traffic while preserving high-intent queries.**
