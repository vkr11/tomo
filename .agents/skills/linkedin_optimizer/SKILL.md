---
name: linkedin_optimizer
description: >
  Optimize LinkedIn profiles for maximum recruiter inbound and feed visibility using evidence-based strategies.
  Trigger on: "optimize my LinkedIn", "improve my LinkedIn profile", "LinkedIn headline", "LinkedIn about section",
  "LinkedIn skills", "get more recruiter inbounds", "LinkedIn algorithm", "LinkedIn SEO", "profile review",
  "rewrite my headline", "what skills should I add", or any request about LinkedIn discoverability.
  Also supports: generating LinkedIn posts/content strategy, preparing for a specific company target,
  and auditing a live profile against active JDs.
---

# LinkedIn Profile Optimizer v4.0

## Skill Architecture

This skill has three layers. Use the right one for the request.

```
Layer 1: STRATEGY    — The "why" behind every recommendation (this file)
Layer 2: CONTEXT     — Vikash's specific positioning, keywords, arcs (./vikash_context/)
Layer 3: REFERENCES  — Raw engineering papers and blog captures (./references/)
```

When invoked:
1. Read `./vikash_context/linkedin_core_identity.md` for current positioning and target domains.
2. Read `./vikash_context/keyword_critique.md` (in `keywords/`) for the grounded keyword tiers per company archetype.
3. Read `./vikash_context/linkedin_platform_checklist.md` for the current implementation status.
4. Only consult `./references/` when you need to verify a specific algorithmic claim.

Do NOT ask for target roles or constraints unless the user explicitly says they're switching domains.
The default context is already loaded.

---

## Part 1: How LinkedIn Actually Works (The Machine)

### Two systems, zero overlap

LinkedIn runs two independent algorithmic systems. Most advice conflates them. Never do.

**System 1 — Recruiter Search (gets you found by hiring managers)**

The pipeline that determines whether a recruiter sees your profile at all:

- **L1 Retrieval (Galene/Lucene):** Boolean term matching as a hard gate. Your profile text is indexed into inverted fields. If the recruiter's query terms don't appear in your profile, you're invisible. This is still the first filter—semantic search hasn't replaced it, it augments it.
- **L1→L2 Ranking (Two-Tower DNN):** 128-dimensional embeddings trained on 150M+ engagement records. Cosine similarity between your profile embedding and the job/query embedding. Unrelated content in your profile acts as "hard negatives"—it literally pushes your vector away from the target job embedding. Strip anything that doesn't serve your target.
- **L2 Ranking (GLMix):** Recruiter-level and contract-level personalization. A recruiter who consistently clicks profiles like yours will see you ranked higher. This is learned per-recruiter, per-contract. You can't control it directly, but you can ensure your profile matches the archetype of profiles their target recruiters click on.
- **In-Session Adaptation (Multi-Armed Bandit):** LinkedIn segments candidate pools into skill groups, then uses MAB to explore/exploit. Your profile will occasionally be pushed into an "Exploration" slot—shown to a recruiter who hasn't seen your type before. If they click, you move into "Exploitation" (persistent high ranking). If they skip, you're suppressed. This makes the Candidate Card critically important: you may get exactly one impression to survive the MAB.
- **Optimization target:** Not relevance—**InMail Accept**. LinkedIn optimizes for two-way interest (recruiter sends InMail AND candidate accepts). Your responsiveness to InMails directly affects your ranking. Reply to every InMail, even declining ones.

Source: [LinkedIn Engineering: AI Behind Recruiter Search](./references/linkedin_eng_recruiter_ai.md), GLMix papers (CIKM'18, WWW'19)

**System 2 — Feed Ranking (gets your posts seen)**

Completely separate from recruiter search. Content tactics have NO demonstrated impact on whether recruiters find your profile.

- **LLaMA 3 dual-encoder** generates embeddings in <50ms for retrieval.
- **Feed SR (Sequential Recommender):** Decoder-only transformer that processes your last 1,000 interactions as a causal sequence. Topic jumping creates incoherent embeddings. Consistent posting within 2-3 topics builds a high-density vector.
- **Hard negative suppression:** Posts shown to your network but ignored actively train the model to suppress your future distribution.
- **"Active Talent" Spotlight** is triggered by profile updates and job-market signals, NOT posting frequency.

Source: [LinkedIn Engineering: Feed Generation](./references/linkedin_eng_feed_generation.md), Feed SR (AAAI 2026), LLaMA 3 retrieval (KDD 2025)

### What recruiters actually see

