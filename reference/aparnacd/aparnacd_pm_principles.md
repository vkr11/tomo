# Aparna Chennapragada — PM Interview Principles

> Extracted from 22 posts at aparnacd.substack.com

---

## 1. The Bitter Lesson (Product Version): Learning Loops Beat Designed UX

**One-liner:** Handcrafted UX doesn't compound — products built to *learn* from every interaction will eventually eclipse even the most polished designed experiences.

**Sources:** *The Bitter Lesson: Product Version*, *Design for Learning*

**The Insight:** Aparna extends Richard Sutton's AI research observation to product design: just as hand-engineered AI systems always lost to methods that learn at scale, products built on static UX will lose to ones designed with learning loops. "When the model IS the product, all UX is RLHF." Every click, tab-press, or edit should teach the system. She distinguishes two loops: the **feedback loop** (user interaction → model improvement) and the **evaluation loop** (verifying improvement actually happened).

**Interview Application:** When asked "How would you design an AI product?" or "How do you think about product iteration?" show that you think beyond launch-day UX to long-term learnability. Explain how every user interaction is a training signal.

**Example Phrasing:** "I designed the interaction so every accept or edit on an AI suggestion became a learning signal. Rather than polishing a static flow, I invested in feedback loops that made the product dramatically better by month three than it was at launch."

---

## 2. Prompt Sets Are the New PRDs

**One-liner:** Traditional PRDs were written for programmers; prompt sets are living specifications that encode human intent, teach the system, and evolve through iteration.

**Sources:** *Prompt Sets Are the New PRDs*, *Just-in-Time Content*

**The Insight:** Aparna argues the old spec-then-build waterfall is dead for AI products. Instead, PMs should write "prompt sets" — collections of natural-language prompts that capture how a human colleague would ask for this work. Good prompts encode *judgment and priorities* ("tell me the key risks and sentiment trend"), not mechanical instructions ("summarize in 5 bullets"). Writing prompts is "less like drafting a rigid contract and more like coaching."

**Interview Application:** When asked about your product development process for AI features, describe how you iterate through prompt sets instead of writing static requirements documents.

**Example Phrasing:** "Instead of a traditional PRD, I wrote a set of 20 prompts that captured how a real user would naturally ask for this output. We iterated through three rounds — each round revealed where the agent fell short, and we refined the prompt set like a curriculum."

---

## 3. Most Work Is Translation — LLMs as the Universal Translator

**One-liner:** Only 39% of the workday is spent on core job duties; the rest is translation — and AI is collapsing that cost to near zero.

**Sources:** *Most Work Is Translation*, *Every Maker Is Now a Manager (of AI)*

**The Insight:** Aparna's most provocative structural observation: organizations are pyramids because *translation is expensive*. Middle layers exist to carry the cost of converting information between forms. When LLMs make translation near-free (paper → brief, meeting → memo, data → chart), the pyramid collapses into a backbone. For individuals: less time producing artifacts, more time judging fidelity. For orgs: smaller, leaner teams can now coordinate at scale.

**Interview Application:** When asked "How would you improve team efficiency?" or "How does AI change the PM role?" frame your answer around reducing translation overhead, not just "using AI tools."

**Example Phrasing:** "I realized our team spent 60% of their time translating information between formats — engineer status into PM decks, PM decks into exec briefings. I introduced AI-assisted summarization at each handoff point, which compressed our weekly reporting cycle from 3 days to 3 hours."

---

## 4. The WOW:WTH Ratio — Designing for Recovery

**One-liner:** Every WTH moment undoes the trust built by several WOWs — and how you design for failure depends on the stakes and autonomy of your product.

**Sources:** *What's Your WOW:WTH Ratio*, *Designing for Trust*, *The Legibility and Control Trap*

