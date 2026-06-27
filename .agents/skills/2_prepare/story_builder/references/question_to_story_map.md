# Question → Story Map (Demand Side)

> Reference for `story_builder`. Given a behavioral question, which Saga/Epic/Story to grab — and
> which Principle lens to tell it through. The operational form of the Saga Method's "Their Side."
> Authoritative keyframe inventory lives in `users/vikash/stories/11_story_to_pillar_mapping.md`; this
> is the question-first index derived from it.

## The 6 Question Categories → grab list

| Category | Prompt shape | Strongest keyframe (Saga · Epic · Story) | Backup | Default lens |
|---|---|---|---|---|
| **Conflict / Disagreement** | "...disagreed with a partner/leader" | WhatsApp · MM · *Ads-team attribution conflict* | RAI · VRS · *Policy-vs-Eng on "variance"* | P2 Map incentives / Have Backbone |
| **Failure / Mistake** | "...something went wrong, your fault" | Growth · Friend Graph · *"Ask for help sooner"* | RAI · PETs · *Hiring failure + slow proposals* | P9 Ask for help / Learn & Be Curious |
| **Ambiguity / Strategy** | "...decide with little data / 0→1" | MSL · Llama · *"Safety for open weights"* | RAI · PETs · *W3C PATCG formation* | P1 Shocks→infra / Think Big |
| **Execution / Grit** | "...deliver under pressure" | RAI · VRS · *HUD deadline (91.7%/<10%)* | WhatsApp · MM · *Holiday WCA crunch* | P5 Options not problems / Deliver Results |
| **Technical Bet / Judgment** | "...a technical call you owned" | RAI · VRS · *BISG demographic inference* | RAI · PETs · *MPC architecture* | P3 Measure w/o collecting / Invent & Simplify |
| **Leadership / Influence** | "...influenced without authority" | RAI · PETs · *Mozilla partnership* | MSL · *GenAI Bootcamp 800+ PMs* | P8 Educate the industry / Earn Trust |

> Sagas: **WhatsApp** = Click-to-Message Monetization · **RAI** = Responsible & Private AI · **MSL** = Frontier Model Safety · **Growth** = Real-World Identity · **Founder** = eLagaan/LawGro.

## The "5 Essential Stories" coverage
| Essential | Keyframe |
|---|---|
| Turnaround / Ownership | Friend Graph — "Ask for help" → stabilized 38-person team |
| 0→1 / Drive | Llama — Purple Llama launch · or PETs — IPA/W3C |
| People Crisis / Leadership | Friend Graph — stretched team / hiring gap |
| Contrarian Bet / Conviction | Llama — open-weights safety strategy · or VRS — BISG bet |
| Hard Failure / Resilience | PETs — hiring failures + slow proposal release |

## The Read (before you pick)
Per `the_saga_method.md` Step 2, a single category can be probing different things. Decide which by company (use the `companies/{name}/` dossier and `principle_library.md` rubric map):
- A **Conflict** question may test conviction (*Have Backbone*), empathy (*Earn Trust*), or pragmatism (*Invent & Simplify*). Pick the lens the role rewards.
- **Amazon** → map every answer to an LP, use "I"; **Google** → coalition-building + frameworks + 10x; **Meta** → speed, iteration, quantify; **Anthropic** → safety conviction + intellectual honesty.

## Coverage gaps (generate carefully — don't fabricate)
From `11_story_to_pillar_mapping.md`, these pillars are thin. If a question targets them, surface the gap and ask Vikash for a real moment rather than inventing one:
- **Sense (P2 pillar)** — design-critique / user-empathy story. *Open gap.*
- **Metrics (P4 pillar)** — A/B-test / metric-drop-debug story. *Open gap.*
- **Management (P5 pillar)** — hiring-bar / team-scaling depth beyond the 38-person anecdote. *Limited.*

## How the builder uses this file
- **"Give me a conflict story for Amazon"** → grab MM attribution conflict, lens = Have Backbone (P2), map to Amazon LP, render STAR+ with pushback.
- **"What do I tell for a 0→1 question at Anthropic?"** → Purple Llama keyframe, lens = P7 transparency, Anthropic safety framing.
- **"Where am I thin?"** → report the coverage gaps above + any Principle in the Lookup View with only one Story.