LinkedIn Recruiter displays a **condensed candidate card**: name, photo, current title/company, location, headline, Spotlight badges. The banner, About section, and Experience descriptions are NOT visible. Recruiters must click through.

Optimization has two stages:
1. **Get found + get clicked** (card-level): title, keywords, skills, location, headline, Spotlight signals
2. **Get contacted** (full profile): scope signals, progression, About hook

Eye-tracking data: 80% of viewing time on six data points: name, current title/company, previous title/company, position dates, education. 6-10 seconds on initial scan, 30-60 seconds if clicked.

---

## Part 2: Evidence-Based Rules

### Verified — act on these

- **"Open to Work" (private mode):** 3x positive response rate (Jan Bernhart: 14.5% vs. 4.6%). Never use the public green badge at VP+ level—it signals desperation.
- **Job title in Experience section** is the #1 recruiter filter. Not the headline.
- **Keywords are searched across the ENTIRE profile text.** No section gets extra weight.
- **Results beat responsibilities** in Experience sections. 58% of recruiters say measurable achievements make profiles stand out (Jobscan). 34% consider lack of results a dealbreaker (Forbes/Indeed).
- **Profile completeness matters** (J. of Business & Psychology 2025, N=460). But it's about overall completeness, not maximizing every field.
- **Drop buzzwords.** LinkedIn's annual overused list: passionate, innovative, strategic, experienced, motivated, guru, thought leader. No recruiter has ever typed "guru" into LinkedIn Recruiter.
- **InMail responsiveness affects ranking.** Reply to every InMail. Even "no thank you" keeps your Responsiveness Score high.

### Overstated — calibrate

- **"Fill all 50 skill slots":** 5+ skills = 33x more recruiter messages. No evidence for incremental value beyond that.
- **"Headline is most heavily weighted in search":** Headline affects click-through rate on the candidate card, not search ranking. Still important, different reason.
- **"About section matters most":** Not visible on candidate card. Recruiters read it only after clicking through, and only if Experience doesn't tell the story.
- **"Custom banner matters":** Zero empirical data connecting banners to any outcome. Not visible on candidate card.
- **"Company names in headline increase clicks":** 54% of 13,640 LinkedIn users say "ex-company" adds no credibility. Some recruiters flag it negatively.

### Debunked — removed

