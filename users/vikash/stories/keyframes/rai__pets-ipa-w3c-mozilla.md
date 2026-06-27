---
saga: Responsible & Private AI (Meta, 2021–2023)
epic: PETs / IPA (Privacy Enhancing Technologies)
story: Founding W3C PATCG and co-authoring IPA with Mozilla
question_categories: [ambiguity, leadership, technical_bet]
principles: [P1, P8, P2, P7]
rubric_map: { amazon: "Think Big / Earn Trust", google: "Strategic / open ecosystems", anthropic: "field-building, ambitious-careful", meta: "Industry standards" }
source: project_inventory.md (PETs Story 2, 2022 notes) · story_bank.md #1 · amazon_leadership_principles.md (#8, #11)
default_format: STAR+
covers_essential: [0to1, Contrarian Bet]
generated_by: story_builder (Saga Method)
---

# Story: Founding W3C PATCG (IPA with Mozilla)

## 10-second hook (BLUF)
After iOS14 and cookie deprecation broke ad measurement, I bet that the durable fix wasn't a Meta-only workaround but a new *industry standard* — so I drove the founding of the W3C PATCG and co-authored the Interoperable Private Attribution proposal with Mozilla, a privacy hawk, getting competitors to the same table.

## STAR+ (default delivery — S 10% · T 10% · A 60% · R 20%)

**Situation** — iOS14 ATT plus third-party cookie deprecation caused a fundamental signal loss across digital advertising. This wasn't a Meta problem — it was an industry problem, and no single company controlled the fix: it needed mobile-OS vendors, browser vendors, regulators, competitors, advertisers, and users to move together.

**Task** — I owned Meta's privacy-preserving measurement strategy. The hard part: we did *not* control the outcome, so the mandate was really "create alignment across an industry that doesn't trust us."

**Action** — I treated this as a standards-and-ecosystem problem, not a product-shipping problem:
- I identified **IPA (Interoperable Private Attribution)** — built on **secure multi-party computation (MPC)** so no single party ever sees the user — as the highest-leverage bet, and made it Meta's position.
- The signature move: I **co-authored the proposal with Mozilla**. Partnering with a privacy-first browser maker — a natural skeptic of an ad giant — gave the proposal credibility no Meta-authored doc could have. That required mapping Mozilla's incentives and genuinely meeting them, not co-opting them.
- I drove the **founding of the W3C PATCG** (Private Advertising Technology Community Group) to give the work a neutral home, and pulled in major players plus competitors — getting most of the big platforms to the table.
- I defined a **maturity framework with explicit exit criteria** so a multi-party effort had a spine, and I **educated the ecosystem** through blogs, talks, and the PETS Summit, because a standard moves only when the players understand it.

**Result** — IPA became a co-authored, externally-credible proposal inside a standards body with cross-industry participation — converting an existential platform shock into durable, industry-level privacy infrastructure and positioning Meta to shape the post-cookie web rather than just react to it. `[NEEDS INPUT: current status/adoption of PATCG/IPA as of your last update — confirm the up-to-date outcome]`

## Principle closes (the lenses — pick per question)
- **Through P1 "turn shocks into infrastructure" (for an AMBIGUITY / 0→1 question):**
  Foreground that there was no playbook and you built an industry mechanism from nothing.
  *Close:* "When the shock is industry-wide and you don't control the fix, the move is to build the shared infrastructure — I'd rather author the standard than optimize around someone else's."
- **Through P8 "to move an industry, educate it" + P2 "map incentives" (for a LEADERSHIP / INFLUENCE question):**
  Foreground the Mozilla partnership and getting competitors to the table.
  *Close:* "I got a privacy hawk to co-author with an ad company by meeting their actual incentive, and I moved the room by teaching it — influence at industry scale is incentive-mapping plus education, not authority."

## Likely pushback (rehearse — see sample_interview_tradeoff.md)
- **Process probe:** "How did you actually get Mozilla to say yes? What did *they* get?" → Be concrete about their incentive (a genuinely private standard they could endorse). `[NEEDS INPUT: the specific terms]`
- **Value challenge:** "Isn't an industry standards effort just a way to slow-walk a problem and look good?" → Counter with the maturity framework + exit criteria you imposed to force progress; concede that pace was a real risk (see the companion failure story).
- **Bias test:** "Did you pick IPA because it was best, or because it suited Meta?" → Honest: name the alternatives considered and why MPC-based IPA was the most defensible privacy posture, not just the most convenient.

## Alternate formats
- **DIGS** is strong: the *alternatives* (Meta-only workaround vs. open standard) and the unlikely Mozilla alliance are the memorable parts.

## Company tailoring notes
- **Anthropic:** field-building + getting competitors to collaborate on a hard, careful standard is a near-perfect signal — lead with it.
- **Amazon:** *Think Big* (rewrite the web's ad standards) + *Earn Trust* (Mozilla, regulators).
- **Google:** open ecosystems + standards fluency.

## Reflection & gaps
- **What I'd repeat:** the credibility-borrowing Mozilla partnership; imposing exit criteria on a multi-party effort.
- **What I'd avoid:** see the paired failure story — initial proposals went out too slowly.
- **[NEEDS INPUT]:** current PATCG/IPA adoption status; specific Mozilla terms. Fill before a live loop.