**The Insight:** Aparna introduces a 2x2 framework of **Autonomy** (how freely the system acts) × **Stakes** (how much it matters if it's wrong). Low stakes/low autonomy: ship fast, small WTHs don't matter. High stakes: WTHs must be *reviewable* (show reasoning). High autonomy: WTHs must be *reversible* (one-click undo). High stakes + high autonomy: "a WTH is basically an incident" — you need incident-response plans. Designing for trust means caring as much about how a system fails as how it shines.

**Interview Application:** When asked "How do you think about risk in AI products?" or "How do you build trust with users?" use the Autonomy × Stakes framework to show sophisticated AI product thinking.

**Example Phrasing:** "I categorized our agent features along two axes: autonomy and stakes. For high-stakes outputs, I added reasoning traces so users could verify before acting. For high-autonomy actions, I made every operation reversible with one click. This reduced our support tickets by 40%."

---

## 5. The Six Finger Trap — Don't Over-Engineer for Temporary Limitations

**One-liner:** Don't invest significant resources solving a model limitation that will be fixed upstream in the next release — build for where the model puck is going.

**Sources:** *Beware the Six Finger Trap*, *The Bitter Lesson: Product Version*

**The Insight:** Early AI image models gave people six fingers. Teams built elaborate workarounds. Then the next model version just... fixed it. Aparna warns against this pattern: "Today's limitation becomes tomorrow's solved problem." Her antidote: (1) Do the wait calculation — is this a temporary quirk or a fundamental design constraint? (2) Build architectures that swap models in and out so today's workarounds don't become tomorrow's technical debt.

**Interview Application:** When asked "How do you make product decisions under uncertainty?" or for an AI product strategy case, demonstrate that you think about *model trajectory*, not just current capabilities.

**Example Phrasing:** "We were about to build an elaborate post-processing pipeline to fix hallucinations in a specific domain. I argued we should wait — the next model update was 6 weeks away and would likely solve it upstream. Instead, we invested that engineering time in the feedback loop, which was durably valuable."

---

## 6. All Leaders Are GPT-5s — Balancing Reasoning and Execution

**One-liner:** Leaders dynamically route challenges into reasoning (exploration) or execution (scaling playbooks) — the art is knowing when to rebalance and how fast to distill insights into repeatable processes.

**Sources:** *All Leaders are GPT-5s*, *The Latent Long Tail of Ideas*

**The Insight:** Using Andy Grove's Skill/Will framework as a foundation, Aparna extends it to the organization level through an AI metaphor: companies are "mixtures of models" — some people are instruction-followers (fast, disciplined) and others are reasoners (slower, navigating ambiguity). The leader's job is to act like GPT-5: routing to the right mode. Critical concept: **distillation velocity** — how quickly insights from reasoning teams become executable playbooks for the broader org. Too slow = drowning in exploration. Too fast = ossifying half-baked ideas.

**Interview Application:** When asked "How do you balance innovation with execution?" or "How do you scale a team?" use the reasoning vs. execution framing and explain how you manage distillation velocity.

**Example Phrasing:** "I think of my team as a mixture of reasoners and executors. When we were pre-PMF, I tilted toward reasoning — small team, lots of exploration. Once we found signal, I focused on distillation: converting the experimental insights into repeatable playbooks that the broader team could run independently."

---

## 7. Every Maker Is Now a Manager (of AI)

**One-liner:** Working with AI agents pulls makers into manager mode — high responsibility with low execution control — which is cognitively draining unless we design calmer human-AI interfaces.

**Sources:** *Every Maker Is Now a Manager (of AI)*, *Prompt Sets are the New PRDs*

**The Insight:** Paul Graham's maker/manager schedule distinction is collapsing. Makers using AI agents spend more time reviewing outputs and deciding where to intervene than doing deep creative work. Aparna frames this through Karasek's Demand-Control model: stress increases when responsibility stays high but control over execution decreases. Her solution: design AI interactions like working with "a high-performing colleague" — well-scoped work, batched questions, updates at natural breakpoints, artifacts instead of running commentary.

**Interview Application:** When asked "How do you see AI changing the PM role?" or "What's your biggest concern about AI in the workplace?" demonstrate nuanced understanding that AI doesn't just save time — it reshapes the *texture* of work.

**Example Phrasing:** "I noticed my team was spending more time supervising AI outputs than doing deep work. I restructured our workflow so the AI delivered completed drafts at checkpoints rather than streaming partial results, which restored the maker schedule for our designers."