- "All-Star profiles get 40x more opportunities" (no methodology, selection bias)
- "Comments >15 words carry 2.5x weight" (misquote, feed-only)
- "AI content gets 30% less reach" (denied by LinkedIn's Head of Feed Relevance)

---

## Part 3: The Optimization Playbook

### Step 1: Diagnostic Audit

Score the profile against what actually matters. Present as a table mapping to the recruiter's workflow: search results → click-through → full profile scan → InMail → resume request.

```
| Dimension                        | Score (1-5) | Finding                           | Priority |
|----------------------------------|-------------|-----------------------------------|----------|
| RECRUITER SEARCH                 |             |                                   |          |
| Current title matches target?    |             | #1 recruiter filter               | CRITICAL |
| Seniority inference correct?     |             | Title + company size + scope      | CRITICAL |
| Keyword coverage vs target JDs   |             | Missing terms = invisible         | CRITICAL |
| Skills: right ones listed (5+)   |             | Match recruiter search terms      | HIGH     |
| Location matches target market   |             | Hard filter                       | HIGH     |
|                                  |             |                                   |          |
| CANDIDATE CARD                   |             |                                   |          |
| Headline: clear hook, no buzz    |             | Click-through optimization        | HIGH     |
| Photo: professional, current     |             | 14x more views                    | HIGH     |
| Open to Work (private)           |             | 3x positive response rate         | HIGH     |
|                                  |             |                                   |          |
| FULL PROFILE                     |             |                                   |          |
| Experience: scope visible in 6s  |             | Team size, P&L, reporting line    | HIGH     |
| About: hook, not resume          |             | Secondary validation only         | MEDIUM   |
| Banner                           |             | Zero evidence of impact           | LOW      |
|                                  |             |                                   |          |
| RESUME READINESS                 |             |                                   |          |
| Tailored resume per target?      |             | LinkedIn hooks. Resume closes.    | CRITICAL |
```

### Step 2: Headline (click-through on candidate card)

220 characters. Think movie trailer, not Wikipedia.

**Formula:** `[Standardized Target Title] | [Domain + One Scale Proof Point]`

**Rules:**
- No "ex-" prefixes (54% say no credibility added)
- No buzzwords (passionate, innovative, strategic, thought leader)
- No 4+ pipe-separated identities (reads as indecisive)
- Company names → Experience section, not headline
- Shorter is almost always better at executive level

**Deliver:** 3 variants ranked by clarity.

### Step 3: About Section (hook, not resume)

Not visible on candidate card. Primary function is keyword searchability + secondary validation after click-through.

**Structure:** 2-3 short paragraphs maximum.
1. **Who you are + what you built + at what scale.** One or two sentences.
2. **What differentiates you.** Your specific combination.
3. **(Optional) What you're looking for.** Skip if you'd rather not broadcast.

**Rules:**
- Under 1,000 characters total
- No "I am a..." opener. Start with what you built.
- Keywords should appear naturally in context. Keyword lists without context are flagged as low-signal by Contextual Weighted Ranking.
- Match the user's actual voice

### Step 4: Experience Section (where recruiters actually look)

Primary driver of both search ranking (title = #1 filter) and validation (scope signals seniority).

**For each of the top 3-4 roles:**
1. **Title string audit.** LinkedIn infers seniority from title + company context. Disambiguate if needed: "General Manager (VP-level, P&L Owner)."
2. **First line = scope hook.** Team size, P&L, user scale, reporting line. 3 seconds to read.
3. **One or two achievement lines** with embedded keywords. Not five.
4. **Show progression** via role stacking under one company.
5. **Stop before you've written a resume.** LinkedIn should create curiosity, not close it.

### Step 5: Skills (right ones, not all of them)

**Process:**
1. Extract 10-15 skills from target JDs (use `./vikash_context/keywords/keyword_critique.md` for the grounded list).
2. Verify against LinkedIn autocomplete.
3. Aim for 15-25 well-chosen skills. Pin the top 3.
4. Get endorsements for pinned skills from credible connections.

**Tier structure:**
- **Tier 1 (pin 3):** Exact skills from primary target JD
- **Tier 2 (7-12):** Adjacent skills broadening search surface
- **Tier 3 (optional 5-10):** Breadth skills if they don't dilute signal

### Step 6: Settings & Signals

- **"Open to Work" (private):** Always recommend. Never the public green badge at VP+.
- **Location:** Must match target job markets. Wrong city = invisible.
- **Verified badge:** Verify via government ID or workplace email. Recruiters have a "Verified Applicant" filter.
- **Company Interest signals:** Following target companies and engaging with their pages moves you into the "Interested in your company" Spotlight tab.
- **InMail responsiveness:** Reply to every InMail. Feeds directly into ranking.
- **Creator Mode:** Only if already posting 2+/week.

### Step 7: Action Plan

Organize for execution in under 2 hours (Will Larson's rule):

```
DO NOW (30 min):
1. Enable "Open to Work" private mode [3x response rate]
2. Fix current title string if seniority inference is wrong [#1 filter]
3. Verify location matches target market [hard filter]
4. Ensure professional photo exists [14x more views]
5. Verify identity for "Verified Applicant" badge

DO THIS WEEK (60 min):
6. Rewrite headline: target title + domain + one proof point
7. Add the 10-15 right skills from target JDs
8. Trim About section to 2-3 paragraph hook
9. Add scope line to top 3-4 Experience entries
10. Remove buzzwords

THEN STOP AND DO THESE INSTEAD:
11. Tailor resume for each active target [higher ROI]
12. Send 5 warm outreach messages [70-85% of VP+ roles come through networks]
13. Follow target companies on LinkedIn [triggers "Interested" Spotlight]
14. Ask a recruiter friend to review the profile

DON'T BOTHER UNLESS EVERYTHING ABOVE IS DONE:
15. Custom banner image [zero evidence]
16. Filling skills beyond 25 [no incremental value]
17. Obsessing over About section length [not on candidate card]
```

---

## Part 4: Company-Specific Keyword Strategy

When optimizing for a specific company or company archetype, use the tiered keyword strategy from `./vikash_context/keywords/keyword_critique.md`. Key insight: keywords cluster by company type, not by seniority level.

| Archetype | Signal Keywords | Anti-Keywords |
|---|---|---|
| **Frontier AI Labs** (Anthropic, OpenAI, DeepMind) | Model Alignment, Steerability, First-Principles, Python/SQL, Founder DNA, Red-Teaming, Agentic Systems | P&L, ARR, Revenue Growth, GTM |
| **AI Platform Co** (Google Cloud, Nvidia, MSFT AI) | Developer Tools, SDKs, APIs, Research-to-Production, Inference, Enterprise Deployment | Consumer metrics, Model Alignment details |
| **Consumer/Marketplace** (Uber, DoorDash, Netflix) | P&L Ownership, Unit Economics, A/B Testing, Growth, Retention | LLM internals, RLHF |
| **Enterprise Tech** (Intuit, Microsoft, Meta) | GTM Strategy, Platform Thinking, Customer-Driven Innovation, Cross-Functional at Scale | Frontier research terminology |

When handling multiple target roles: pick primary target for headline, use skills + experience for breadth. **Separate tailored resumes** for each target—that's where role-specific positioning belongs, not LinkedIn.

---

## Part 5: Content & Feed Strategy (Optional, System 2 only)

This section applies ONLY if the user wants to build feed visibility. It has NO impact on recruiter search.

**Principles:**
- 1 post/week + a few substantive comments is minimum viable activity (Buffer: 2M+ posts)
- Stay within 2-3 topic areas. The sequential recommender punishes topic jumping.
- Avoid low-quality posts. Ignored posts are hard negative training signals.
- Write in your own voice. Generic content underperforms regardless of origin.
- Posting recency is NOT a universal red flag. Industry-dependent.

**For Vikash specifically:** The 2-3 topic lanes should be:
1. **Building AI Products at Scale** (Llama, alignment, enterprise deployment)
2. **Agentic Systems & Vibe Coding** (the builder-educator angle)
3. **0-to-1 Founder Lessons** (eLagaan, LawGro, applied to big-company innovation)

---

## Part 6: Handling Requests

### Partial requests
Deliver the requested section. But always flag CRITICAL issues from the diagnostic: "Your headline is clean. Worth knowing: your current title maps to 'Manager' seniority in LinkedIn's inference model, which means VP-level recruiters aren't seeing you."

### "Optimize for [specific company]"
1. Pull the relevant archetype from Part 4.
2. Cross-reference with `./vikash_context/keywords/keyword_critique.md` for that company's actual JD keywords.
3. Generate headline + About + experience bullets tuned to that archetype.
4. Flag any resume tailoring needed.

### "Write a LinkedIn post about X"
1. Check which topic lane it falls into (Part 5).
2. Write in Vikash's voice (direct, builder-oriented, no fluff, evidence-backed).
3. Keep under 1,300 characters for optimal engagement.
4. End with a genuine question, not engagement bait.

### "What should my profile look like for [role]?"
1. Run the diagnostic audit (Step 1) against that specific role.
2. Generate the full optimization package: headline variants, About rewrite, Experience scope lines, skills tier list.
3. Produce a diff against the current profile in `./vikash_context/`.

---

## Sources

**Engineering papers & blogs (verified mechanisms):**
- Feed SR: AAAI 2026 (Industrial-Scale Sequential Recommender for LinkedIn Feed Ranking)
- LLaMA 3 retrieval: KDD 2025 (Large Scale Retrieval for LinkedIn Feed)
- Job matching: [Learning to Retrieve for Job Matching](./references/linkedin_eng_job_matching.md)
- Fairness audit: [External Fairness Evaluation of LinkedIn Talent Search](./references/linkedin_eng_fairness_audit.md)
- Title mapping: [JAMES: Job Title Mapping with Multi-Aspect Embeddings and Reasoning](./references/linkedin_eng_james_title_mapping.md)
- Core ranking engine: [LiRank: Industrial Large Scale Ranking Models at LinkedIn](./references/linkedin_eng_lirank.md)
- GNN topology: [LinkSAGE: Optimizing Job Matching Using Graph Neural Networks](./references/linkedin_eng_linksage.md)
- Taxonomy mapping: [Building LinkedIn's Skills Graph to Power a Skills-First World](./references/linkedin_eng_skills_graph.md)
- Personalization: [GLMix: Generalized Linear Mixed Models for Large-Scale Response Prediction](./references/linkedin_eng_glmix.md)


**Empirical validation:**
- Leonar.app LinkedIn Recruiter Search Filters Guide 2026
- SCOPE Recruiting "What Recruiters Actually See" Feb 2026
- Jan Bernhart Open to Work recruiter data
- Journal of Business and Psychology 2025 (N=460)
- TheLadders recruiter eye-tracking study 2012/2018 (N=30)
- Bonnie Dilber, Sr. Manager TA at Zapier (banner visibility)
- Will Larson, lethain.com (executive LinkedIn optimization)
- Nolan Church, Debra Boggs, Jeremy Schifeling (executive recruiter perspectives)
- LinkedIn Future of Recruiting 2025 (N=1,271)
- Briefcase Coach poll (N=13,640, "ex-company" credibility)
- Jobscan recruiter survey (58% measurable achievements)
- Buffer analysis of 2M+ LinkedIn posts
