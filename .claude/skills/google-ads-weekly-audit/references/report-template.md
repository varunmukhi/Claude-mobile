# Google Ads Weekly Audit

Replace placeholders with evidence or write unavailable. For fixtures, state: Synthetic test data. No live account query took place.

## Scope and reconciliation

| Field | Value |
| --- | --- |
| Account reference | [Private client reference; manager context if needed] |
| Reporting dates | [Inclusive start and end dates] |
| Currency and account time zone | [Retrieved or confirmed values] |
| Data source | [MCP-based / export-based / mixed; dataset timestamps] |
| Conversion definition and target | [Primary actions; CPA or ROAS target] |
| Retrieval | [Queries, filters, complete/incomplete pagination, omitted data] |
| Account spend | [Cost micros / 1,000,000 in account currency] |
| Platform comparison | [User-confirmed total for identical account and dates] |
| Reconciliation status | [Confirmed / pending / mismatch] |
| Query spend | [Separate reported term total and coverage limitation] |

If reconciliation is pending or mismatched, stop here with the discrepancy and next checks. Do not produce recommendations or a health score.

## Phase status and method

| Phase | Method used | Complete / incomplete / not requested | Missing fields |
| --- | --- | --- | --- |
| Campaign performance | [Installed specialist or built-in] | [Status] | [Fields] |
| Search terms | [Installed specialist or built-in] | [Status] | [Fields] |
| Proposed negatives | [Installed specialist or built-in] | [Status] | [Fields] |
| Ad-copy review | Built-in; no separate copy Skill required | [Status] | [Fields] |
| Optional PMax | [Requested specialist, unavailable, or not requested] | [Status] | [Fields] |

## Observations and uncertainty

Record metrics with units, denominators, exact dates and evidence references. Separate account totals from query totals. Describe conversion delays, low volume, filters and retrieval gaps. Do not infer a cause from correlation.

### Campaign performance

| Campaign | Spend | Primary conversions | CPA / ROAS | Evidence | Uncertainty |
| --- | --- | --- | --- | --- | --- |
| [Name] | [Currency value] | [Value or unavailable] | [Value or unavailable] | [Source] | [Limits] |

### Search terms and proposed negatives

| Query or candidate | Observed spend | Conversion history | Business context | Proposed match type | Hold or review reason |
| --- | --- | --- | --- | --- | --- |
| [Term] | [Currency value] | [Evidence or missing] | [Confirmed or unknown] | [Proposal only] | [Overlap and uncertainty] |

A conversion-bearing query matching a proposed negative stays on hold for owner review. Informational intent, low CTR or zero conversions alone does not justify exclusion.

### Ad-copy review and drafts

Record existing-ad diagnosis separately from proposed text. Show character counts for each draft headline and description. Mark unsupported diagnosis incomplete. Do not promise policy approval or performance gains.

### Optional PMax

State whether requested, which checks ran and which fields were unavailable. Do not imply complete placement or query coverage.

## Estimates, kept separate from observations

| Estimate | Method and period | Assumptions | Overlap checks | Confidence |
| --- | --- | --- | --- | --- |
| [Value or omitted] | [Calculation] | [Explicit assumptions] | [Evidence] | [Limits] |

Observed spend is not guaranteed savings. A monthly projection requires an explicit extrapolation method. Omit unsupported estimates and invented benchmarks.

## Optional health score

Use the rubric in `benchmarks.md`. Show inputs and weights. Call it the Skill's rubric, not a Google score. Mark unavailable if reconciliation or essential conversion evidence is missing. Do not hide incomplete phases inside a complete-account score.

## Human review queue

| Priority | Evidence | Proposed action | Risk or uncertainty | Human owner | Approval status |
| --- | --- | --- | --- | --- | --- |
| [Rank] | [Reference] | [Proposal] | [Limits] | [Named owner or unassigned] | Pending |

Account changes occur through a separate owner-approved process. This report performs no mutations.

## Next reporting period

Name comparable completed dates, metrics to recheck, conversion-delay considerations and missing data to retrieve. Do not predict a result without evidence.
