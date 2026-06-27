---
saga: Frontier Model Safety & Human Alignment (MSL, 2024–present)
epic: Llama Safety & Red Teaming (open weights)
story: Defining safety for open-weight models — the transparency bet (Purple Llama)
question_categories: [ambiguity, technical_bet, leadership]
principles: [P7, P1, P6]
rubric_map: { amazon: "Are Right A Lot / Success & Scale Bring Broad Responsibility", google: "Open ecosystems / 10x", anthropic: "transparency, safety-as-product", meta: "Openness" }
source: project_inventory.md (MSL, Purple Llama) · amazon_leadership_principles.md (#4, #16) · story_bank.md #3
default_format: STAR+
covers_essential: [Contrarian Bet, 0to1]
generated_by: story_builder (Saga Method)
---

# Story: Safety for Open Weights — The Transparency Bet

## 10-second hook (BLUF)
For open-weight models you can't recall or control downstream, I bet that *published* safety — open evaluations and safeguard models like Purple Llama and Llama Guard — would build more trust than a black box, and that ecosystem is now part of why Llama shipped responsibly at 100M+ downloads with standards recognized by MLCommons and the White House.

## STAR+ (default delivery — S 10% · T 10% · A 60% · R 20%)

**Situation** — Frontier capability was moving fast, and Meta's strategy was open weights. That breaks the usual safety model: once weights are released you can't claw them back or gate usage, and the industry default for "safety" was a closed, black-box posture you simply trust.

**Task** — I owned the PM strategy for what "safe enough to release" means for open-weight Llama — across alignment, safety evaluations, and child safety — without strangling research velocity.

**Action** — The core ambiguity was *defining safety for artifacts you no longer control*. I drove a transparency-first posture rather than a black-box one:
- Shaped investment across the **Purple Llama** ecosystem — a red+blue-teaming approach — including **Llama Guard** (a safeguard model), **CyberSec Eval** (a security benchmark), and **Code Shield** (inference-time filtering).
- Made the contrarian call that **publishing** evals and safeguards builds more durable trust than hiding them: for open weights, transparency *is* the safety story, because the community can verify and extend it.
- Held the line on a real tradeoff: tuning safeguards (e.g., Llama Guard) to reduce harm **without** driving false-refusal rates so high the model became useless — safety that destroys utility isn't safety. `[NEEDS INPUT: the false-refusal metric / before-after — project_inventory flags this; confirm]`
- Scaled the *judgment* beyond my team by building the GenAI PM education program (800+ PMs) so safety calls weren't a bottleneck on me.

**Result** — Llama shipped responsibly as open weights now at **100M+ downloads**, with a safety ecosystem (Purple Llama et al.) that became an external reference point — recognized by **MLCommons** and cited at the **White House** level. The transparency bet turned "open is unsafe" into "open can be *more* accountable."

## Principle closes (the lenses — pick per question)
- **Through P7 "transparency builds more trust than a black box" (for a CONTRARIAN BET question):**
  Foreground betting against the closed-safety industry default.
  *Close:* "I bet that for open weights, publishing your safety work beats hiding it — verifiable safeguards compound trust faster than 'trust us.' That's the call I'd make again."
- **Through P6 "broad responsibility at scale" (for an AMBIGUITY / ethics question):**
  Foreground defining safety for something you can't control downstream, including child safety.
  *Close:* "Shipping powerful open models means owning the second-order effects you can't recall — so we built the safeguards *before* release rather than apologizing after."

## Likely pushback (rehearse — see sample_interview_tradeoff.md)
- **Process probe:** "How did you decide a model was safe *enough* to release as open weights? What was the bar?" → Be ready with the eval gates and who signed off. `[NEEDS INPUT: the release-gate criteria]`
- **Value challenge:** "Publishing CyberSec Eval also hands a roadmap to attackers — how is that net-safer?" → Argue defenders benefit more than attackers from shared benchmarks; concede it's a genuine dual-use tension you weighed.
- **Bias test:** "Was 'transparency is safer' your conviction or post-hoc justification for a business decision (open weights as strategy)?" → Be honest that open weights was the company bet; your contribution was making it *defensible*, and you'd have pushed back if the safeguards couldn't reach bar.

## Alternate formats
- **STAR+** for an ethics/judgment framing; **DIGS** if you want to lead with the open-vs-closed stakes.

## Company tailoring notes
- **Anthropic:** lead here — transparency, evals, and owning downstream effects map directly to their core; be ready for deep, honest dual-use discussion and don't oversell.
- **Amazon:** *Are Right, A Lot* + *Success & Scale Bring Broad Responsibility*.
- **Google:** open ecosystems + safety at scale.

## Reflection & gaps
- **What I'd repeat:** safeguards-before-release; scaling safety judgment via education.
- **What I'd avoid:** `[NEEDS INPUT: a real miss from the program]`.
- **[NEEDS INPUT]:** false-refusal metric; release-gate criteria; the specific White House/MLCommons reference. Fill before a live loop.
