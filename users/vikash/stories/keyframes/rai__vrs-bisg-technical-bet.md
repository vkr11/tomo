---
saga: Responsible & Private AI (Meta, 2021–2023)
epic: VRS (Variance Reduction System) / HEC Compliance
story: BISG demographic inference — measuring fairness without collecting race
question_categories: [technical_bet, ambiguity, execution]
principles: [P3, P1, P6]
rubric_map: { amazon: "Invent & Simplify / Insist on Highest Standards", google: "Analytical rigor", anthropic: "do the hard thing correctly", meta: "Privacy by design" }
source: project_inventory.md (Responsible & Private AI) · amazon_leadership_principles.md (#3, #7) · story_bank.md #1
default_format: STAR+
covers_essential: [Contrarian Bet, Technical Bet]
generated_by: story_builder (Saga Method)
---

# Story: BISG — Measuring Fairness Without Collecting Race

## 10-second hook (BLUF)
Under a DOJ mandate to remove discrimination from housing-ad delivery, I bet on a system that infers demographics *without ever collecting race* — using Bayesian Improved Surname Geocoding plus Differential Privacy — and we hit the mandate's bar of under-10% variance for 91.7% of housing ads, turning a settlement into durable fairness infrastructure.

## STAR+ (default delivery — S 10% · T 10% · A 60% · R 20%)

**Situation** — Meta faced a DOJ/HUD mandate over housing-ad targeting discrimination. We had to prove and enforce fairness in ad *delivery* across Housing, Employment, and Credit — but the obvious way to measure fairness (collect users' race/gender) was exactly the data we should not be hoarding, and would create its own privacy and trust problem.

**Task** — I owned the product strategy for fairness in the HEC verticals: define what "fairness" meant operationally, and ship a system that satisfied the regulator without breaking advertiser value or user privacy.

**Action** — The core judgment call was *how to measure a protected attribute we deliberately don't collect*. I drove the bet on the **Variance Reduction System (VRS)**:
- Used **BISG** (Bayesian Improved Surname Geocoding) to *infer* demographic distributions statistically, paired with **Differential Privacy** so no individual's attribute was ever exposed — measuring the outcome without collecting the sensitive input (the hard, correct version of the problem rather than the easy, invasive one).
- Defined "fairness" as a quantitative, auditable target — real-time variance in delivery — so Policy, Legal, and Eng were aligning on a number, not a feeling. `[NEEDS INPUT: the initial algorithm approach that underperformed before VRS — project_inventory flags an "Initial Algorithm Fail"; confirm the detail]`
- Built it to pass **external third-party audit** (e.g., a federal auditor), not just an internal bar — which forced a much higher standard of measurement integrity.

**Result** — We met the DOJ mandate: **under-10% variance for 91.7% of housing ads**, and expanded VRS to Credit and Employment across the US and Canada. Strategically, it converted a settlement obligation into a **moat** — competitors now have to build the same costly fairness infrastructure to operate in these regulated verticals.

## Principle closes (the lenses — pick per question)
- **Through P3 "measure what matters without collecting what you shouldn't" (for a TECHNICAL BET question):**
  Foreground the inference-without-collection design and the rigor.
  *Close:* "I refuse to solve a privacy problem by collecting more sensitive data — the win was proving fairness statistically without ever holding race data. That's the bar I hold on any measurement system."
- **Through P1 "turn shocks into infrastructure" + P6 "compliance = trust" (for a STRATEGY question):**
  Foreground turning a DOJ settlement into a durable competitive moat.
  *Close:* "I treat a regulatory mandate as a chance to build infrastructure competitors will also have to pay for — the fairness system outlived the settlement and became a barrier to entry."

## Likely pushback (rehearse — see sample_interview_tradeoff.md)
- **Process probe:** "BISG is an *estimate* of race from name and geography — how did you defend that to a regulator?" → Be ready on accuracy bounds + why inference + DP is more defensible than collection.
- **Value challenge:** "Did the fairness constraint hurt advertiser performance? How much?" → Acknowledge the real tradeoff between variance limits and advertiser utility; argue durable trust + market access. `[NEEDS INPUT: any advertiser-impact number]`
- **Bias test:** "Was BISG your idea or did Legal hand you the constraint?" → Be honest about what was mandated (the outcome) vs. what you drove (the measurement architecture and the audit bar).

## Alternate formats
- **DIGS** works: *dramatize* the bind (measure race without collecting it), *indicate* the naive alternative (just collect it / use a crude proxy), then your build.

## Company tailoring notes
- **Amazon:** *Invent & Simplify* (measure without collecting) + *Insist on the Highest Standards* (external audit, 91.7%/<10%).
- **Google / Anthropic:** analytical rigor + "do the hard thing correctly"; this is a strong technical-depth signal — be ready to whiteboard BISG vs. DP.

## Reflection & gaps
- **What I'd repeat:** defining fairness as an auditable number up front; building for external audit.
- **What I'd avoid:** `[NEEDS INPUT: lesson from the initial algorithm miss]`.
- **[NEEDS INPUT]:** initial-algorithm-failure detail; advertiser-impact metric; settlement value. Fill before a live loop.
