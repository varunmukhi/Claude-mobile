---
name: google-ads-weekly-audit
description: "Review Google Ads campaign performance, search terms, proposed negatives and ad copy in one report. Use for a weekly or periodic account audit through a connected MCP server or approved dated exports. Read and analyze only. Add a Performance Max phase only when requested and supported by available data."
---

# Google Ads Weekly Audit

Coordinate four base analysis phases. Return evidence and proposals for human review. One prompt can involve several data queries. Coverage and runtime depend on the account and data returned.

## Account actions stay outside this Skill

Do not add negatives, create assets, upload videos, edit labels, pause campaigns, or change bids and budgets. Do not invoke mutation tools, including validation-only mutation calls. Return a review queue with evidence, a proposed action and a human owner. The account owner approves and applies actions through a separate process.

These instructions are not a security boundary. Require a separately configured audit-only server. Inspect exposed tools before account retrieval. Stop if unexpected write tools appear. Do not change server configuration yourself.

## Inputs and collection gate

Before analysis, confirm:

- Client customer ID and manager customer ID, where required.
- Explicit reporting start and end dates, account currency and reporting time zone.
- Primary conversion definition, including which conversion actions count toward it.
- Target CPA or ROAS and business context.
- Landing page URL, if available.

If requested, resolve the most recent 28 complete days in the account's reporting time zone. State the exact dates before analysis. Exclude the current partial day. Ask for missing required inputs rather than inventing them. A missing landing page limits message-match checks. A missing target prevents target-based judgments.

Discover the connected server's actual tool names and schemas through the host's MCP interface. Do not assume legacy names. For the guide's reviewed v0.0.6 configuration, reporting tools are `customers_list_accessible_customers`, `search_search` and `metadata_get_resource_metadata`. Verify the live list rather than assuming those names apply to another version.

1. List accessible accounts using read tools.
2. Confirm the intended client and any manager context with the user.
3. Retrieve reporting currency and time zone.
4. Retrieve total account spend for the explicit dates, using a customer-level aggregate where supported.
5. Convert cost micros by dividing by 1,000,000 before display.
6. Ask the user to compare spend with Google Ads for the same account, dates and currency.
7. Wait for confirmation before the four analysis phases.

If totals or account identity differ, stop analysis pending reconciliation. Check units, dates, time zone, filters, pagination, duplicate rows and incomplete retrieval. Report the mismatch without issuing recommendations or a health score. Do not use query-level spend as the account total. A rounded difference must be explained and agreed, not silently ignored.

Retrieve campaign, query and ad data with read tools only after reconciliation. Use metadata to check field availability and compatible query resources. Record queries, filters, source timestamps and retrieval completeness privately with the report. Follow the tool's pagination or streaming behavior to completion. Do not combine overlapping totals.

If MCP is absent or fails, ask the user before switching to dated CSV exports. Request campaign, search-term and ad exports for matching dates. Confirm account, currency, time zone and spend before analysis. Label the report MCP-based, export-based or mixed, with the provenance of each dataset. Do not present cached or exported inputs as a fresh account query.

## Specialist discovery and precedence

Discover installed Skills using the host's supported Skill list. In Claude Code, personal Skills normally live at `~/.claude/skills/<skill-name>/SKILL.md`. Project and plugin locations can differ. Do not require a directory from another machine.

Use an available specialist for phases 1-3 only within this Skill's collection gates and account-action limits. Specialist examples do not override these rules. If a specialist is absent, use the built-in method below. Record the method used for each phase. Packaged references resolve relative to this Skill directory.

## Calculation and evidence rules

