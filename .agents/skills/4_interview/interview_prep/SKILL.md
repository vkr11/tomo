---
name: interview_prep
description: >
  Prepare for a specific company interview by combining company dossiers, framework drills,
  and story rehearsal into a focused prep session. Trigger on: "prep me for [company] interview",
  "mock interview for [company]", "what should I expect at [company]", "interview game plan",
  "drill me on [topic]", "practice [company] questions".
---

# Interview Prep

Combines company-specific dossiers (from `company_researcher`), PM frameworks (from `framework/`),
and behavioral stories (from `story_builder`) into a focused, company-targeted interview preparation session.

## Inputs
- Company dossier from `companies/{name}/` (run `company_researcher` first if missing)
- PM frameworks from `framework/`
- Story bank from `users/vikash/stories/`
- Company-specific prep frameworks from `companies/{name}/framework/` (if available)

## Capabilities
1. **Company-specific question prediction** — Based on the dossier, predict likely interview questions
2. **Story-to-question mapping** — Match stories from the story bank to predicted questions
3. **Framework drill** — Walk through relevant PM frameworks with company-specific examples
4. **Gap analysis** — Identify weak areas and recommend additional prep

## Output
```
users/vikash/mock-interviews/{company}/prep_session.md
```

## When to Use
- "Prep me for my [company] interview"
- "What questions should I expect at [company]?"
- "Mock interview for [company]"
- "Drill me on product sense / execution / leadership"
