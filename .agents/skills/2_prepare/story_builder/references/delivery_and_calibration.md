# Delivery & Calibration

> Reference for `story_builder`. How a generated Story is *told* — format, timing, seniority calibration,
> and surviving pushback. The Saga Method's "Step 5: Deliver." Pairs with `principle_library.md` (the lens).

## Delivery formats (pick per Story; default STAR+)

| Format | Structure | Best for |
|---|---|---|
| **STAR+** | Situation → Task → Action → Result → **Leadership Reflection** | Default. Structured, safe, universally understood. The `+` is the Principle close. |
| **Freytag** | Exposition → Rising Action → Climax → Falling Action → Resolution | High-drama conflict/crisis stories where tension is the point (e.g., 533M scraping incident). |
| **DIGS** | Dramatize → Indicate alternatives → Go through what you did → Summarize impact | Leading with stakes; good when the alternatives considered are the impressive part (the tradeoff stories). |

Every generated Story should render in **STAR+ by default**, and note which alternate format suits it.

## Senior timing (IC7 / D1 — the time budget)
From `framework/10_story_building_strategy.md`. Most candidates over-invest in Situation and under-invest in Action.

| Beat | % of airtime | The question it answers |
|---|---|---|
| Situation | ~10% | "Why does this matter?" (stakes, in one or two lines) |
| Task | ~10% | "What was **my** specific mandate?" (not the team's) |
| Action | ~60% | "What did **I** do?" — strategy, influence, execution. The substance. |
| Result | ~20% | "So what?" — metrics, second-order effects, the moat |
| + Reflection | one line | The Principle. What this proves about how you operate. |

## IC7/D1 calibration (weak → strong)
The same event told at the wrong altitude reads as mid-level. Calibrate every generated Story up:

| Dimension | IC5/IC6 (weak) | IC7/D1 (strong) |
|---|---|---|
| Ownership | "The project was delayed due to Eng resourcing." | "I underestimated integration complexity, we were 6 weeks late, I owned it and reframed our API as a defensive moat to get the VP to prioritize it." |
| Voice | "We" for everything | "I" for the decision and the influence; "we" for the team's execution |
| Influence | "I asked them to prioritize it" | "I mapped their incentives, pre-wired the stakeholders, and let the data settle the room" (see Influence Playbook) |
| Result | "It improved engagement" | "D7 retention +18%; became the foundation for three later features" |
| Scope | one feature | org/system/industry-level second-order effects |

**Anti-patterns to strip:** blaming Eng/Design/Legal; "participated" instead of "led"; failures with no learning; outcomes that are merely "satisfactory" (D1 needs exceptional); buzzwords.

## The Influence Playbook (use in Action beats for conflict/leadership stories)
1. **Incentive mapping** — what does the other side gain? (Principle P2)
2. **Coalition building** — who influences the influencer? Pre-wire them.
3. **Data as neutral ground** — let the numbers settle the emotion.
4. **Pre-wiring** — no one is surprised in the big meeting.

## Surviving pushback (the exemplar bar)
`users/vikash/stories/sample_interview_tradeoff.md` shows the standard: an answer that holds up through three escalating challenges. Every generated Story should ship with a **"Likely pushback" section** anticipating:
- **Process probes** — "Walk me through that exact conversation. What did they say?"
- **Value challenges** — "How do you justify delivering less to users short-term?"
- **Bias tests** — "Did you already decide before that meeting and work backward?"

What survives pushback (from the exemplar): specific quotes and numbers; showing the genuine alternative you considered; admitting uncertainty and your own bias; ending with what you'd do differently — *without* collapsing the conviction (PMs are paid to have a point of view).

## The 5 Essential Stories (ensure the bank covers all five)
Every IC7/D1 bank needs these; map each to a real keyframe (existing mapping in `11_story_to_pillar_mapping.md`):
1. **Turnaround / Ownership** — fix an inherited mess.
2. **0→1 / Drive** — value from absolute ambiguity.
3. **People Crisis / Leadership** — XFN standoff or team-morale collapse.
4. **Contrarian Bet / Conviction** — go against consensus with judgment.
5. **Hard Failure / Resilience** — high-stakes loss, owned, applied to the next win.

If a generated bank is missing one of the five, flag it as a coverage gap.

## Communication tactics (apply to the hook + delivery)
- **BLUF** — answer first (the 10-second hook), explain second.
- **Minto Pyramid** — conclusion → key points → detail.
- **Quantify** — replace every adjective of impact with a number where one is traceable.
- **Close strong** — "Does that answer it, or should I go deeper on the [X] decision?"