- Divide `cost_micros` by 1,000,000. State the account currency; do not assume USD.
- Calculate CTR as clicks / impressions, CPC as currency cost / clicks, CPA as currency cost / conversions, and ROAS as conversion value / currency cost.
- State the conversion-rate denominator used. Do not silently replace interactions with clicks across campaign types.
- Mark zero-denominator ratios unavailable. Missing conversions are not zero conversions.
- Keep account totals separate from reported search-term totals. Record their coverage ratio only for matching periods and currency.
- Record incomplete pagination, filters and omitted queries. Visible terms may not cover all account spend. Do not label the unreported difference as waste.
- Separate observed metrics from projections and recommendations. Conversion delays and low volume create uncertainty, even for complete calendar days.
- Check proposed negatives against conversion history, overlapping terms, match-type scope and business context. Hold conversion-bearing or uncertain candidates for review.
- Do not classify an informational query, zero-conversion query or low-CTR query as waste on that fact alone.
- Give savings estimates only with a stated method, period, assumptions and overlap checks. Do not equate observed spend with recoverable savings.
- Do not extrapolate to monthly savings without naming the method and assumptions. Omit estimates when evidence is insufficient.
- Do not attribute performance changes to a cause without supporting evidence. Label a possible explanation as a hypothesis.
- Mark a phase incomplete when required data is unavailable. Do not fill gaps with invented values or generic benchmarks.

## Phase 1: Campaign performance

Discover `ad-performance-diagnostic` if installed. Otherwise compare supported campaign metrics with the user's target and comparable completed periods. Check spend, clicks, impressions, primary conversions, conversion value and compatible impression-share fields. Distinguish measured changes from possible explanations.

Return campaign observations, data gaps and proposed checks. Budget, bidding and pause suggestions belong in the human review queue. Use [comparison and score rules](references/benchmarks.md). A health score is optional and is this Skill's rubric, not a Google score.

## Phase 2: Search terms

Discover `search-terms-analyzer` if installed. Otherwise rank available queries by observed cost, primary conversion evidence and business relevance. Compare like-for-like periods and conversion definitions. Identify possible keyword opportunities and landing-page mismatches where evidence exists.

Do not assume the query report contains all spend. Return measured query totals, account totals and coverage limitations separately. Flag low-volume or delayed-conversion cases as uncertain. Candidate concerns feed a review list, not an exclusion command.

## Phase 3: Proposed negative keywords

Discover `negative-keyword-miner` if installed. Otherwise examine phase 2 candidates against conversion history, business context and the reach of the proposed match type. Check whether a phrase or broad negative would block relevant or converting queries.

Use three review categories: supported proposal, needs more evidence, and monitor. None authorizes an account action. Give evidence, proposed match type, risks, observed spend and owner. Keep conversion-bearing candidates on hold until the account owner explains and reviews them. Do not generate an automatic upload list.

## Phase 4: Built-in ad-copy review

This phase works without `google-ads-copy-generator`. Use the built-in method even when that optional Skill is absent.

Review available ad text, message match, supported performance metrics and asset coverage. Treat pinning and CTR differences as review signals, not proof of a cause. Do not invent missing ads, landing-page claims or asset statuses.

When query intent and business details support drafts, propose RSA text for relevant queries. Label it draft copy pending policy and owner review. For responsive search ads, use 3-15 headlines of at most 30 characters and 2-4 descriptions of at most 90 characters. Count characters, including spaces. Check language-specific counting and current platform validation before use.

Limits checked November 10, 2026: [Google RSA creation documentation](https://developers.google.com/google-ads/api/docs/responsive-search-ads/create-responsive-search-ads). Do not claim policy approval from a local character check. If ad data is missing, mark existing-ad diagnosis incomplete. Draft copy only when enough business and intent evidence exists.

## Optional Phase 5: Performance Max

Run only when the user requests PMax review and PMax campaigns exist. Discover `performance-max-auditor` through the host. If absent, report the optional phase unavailable and ask whether the user wants to install it. Do not claim it ran.

Apply the same gates and evidence rules to the specialist. Review only supported campaign, asset-group and other PMax data. Mark unsupported placement, query, audience or asset checks incomplete. Do not infer full placement or query visibility. Merge supported checks into the same report and record the method.

## Report delivery

Use [the report template](references/report-template.md). Label any test fixtures synthetic. Include phase status, provenance, reconciliation, uncertainty, evidence and a human review queue. Do not give a score or recommendations after a spend mismatch. Save a private report as `google-ads-weekly-audit-YYYY-MM-DD.md` in the user-approved workspace. Keep account identifiers and outputs out of public source control.
