# Dossier Templates

These are the exact output templates the company_researcher skill produces. Use them verbatim, filling in the `{placeholders}`.

---

## Template: `culture_principles.md`

```markdown
# {Company Name} — Culture & Principles

> {One-line summary of the company's culture philosophy, e.g. "Amazon is governed by 16 Leadership Principles that drive every hiring and promotion decision."}

---

## {N}. {Principle Name}
*{Official definition / description, quoted exactly from source}*

**Interview Signal**: {What "strong" looks like — a one-sentence description of the behavior they want to see in your answer.}

<!-- Repeat for each principle/value -->

---

## Principle Priority Tiers

| Priority Tier | Principles | Why |
|---|---|---|
| **Tier 1 — Always tested** | {list} | {reason} |
| **Tier 2 — Frequently tested** | {list} | {reason} |
| **Tier 3 — Differentiators** | {list} | {reason} |

> **Pro Tip**: {A company-specific tactical tip for using these principles in interviews.}
```

### Guidelines for `culture_principles.md`

- Quote official definitions exactly when available. If no official public text exists, paraphrase clearly and note the source.
- Interview Signals should be actionable — "Show you did X" not "Be someone who values X."
- Tier assignments are based on frequency of testing, not importance. Tier 1 = appears in nearly every loop.
- If the company has fewer than 5 principles, skip the tier table and just flag the top 2-3.

---

## Template: `interview_process.md`

```markdown
# {Company Name} — PM Interview Process

> **Role Target**: {Level, e.g. "Senior PM (L6) / Principal PM (L7)"}

---

## Interview Stages

| Stage | Duration | Format | Focus |
|---|---|---|---|
| **1. {Stage Name}** | {duration} | {format} | {focus areas} |
<!-- Repeat for each stage -->

---

## The Loop — Round Breakdown

| Round | Interviewer | Focus | Key Principles |
|---|---|---|---|
| {N} | {who} | {what they test} | {which principles} |
<!-- Repeat for each round -->

---

## Special Rounds

{Describe any unique interview elements: Bar Raiser, case studies, presentations, written exercises, take-homes, etc. If none, write "No special rounds documented."}

---

## Communication Style

| Do | Don't |
|---|---|
| {specific tip} | {specific anti-pattern} |
<!-- 4-6 rows -->

---

## Gaps & Caveats

{Honestly note what information was NOT available from public sources. E.g., "Limited public data on the exact number of rounds for L7+ candidates."}

---

## Key Resources

- [{source name}]({URL})
<!-- 3-5 links to the best public resources -->
- Your story mappings: `../../users/vikash/stories/`
```

### Guidelines for `interview_process.md`

- If the company's exact loop structure isn't publicly documented, note this in Gaps and provide the best available approximation.
- Communication Style should reflect the company's actual culture (e.g., Amazon = BLUF, Google = structured frameworks, Meta = speed + metrics).
- Key Resources should link to the 3-5 most useful public guides, not every source you read.

---

## Template: `README.md`

```markdown
# {Company Name} — Interview Prep Dossier

> Target Level: {role level}

## Files

| File | Purpose |
|---|---|
| [culture_principles.md](./culture_principles.md) | {Company}'s values/principles with interview signals |
| [interview_process.md](./interview_process.md) | Full interview loop breakdown and strategy |
| [_raw/](./_raw/) | Raw web dumps and reference articles |

## Cross-References

| What | Where |
|---|---|
| **Your story mappings** | [stories/](../../users/vikash/stories/) |
| **Master 8-pillar guide** | [framework/README.md](../../framework/README.md) |
| **Saga Method** | [saga-method/](../../framework/saga-method/the_saga_method.md) |

## Prep Checklist

- [ ] Map principles to 2+ stories using the Saga Method
- [ ] Practice behavioral rounds with company-specific follow-up style
- [ ] Research the specific team/org you're interviewing for
- [ ] Do 2 mock rounds with principle focus
- [ ] Prepare "Why {company}?" answer
```
