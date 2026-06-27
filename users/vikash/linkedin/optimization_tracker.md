# LinkedIn Optimization — Vikash Rungta
> Exact actions + copy-paste text. Work through top to bottom.
> Grounded in [SKILL.md v5.0](file:///Users/vikashrungta/code/tomo/.agents/skills/linkedin_optimizer/SKILL.md) — the 5-layer pipeline architecture.

> ⚠️ **BATCH ALL CHANGES IN ONE SESSION.** LiRank's Multi-Armed Bandit allocates one exploration window per major profile update. If you trickle changes over 2 weeks, you get several weak exploration windows with only partial optimization live. If you batch everything into one sitting (~2 hours), you get one strong exploration window with your fully optimized profile — maximizing the chance of high CTR during exploration → persistent high ranking.

---

# LAYER 1: HARD FILTERS (pass/fail — if you fail here, no ML model ever evaluates you)

---

## Action 1: Clean Up Experience Titles `[L1 — JAMES Taxonomy]`

Go to: **LinkedIn → Profile → Experience → Senior Product Manager (AI) at Meta → Edit**

In the **Title** field, clear what's there and start typing `Senior Product Manager`. **Pick "Senior Product Manager" from the LinkedIn autocomplete dropdown** — don't free-type it.

**Why (JAMES model — 3 embedding layers):**
LinkedIn maps every free-text title to a canonical **Taxonomy Entity ID**. Picking from the dropdown locks in the exact entity, bypassing the fuzzy NLP pipeline. Free-typing a custom string (like adding parentheticals) forces the model to guess across 350,000+ unique titles using syntactic + semantic + topological embeddings — risking seniority misclassification.

**Don't add parentheticals or custom text to the title field.** Scope belongs in the **first line of the description** (see Action 7).

> 💡 Your strongest title at Meta ("Head of Product" from 2021-2024) validates Director-level seniority. Your headline (Action 5) says "Head of Product" — that's the click-through hook. The Experience title just needs clean taxonomy mapping.

**Do this for every Meta role:**
- `[ ]` Senior Product Manager → pick from dropdown
- `[ ]` Lead Product Manager → pick from dropdown
- `[ ]` Head of Product → pick from dropdown
- `[ ]` Product Lead → pick from dropdown (if it appears; otherwise "Product Manager")
- `[ ]` Course Instructor → pick from dropdown

- `[ ]` Done

---

## Action 15: Stack Meta Roles `[L1 — JAMES Poincaré Trajectory]`

> ⚠️ Reordered before other actions because this is a Layer 1 hard signal. Do it now while you're editing titles.

Go to: **LinkedIn → Profile → Experience**

Make sure all Meta roles appear **under one "Meta" company entry** with each role shown as a sub-position:
```
Meta (6 years)
  ├─ Senior Product Manager              (2024–2025)
  ├─ Lead Product Manager                (2023–2024)
  ├─ Head of Product                     (2021–2024)
  ├─ Product Lead                        (2019–2021)
  └─ Course Instructor                   (2022–2025)
```

**Why (JAMES — Job Transition Graph):**
LinkedIn's JAMES model builds a directed graph from 2.7M+ career transitions, embedded in Poincaré hyperbolic space. When stacked under one company, the algorithm traces: `Product Lead → Head of Product → Lead PM → Senior PM` as a directed promotion path. This mathematically increases your inferred seniority score. Separate company entries break the graph — each role looks lateral, not promoted.

If roles are listed as separate company entries, edit each one and set "Company" to the same "Meta" page.

- `[ ]` Done

---

## Action 16: Update Skills `[L1 — Skills Graph Hard Filter]`

Go to: **LinkedIn → Profile → Skills → Edit**

**Why skills are a Layer 1 gate:** Recruiters filter by Skills in LinkedIn Recruiter. If "Agentic AI" isn't in your skills list and a recruiter has it as a filter, you're invisible. Skills from old industries (FPGA, VHDL) act as **hard negatives** in the Two-Tower DNN — they pull your embedding away from AI PM jobs.

**PIN these 3** (reorder so they appear first):
1. `Product Strategy`
2. `Generative AI`
3. `Cross-Functional Team Leadership`

**ADD these** — type into "Add skill" and **select from autocomplete** (same taxonomy principle as titles):
- `[ ]` Agentic AI
- `[ ]` AI Safety
- `[ ]` Responsible AI
- `[ ]` Model Alignment
- `[ ]` First-Principles Thinking
- `[ ]` Foundation Models
- `[ ]` Large Language Models (LLMs)
- `[ ]` Python
- `[ ]` SQL
- `[ ]` Developer Tools
- `[ ]` API Design
- `[ ]` Red-Teaming
- `[ ]` Go-to-Market Strategy
- `[ ]` P&L Management
- `[ ]` Privacy Enhancing Technologies
- `[ ]` Stakeholder Management

> 💡 **Skill adjacency (Skills Graph):** Listing "Model Alignment" automatically associates "RLHF," "AI Safety," and "Red-Teaming" at reduced weight. You don't need to list every variant — anchor skills expand coverage.

**REMOVE these** (click ✕ next to each):
- `[ ]` FPGA
- `[ ]` VHDL
- `[ ]` RTL Design
- `[ ]` ASIC Design
- `[ ]` Any other semiconductor/hardware-specific skills

- `[ ]` Done

---

# LAYER 4: CANDIDATE CARD (the 6-second decision — what recruiters actually see)

---

## Action 2: Enable "Open to Work" (private mode) `[L4 — Spotlight Filter #1]`

Go to: **LinkedIn → Profile → "Open to" button → "Finding a new job"**

Set visibility to: **Recruiters only** (NOT the public green badge)

Add these job titles:
```
Director of Product Management
Head of Product
Principal Product Manager
Group Product Manager
VP of Product
```

Location: `San Francisco Bay Area`
Start date: `Immediately`

**Why (Recruiter Workflow):** "Open to Work" is the #1 Spotlight filter. Recruiters click it BEFORE scrolling results because OTW candidates have a 3x higher response rate, letting them hit sourcing quotas faster. Without it, you're in the "All Candidates" tab, which most recruiters don't open.

- `[ ]` Done

---

## Action 3: Verify Your Identity `[L4 — Spotlight Filter + Ranking Boost]`

Go to: **LinkedIn → Settings → Account → Verification**

Complete verification with government ID or workplace email. This gives you the "Verified" badge.

**Why (Fairness Audit paper):** The Verified badge is both a Spotlight filter AND a ranking feature. Recruiters can filter for "Verified Applicants" only. The audit confirmed that profile completeness signals (including verification) correlate with higher ranking because they produce higher-confidence embeddings.

- `[ ]` Done

---

## Action 4: Follow Target Companies `[L4 — Spotlight + L3 — LinkSAGE GNN]`

Search for and click "Follow" on each:
- `[ ]` Anthropic
- `[ ]` OpenAI
- `[ ]` Google DeepMind
- `[ ]` Nvidia
- `[ ]` Apple
- `[ ]` Netflix
- `[ ]` Uber
- `[ ]` Microsoft
- `[ ]` Intuit
- `[ ]` DoorDash

**Dual purpose:**
1. **Layer 4 (Spotlight):** Triggers the "Engaged with Talent Brand" Spotlight — same visibility tier as "Open to Work"
2. **Layer 3 (LinkSAGE GNN):** Following + connecting with people at these companies shifts your graph neural network embedding closer to their job postings, even if your keywords don't perfectly match

---

## Action 5: Replace Headline `[L4 — Candidate Card CTR → LiRank MAB]`

Go to: **LinkedIn → Profile → Edit intro → Headline**

Delete current headline and paste one of these.

**Why headline is critical (LiRank MAB):** The headline is the ONLY free-text field on the Candidate Card. During LiRank's exploration window (triggered by your batch update), your card CTR determines whether you graduate to persistently high ranking or get suppressed. A weak headline = low CTR during exploration = permanently depressed ranking until the next major update.

Leading with **"Head of Product"** because it accurately reflects the highest level you operated at within Meta, maps to Director-level in the taxonomy, and signals ownership over management.

**OPTION A (recommended):**
```
Head of Product | AI Platforms & Foundation Models | 3B+ Users, 0-to-1 Builder
```

**OPTION B (if targeting Anthropic/OpenAI specifically):**
```
Head of Product | Model Alignment, AI Safety & Agentic Systems | Shipped Llama
```

**OPTION C (if leading with educator angle):**
```
Head of Product | GenAI Infrastructure | Built Llama Alignment + Trained 800 PMs to Ship AI
```

- `[ ]` Done — chose option: ___

---

# LAYER 2 + 5: EMBEDDING QUALITY + FULL PROFILE (what they see after clicking the card)

---

## Action 6: Replace About Section `[L2 — Skill Extraction + L5 — Post-Click Validation]`

Go to: **LinkedIn → Profile → About → Edit**

Delete everything. Paste this:

```
Built Llama's alignment stack at Meta — the safety guardrails and governance framework that made it the most deployed open-source LLM for enterprise. Before that, shipped WhatsApp AI for Business and built Meta's Responsible AI org from scratch. Two-time co-founder (eLagaan: 30K customers, multimillion-dollar revenue; LawGro: vertical SaaS).

I bring founder-grade urgency to large organizations. I also created Meta's GenAI Bootcamp, taken by 800+ PMs — because the next generation of product leaders need to build with AI, not just manage it.

Looking for Head of Product/Director roles at AI-native companies building foundation models, agentic systems, or developer platforms.
```

**Why (Skills Graph BERT extraction):** LinkedIn's BERT-based models extract skills from your prose, not just your Skills list. This text triggers extraction for: model alignment, governance, agentic systems, foundation models, developer platforms. "Built red-teaming frameworks" triggers the Red-Teaming skill; "tested the model" does not.

- `[ ]` Done

---

## Action 7: Rewrite Experience — Llama Role `[L2 — Embedding + L4 — Card Position #1]`

Go to: **LinkedIn → Profile → Experience → "Senior Product Manager" at Meta → Edit**

Delete the current description. Paste this:

```
Led product strategy for Llama's model alignment organization — defining the safety guardrails, model behavior standards, and governance frameworks for Meta's foundational LLM. Cross-functional with ML research, infrastructure, trust & safety, and policy.

• Architected the multi-layer guardrails framework that positioned Llama as the most trusted open-source LLM for enterprise deployment
• Designed the product specification for secure autonomous agent deployment — a 0-to-1 surface enabling agentic AI workflows with safety guarantees
• Created "Generative AI Bootcamp for PMs" — adopted by 800+ product managers at Meta, and "Foundation of AI" training taken by 7,500+ PMs
```

**Keywords embedded for BERT extraction:** model alignment, model behavior, safety guardrails, governance, autonomous agent, agentic AI, 0-to-1, cross-functional, foundation models

- `[ ]` Done

---

## Action 8: Rewrite Experience — WhatsApp Role `[L2 — Embedding + L4 — Card Position #2]`

Go to: **LinkedIn → Profile → Experience → "Lead Product Manager" at Meta → Edit**

Delete the current description. Paste this:

```
Owned AI product strategy for WhatsApp Business — integrating generative AI capabilities into the messaging platform serving 200M+ business accounts globally.

• Defined the product vision for AI-powered business interactions — enabling automated customer engagement, intelligent responses, and content generation for SMBs
• Shipped in a fast-moving, ambiguous environment with direct impact on WhatsApp's monetization trajectory
```

- `[ ]` Done

---

## Action 9: Rewrite Experience — Responsible AI Role `[L2 — Embedding + L4 — Card Position #3]`

Go to: **LinkedIn → Profile → Experience → "Head of Product" at Meta → Edit**

Delete the current description. Paste this:

```
Directed Meta's Responsible AI product organization — a 0-to-1 charter building the safety, privacy, and fairness infrastructure for all GenAI monetization systems. Led cross-functional execution across ML research, data science, legal, and policy.

• Built the Responsible AI product stack from scratch: red-teaming frameworks, model safety interventions, and fairness evaluation pipelines for GenAI-powered ads
• Re-architected ad targeting for Housing, Employment & Credit (HEC) — the most federally regulated ad categories — addressing DOJ/HUD regulatory pressure and protecting billions in at-risk ad revenue
• Shipped Privacy Enhancing Technologies (PETs) enabling ads personalization without compromising user privacy — a strategic unlock for Meta's post-ATT recovery
```

**Keywords embedded:** Responsible AI, 0-to-1, red-teaming, model safety, fairness, privacy enhancing technologies, cross-functional, regulatory

- `[ ]` Done

---

## Action 10: Rewrite Experience — Real World Identities Role `[L2 — Embedding]`

Go to: **LinkedIn → Profile → Experience → "Product Lead" at Meta → Edit**

Delete the current description. Paste this:

```
Owned the cross-app identity platform spanning Facebook, Messenger, Instagram, and WhatsApp — connecting 3B+ users' digital presence to real-world relationships and devices.

• Built the Real World Friend Graph (0→1): privacy-preserving ML signals powering friend recommendations tied to measurable DAU engagement gains
• Shipped the People-to-Device Graph: canonical user-to-device mapping across all Meta apps, reducing account compromise and improving new-device onboarding
```

- `[ ]` Done

---

## Action 11: Rewrite Experience — Course Instructor Role `[L2 — Embedding]`

Go to: **LinkedIn → Profile → Experience → "Course Instructor" at Meta → Edit**

Delete the current description. Paste this:

```
Created and taught three internal programs training Meta's PM organization on AI:
• "GenAI Bootcamp for PMs" — 800+ graduates
• "Foundation of AI" — AI product fundamentals (PMx org)
• "PM Interview Q&A" — 7,500+ participants, Meta's largest PM education program
```

- `[ ]` Done

---

## Action 12: Rewrite Experience — eLagaan `[L2 — Embedding]`

Go to: **LinkedIn → Profile → Experience → "Co-Founder" at eLagaan → Edit**

Delete the current description. Paste this:

```
Co-founded a SaaS fintech startup — "TurboTax for India" — in a market with zero digital tax filing infrastructure. Built product and engineering team from zero. Acquired 30,000 paying customers in 3 years, generating multimillion-dollar revenue.
```

- `[ ]` Done

---

## Action 13: Rewrite Experience — LawGro `[L2 — Embedding]`

Go to: **LinkedIn → Profile → Experience → "Chief Product Officer" at LawGro → Edit**

Delete the current description. Paste this:

```
Co-founded a vertical SaaS product for law firm operations. End-to-end ownership: product vision, engineering, go-to-market. Took product from concept to paying customers.
```

- `[ ]` Done

---

## Action 14: Rewrite Experience — Infinera `[L2 — Embedding]`

Go to: **LinkedIn → Profile → Experience → "Lead Product Manager" at Infinera → Edit**

Delete the current description. Paste this:

```
Owned end-to-end product strategy for network automation at a public telecom infrastructure company ($INFN). Products deployed by cloud providers and ISPs globally. Defined and executed Go-To-Market strategy. Built the "Cognitive Network" vision — a self-driving, self-healing network (0-to-1 in telecom AI).
```

- `[ ]` Done

---

# LAYER 3: RANKING SIGNALS (how you're ordered in the candidate pool)

---

## Action 17: Request Endorsements `[L3 — GLMix Social Proof]`

Send a message to 3-5 credible connections asking them to endorse you for:
1. Product Strategy
2. Generative AI
3. Cross-Functional Team Leadership

Good candidates: VP/Director of Eng you worked with, a GPM-level peer, an ML researcher, a direct report.

Template message:
```
Hey [name] — I'm updating my LinkedIn and would really appreciate if you could endorse 
me for Product Strategy, Generative AI, and Cross-Functional Team Leadership. Happy to 
return the favor. Thanks!
```

- `[ ]` Done

---

## Action 18: Pin a Featured Item `[L5 — Feed GR + Post-Click Signal]`

Go to: **LinkedIn → Profile → Featured → Add**

Pin your single strongest thought-leadership artifact:
- A Substack article from vrungta.substack.com (ideally on Agentic AI or Llama)
- OR a public mention of Stanford BUS 190
- OR the GenAI Bootcamp if it has a public writeup

Only pin 1-2 items. If nothing strong exists, skip this.

**Why (Feed GR):** Pinned content acts as a persistent high-signal artifact that the Generative Recommender references for topic embedding. It also gives post-click visitors a concrete proof of thought leadership.

- `[ ]` Done

---

## Action 19: Reply to All Pending InMails `[L3 — GLMix Per-Candidate Coefficient]`

Go to: **LinkedIn → Messaging → Filter by InMail**

Reply to every unanswered InMail, even if declining:
```
Thanks for reaching out — not the right fit right now but I appreciate you thinking of me.
```

**Why (GLMix + Recruiter AI):** InMail response rate is tracked as a per-candidate feature. Your responsiveness feeds directly into your GLMix coefficients — consistent responsiveness = higher future ranking for all recruiters. This is not politeness. It's a ranking input.

- `[ ]` Done

---

# ✅ Completion Checklist

**Organized by pipeline layer. Do all in one session for maximum MAB exploration window impact.**

| # | Layer | Action | Status |
|---|---|---|---|
| **HARD FILTERS (L1)** | | | |
| 1 | L1 | Clean up all titles via dropdown (JAMES) | `[ ]` |
| 15 | L1 | Stack Meta roles under one entry (Poincaré) | `[ ]` |
| 16 | L1 | Update skills — add/remove/pin (Skills Graph) | `[ ]` |
| **CANDIDATE CARD (L4)** | | | |
| 2 | L4 | Enable Open to Work — private (Spotlight #1) | `[ ]` |
| 3 | L4 | Verify identity (Spotlight + ranking) | `[ ]` |
| 4 | L4 | Follow 10 target companies (Spotlight + GNN) | `[ ]` |
| 5 | L4 | Replace headline — Head of Product (MAB CTR) | `[ ]` |
| **EMBEDDING + PROFILE (L2/L5)** | | | |
| 6 | L2/L5 | Replace About (BERT extraction + validation) | `[ ]` |
| 7 | L2/L4 | Rewrite Llama role (Card Position #1) | `[ ]` |
| 8 | L2/L4 | Rewrite WhatsApp role (Card Position #2) | `[ ]` |
| 9 | L2/L4 | Rewrite Responsible AI role (Card Position #3) | `[ ]` |
| 10 | L2 | Rewrite Real World Identities | `[ ]` |
| 11 | L2 | Rewrite Course Instructor | `[ ]` |
| 12 | L2 | Rewrite eLagaan | `[ ]` |
| 13 | L2 | Rewrite LawGro | `[ ]` |
| 14 | L2 | Rewrite Infinera | `[ ]` |
| **RANKING SIGNALS (L3)** | | | |
| 17 | L3 | Request endorsements (social proof) | `[ ]` |
| 18 | L5 | Pin Featured item (Feed GR) | `[ ]` |
| 19 | L3 | Reply to all InMails (GLMix coefficient) | `[ ]` |

**Total estimated time: ~2 hours in one session.**
