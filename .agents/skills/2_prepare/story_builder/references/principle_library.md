# Principle Library — Vikash's Portable Operating System

> Reference for `story_builder`. The **Demand-side translation layer** of the Saga Method.
> A Principle is *the reason Vikash made the decision he made* — reusable across his whole career.
> Stories are told *through* a Principle (the "lens"). Company rubrics are plug-ins onto these Principles.

## How to use this file
1. When generating a Story, tag it with the Principle(s) it can be told through (pull from this library).
2. When tailoring for a company, translate the Principle to that company's rubric using the mapping table.
3. The Principle shapes **what you foreground and how you close** — see `the_saga_method.md` Part 3.

---

## Vikash's Principles (in his own words)

These are synthesized from his actual decisions across the Sagas. Each is portable — it shows up in multiple Stories. Keep the phrasing in his voice; it's what makes a close land as conviction rather than cliché.

### P1 — "Turn external shocks into durable infrastructure."
When a platform or policy shock hits (iOS14, cookie deprecation, a DOJ mandate, EU DMA), don't patch — build the durable system that becomes a moat competitors must also pay for.
- **Lives in:** PETs/IPA, VRS, AFS, WhatsApp signal loss.
- **Maps to:** Amazon *Think Big* / *Invent & Simplify* · Google *Strategic Thinking / 10x* · Anthropic *ambitious but careful* · Meta *Build durable systems*.

### P2 — "Map the other team's incentives before you try to align."
Influence without authority starts with understanding what the opposing team actually gains. Then reframe your ask in their terms.
- **Lives in:** Ads-team attribution conflict, Policy-vs-Eng on "variance", Mozilla partnership, Legal pushback.
- **Maps to:** Amazon *Earn Trust* / *Have Backbone* · Google *Collaboration / Googleyness* · Meta *Work across boundaries*.

### P3 — "Measure what matters without collecting what you shouldn't."
The best privacy/fairness solution proves the outcome without hoarding the sensitive data — invent the measurement, don't compromise the principle.
- **Lives in:** VRS/BISG (demographic inference without collecting race), IPA/MPC, Differential Privacy.
- **Maps to:** Amazon *Invent & Simplify* / *Insist on the Highest Standards* · Google *Analytical Rigor* · Anthropic *do the hard thing correctly*.

### P4 — "Sort decisions by reversibility, then move at the speed each allows."
Irreversible decisions (infra you'll have to migrate, data you'll have to unwind) get rigor; reversible ones get speed. Name which kind you're in before deciding.
- **Lives in:** The notifications/privacy tradeoff (sample story), batch-vs-realtime, ship-to-stop-the-bleeding then build the fix.
- **Maps to:** Amazon *Bias for Action* + *Are Right, A Lot* · Google *Execution* · Meta *Move fast (with stable infra)*.

### P5 — "Bring options, not just problems."
Never walk into a leadership room with only a blocker. Bring a phased path that captures most of the value within the constraint.
- **Lives in:** Phased bundling (25% now / 40% later), WCA sequencing, AFS pivot to "less personalized ads."
- **Maps to:** Amazon *Deliver Results* / *Ownership* · Google *Drive / problem-solving* · Meta *Bias to impact*.

### P6 — "Compliance is a consumer-trust opportunity, not a constraint."
Reframe the regulatory requirement as a chance to earn durable user trust and competitive differentiation.
- **Lives in:** HUD/DoJ fairness, AFS/DMA, Child Safety, external audits (Guidehouse).
- **Maps to:** Amazon *Customer Obsession* / *Success & Scale Bring Broad Responsibility* · Google *Trust & Safety* · Anthropic *safety as product*.

### P7 — "Transparency builds more trust than a black box."
Bet that openness (open weights + published evals, co-authored standards) compounds trust faster than secrecy — even when the industry defaults to closed.
- **Lives in:** Purple Llama / CyberSec Eval / Llama Guard, W3C PATCG, open-weights safety strategy.
- **Maps to:** Amazon *Are Right, A Lot* / *Earn Trust* · Anthropic *transparency / interpretability* · Google *open ecosystems*.

### P8 — "To move an industry, educate it."
Standards and ecosystems shift when you teach the players — blogs, summits, partnerships, curricula — not when you ship in silence.
- **Lives in:** W3C PATCG formation, Mozilla co-authorship, PETS Summit, GenAI Bootcamp (800+ PMs), 7,500+ candidates.
- **Maps to:** Amazon *Hire & Develop / Earth's Best Employer* · Google *Thought leadership* · Meta *Scale through others*.

### P9 — "Ask for help sooner; scale yourself through process."
Hard-won lesson: stretching to cover a gap solo lowers quality. Define priorities, escalate early, build the operating cadence that scales the team.
- **Lives in:** Friend Graph 38-person team / "ask for help sooner," hiring 2 PMs, operating models.
- **Maps to:** Amazon *Ownership* / *Learn & Be Curious* · Google *Self-awareness / managing scale* · Meta *Org leadership*.

### P10 — "Own the gap, even when it isn't your bug."
Act on behalf of the whole company. Take the platform problem that's hurting users/brand even if it didn't originate on your team.
- **Lives in:** 533M scraping/enumeration defense (TOS→cyber-defense pivot), WA Integrity ($235M risk).
- **Maps to:** Amazon *Ownership* / *Dive Deep* · Google *Ownership* · Meta *Nothing is someone else's problem*.

---

## Principle → Company Rubric Master Map

| Vikash Principle | Amazon LP | Google Signal | Anthropic Lens | Meta Signal |
|---|---|---|---|---|
| P1 Shocks→infrastructure | Think Big; Invent & Simplify | Strategic / 10x thinking | Ambitious, careful | Durable systems |
| P2 Map incentives first | Earn Trust; Have Backbone | Googleyness / collaboration | Honest, low-ego | Cross-boundary |
| P3 Measure w/o collecting | Invent & Simplify; Highest Standards | Analytical rigor | Do the hard thing right | Privacy by design |
| P4 Reversibility sort | Bias for Action; Are Right, A Lot | Execution / judgment | Calibrated decisions | Move fast, stable infra |
| P5 Options not problems | Deliver Results; Ownership | Drive / problem-solving | Pragmatic | Bias to impact |
| P6 Compliance = trust | Customer Obsession; Broad Responsibility | Trust & Safety | Safety as product | Responsible scaling |
| P7 Transparency > black box | Are Right, A Lot; Earn Trust | Open ecosystems | Transparency / interpretability | Openness |
| P8 Educate the industry | Hire & Develop; Earth's Best Employer | Thought leadership | Field-building | Scale through others |
| P9 Ask for help; process | Ownership; Learn & Be Curious | Managing scale | Self-aware | Org leadership |
| P10 Own the gap | Ownership; Dive Deep | Ownership | Extreme ownership | Nothing is not-my-job |

> **Note on Amazon's 16 LPs:** the full LP→story map already exists at `users/vikash/stories/amazon_leadership_principles.md`. Use it as the authoritative Amazon plug-in; this table is the cross-company synthesis.

## Coaching rules for closes
- The **close** is what sticks. Each Story should have a *different* close per Principle lens — see `the_saga_method.md` Part 3 "One Story, three lenses."
- Keep the close to one or two sentences. State the principle as belief, then the durable effect: *"That's why I treat every compliance mandate as a trust opportunity — the fairness infra we built became a moat competitors still have to replicate."*
- Never bolt a Principle on after the fact. If the Story's actions don't actually demonstrate the Principle, pick a different Principle or a different Story.
