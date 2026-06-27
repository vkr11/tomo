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

# LinkedIn Profile Optimizer v5.0

## Skill Architecture

This skill has three layers. Use the right one for the request.

```
Layer 1: STRATEGY    — The "why" behind every recommendation (this file)
Layer 2: CONTEXT     — Vikash's specific positioning, keywords, arcs (./vikash_context/)
Layer 3: REFERENCES  — Engineering papers, blog captures, operational teardowns (./references/)
                       See ./references/README.md for the full annotated index with architecture map.
```

When invoked:
1. Read `./vikash_context/linkedin_core_identity.md` for current positioning and target domains.
2. Read `./vikash_context/keyword_critique.md` (in `keywords/`) for the grounded keyword tiers per company archetype.
3. Read `./vikash_context/linkedin_platform_checklist.md` for the current implementation status.
4. Consult `./references/README.md` for the annotated engineering index when verifying algorithmic claims.

Do NOT ask for target roles or constraints unless the user explicitly says they're switching domains.
The default context is already loaded.

---

## Part 1: How LinkedIn Actually Works (The Machine)

### The 5-Layer Pipeline

LinkedIn Recruiter Search is not a single algorithm. It's a 5-layer pipeline where each layer can eliminate you entirely. Understanding which layer you're failing at determines which profile section to fix.

```
Recruiter enters search query
        │
        ▼
┌─────────────────────────┐
│  LAYER 1: HARD FILTERS   │  Title (JAMES taxonomy), Location, Skills (Skills Graph)
│  (Binary pass/fail)      │  If you fail here, the pipeline stops. You don't exist.
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│  LAYER 2: RETRIEVAL      │  Two-Tower DNN: candidate embedding vs. query embedding
│  (Top ~1000 pool)        │  Profile text richness determines embedding quality.
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│  LAYER 3: RANKING        │  LiRank (MAB explore/exploit + Residual DCN)
│  + GLMix personalization │  Per-recruiter coefficients reorder the pool.
│  + LinkSAGE GNN          │  Network topology shifts your position.
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│  LAYER 4: CANDIDATE CARD │  What the recruiter sees: Headline, Photo,
│  (6-second decision)     │  Current Title, Past 2 Roles, Education, Spotlights
│                          │  NOT shown: About, Experience bullets, Recommendations
└─────────┬───────────────┘
          │ Click or skip
          ▼
┌─────────────────────────┐
│  LAYER 5: FULL PROFILE   │  About, Experience descriptions, Skills list,
│  (Only if they clicked)  │  Recommendations. This is where scope signals live.
└─────────────────────────┘
```

### Layer 1: Hard Filters (Pass/Fail Gate)

Source: [JAMES](./references/linkedin_eng_james_title_mapping.md), [Skills Graph](./references/linkedin_eng_skills_graph.md), [Job Matching](./references/linkedin_eng_job_matching.md)

Hard filters are applied BEFORE any ML model evaluates you. If your title, location, or skills don't match the recruiter's filter selections, the Two-Tower DNN never sees your profile. There is no "soft match" fallback at this layer.

**Title Taxonomy (JAMES model):**
- LinkedIn maps every free-text title to a canonical **Taxonomy Entity ID** via the JAMES model (Job Title Mapping with Multi-Aspect Embeddings and Reasoning).
- JAMES uses 3 embedding layers: syntactic (string matching), semantic (BERT meaning), and topological (Poincaré hyperbolic embeddings from 2.7M+ career transitions).
- The topological layer embeds a **Job Transition Graph** in hyperbolic space. It treats "the most recent job title as the parent, assuming it contains all requirements from previous titles." Your sequential career trajectory is a hard quantitative seniority signal.
- Free-text titles that don't cleanly match a taxonomy entity fall into a "long tail" bucket (350,000+ unique titles) where seniority inference becomes unreliable.
- **Rule: ALWAYS pick titles from LinkedIn's autocomplete dropdown.** This locks in the exact entity ID, bypassing the fuzzy NLP pipeline.

**Skills Taxonomy (Skills Graph):**
- LinkedIn runs BERT-based extraction models over your About and Experience text to **infer** additional skills beyond the ones you explicitly list.
- Skills have "market-aware" weighting — "Python" on a PM profile is weighted differently than on an engineer's profile.
- The Skills Graph tracks **skill adjacencies** — listing "Model Alignment" automatically associates "RLHF," "AI Safety," and "Red-Teaming" at reduced weight.
- Skills from industries you're leaving (FPGA, VHDL, ASIC) act as **hard negatives** — they pull your embedding away from your target domain.

### Layer 2: Two-Tower Retrieval

Source: [Job Matching](./references/linkedin_eng_job_matching.md)

LinkedIn treats candidates as "Items" and recruiters/jobs as "Users." Each side gets a 128-dimensional embedding vector trained on 150M+ engagement records. The system computes approximate nearest neighbor (ANN) similarity to produce a pool of ~1000 candidates.

- Retrieval quality is bottlenecked by the **candidate tower embedding**, not the query tower. This means the richness and specificity of YOUR profile text is the primary lever.
- Unrelated content in your profile acts as "hard negatives" — it pushes your vector away from the target job embedding. Strip anything that doesn't serve your target.
- The "nearline inference pipeline" (Kafka + Apache Beam) updates candidate embeddings in near real-time. Profile updates are reflected in search results within minutes to hours.

### Layer 3: Ranking (LiRank + GLMix + LinkSAGE)

Source: [LiRank](./references/linkedin_eng_lirank.md), [GLMix](./references/linkedin_eng_glmix.md), [LinkSAGE](./references/linkedin_eng_linksage.md)

Three models work together to order the ~1000 retrieved candidates:

**LiRank (Explore/Exploit):**
- Uses a Multi-Armed Bandit (MAB) strategy. When your profile is new or recently updated, LinkedIn enters an "exploration" phase, surfacing you to a broader set of recruiters.
- If engagement is high during this window (recruiters click your card), you graduate to the "exploit" bucket with persistently high ranking. Low engagement = suppressed.
- **The "Update Window Effect":** Batch all profile changes together. You get one strong exploration window, not several weak ones if you trickle changes over weeks.
- Uses isotonic calibration to correct for biases in historical click data, so past poor performance can be partially overcome.

**GLMix (Per-Recruiter Personalization):**
- Trains 3 sets of coefficients: global, per-recruiter, and per-candidate.
- Two recruiters running the exact same search query see **different rankings**. An Anthropic recruiter who historically clicks on profiles mentioning "Agentic AI" from Meta alumni will see those candidates boosted. A startup recruiter with different click patterns sees a completely different ordering.
- Produced a **20-40% increase in job applications** when deployed — proving personalization massively outperforms global ranking.
- **Implication:** Don't try to be a "generalist PM." GLMix rewards keyword specificity per recruiter archetype. Mixing Enterprise GTM and Frontier Lab keywords makes your embedding fuzzy for all recruiter segments.

**LinkSAGE (Network Topology):**
- Graph Neural Network that augments text-based matching with your **connection graph** topology.
- If you're connected to 50 engineers at Anthropic, the GNN pulls your embedding closer to Anthropic's job postings — even if your keywords don't perfectly match.
- Conversely, a network dominated by connections in industries you're leaving anchors your embedding to those industries.
- Uses neighborhood sampling, so the quality of your *closest* connections matters more than total count.

### Layer 4: Candidate Card (The Decision Surface)

Source: [Recruiter Workflow](./references/linkedin_recruiter_workflow.md), [Fairness Audit](./references/linkedin_eng_fairness_audit.md)

Recruiters use a $10,000/yr enterprise SaaS product (LinkedIn Recruiter). Search results appear as a list of **Candidate Cards**, not full profiles. The recruiter makes a Yes/No/Skip decision in ~6 seconds.

**What the Candidate Card shows:**
- Photo + Name
- **Headline** (only free-text hook you control on the card)
- Current Position + Company
- Past 2 Positions
- Education
- Shared Connections
- Spotlight badges (Open to Work, Engaged with Company, Verified)

**What the Candidate Card does NOT show:**
- About Section
- Experience bullet points / descriptions
- Recommendations
- Publications / Projects
- Skills list

**"Spotlights" accelerate sourcing.** Recruiters click Spotlight filters BEFORE scrolling results:
- *Open to Work* (3x response rate — this is the #1 behavioral filter)
- *Engaged with Talent Brand* (followed the company page)
- *Verified Applicant* (completed identity verification)

**Company-First Sourcing:** Executive recruiters frequently start by selecting target companies (Meta, Google, OpenAI), then filter by department — rather than starting with a title search. Tier 1 companies in your experience act as a gravity well for search volume.

### System 2 — Feed Ranking (Separate System, Zero Overlap)

Source: [Feed Generation](./references/linkedin_eng_feed_generation.md)

Feed ranking is completely independent from Recruiter Search. Content tactics have NO demonstrated impact on whether recruiters find your profile.

- **Generative Recommender (GR):** Transformer-based sequential recommender processes your last 1,000+ interactions. Topic density beats posting frequency.
- **Long-range dependencies:** A post from 3 months ago still influences how the model categorizes your content today.
- **Engagement hierarchy:** Comments > Reactions > Clicks > Impressions. 10 thoughtful comments outrank 100 likes.
- **Hard negative suppression:** Posts shown to your network but ignored actively train the model to suppress your future distribution.
- **"Active Talent" Spotlight** is triggered by profile updates and job-market signals, NOT posting frequency.

---

## Part 2: Evidence-Based Rules

### Verified — act on these

- **"Open to Work" (private mode):** 3x positive response rate (Jan Bernhart: 14.5% vs. 4.6%). Never use the public green badge at VP+ level — it signals desperation.
- **Title from dropdown = Taxonomy Entity ID.** The #1 recruiter filter. Free-text titles risk misclassification in JAMES' long-tail bucket.
- **Role stacking = Poincaré trajectory signal.** Sequential roles under one company feed directly into the Job Transition Graph for seniority inference.
- **Keywords are searched across the ENTIRE profile text.** No section gets extra weight at the retrieval layer.
- **Results beat responsibilities** in Experience sections. 58% of recruiters say measurable achievements make profiles stand out. 34% consider lack of results a dealbreaker.
- **Profile completeness matters** (J. of Business & Psychology 2025, N=460). Incomplete sections produce lower-confidence embeddings.
- **Drop buzzwords.** LinkedIn's annual overused list: passionate, innovative, strategic, experienced, motivated, guru, thought leader. No recruiter has ever typed "guru" into LinkedIn Recruiter.
- **InMail responsiveness is a ranking feature.** Reply to every InMail. Even "no thank you" keeps your Responsiveness Score high. Your per-candidate GLMix coefficients are trained on this signal.
- **Batch profile updates.** LiRank's MAB triggers one exploration window per major update. Trickle changes = several weak windows. Batch changes = one strong window.
- **Skills extraction fires on prose.** BERT-based models extract skills from your About and Experience text, not just your Skills list. "Built red-teaming frameworks" triggers extraction; "tested the model" does not.
- **Skill adjacencies expand coverage.** Listing "Model Alignment" automatically pulls in RLHF, AI Safety, evaluation at reduced weight. You don't need to list every related skill.
- **Network topology matters.** Connections at target companies shift your GNN embedding toward their job cluster (LinkSAGE). Follow target companies and connect with their people.

### Overstated — calibrate

- **"Fill all 50 skill slots":** 5+ skills = 33x more recruiter messages. No evidence for incremental value beyond ~25.
- **"Headline is most heavily weighted in search":** Headline affects click-through rate on the candidate card, not search ranking. Critical for a different reason (Layer 4, not Layer 1).
- **"About section matters most":** Not visible on candidate card. Recruiters read it only after clicking through.
- **"Custom banner matters":** Zero empirical data connecting banners to any outcome. Not visible on candidate card.
- **"Company names in headline increase clicks":** 54% of 13,640 LinkedIn users say "ex-company" adds no credibility.

### Debunked — removed

- "All-Star profiles get 40x more opportunities" (no methodology, selection bias)
- "Comments >15 words carry 2.5x weight" (misquote, feed-only)
- "AI content gets 30% less reach" (denied by LinkedIn's Head of Feed Relevance)

---

## Part 3: The Optimization Playbook

### Step 1: Diagnostic Audit

Score the profile against what actually matters. Map each dimension to the **pipeline layer** it affects:

```
| Dimension                        | Layer | Score | Finding                           | Priority |
|----------------------------------|-------|-------|-----------------------------------|----------|
| HARD FILTERS (Layer 1)           |       |       |                                   |          |
| Title from dropdown?             | L1    |       | Taxonomy Entity ID match          | CRITICAL |
| Roles stacked under company?     | L1    |       | Poincaré trajectory signal        | CRITICAL |
| Keyword coverage vs target JDs   | L1    |       | Missing terms = invisible         | CRITICAL |
| Skills: right ones listed (5+)   | L1    |       | Hard filter in Recruiter          | HIGH     |
| Location matches target market   | L1    |       | Hard filter                       | HIGH     |
|                                  |       |       |                                   |          |
| RETRIEVAL (Layer 2)              |       |       |                                   |          |
| Experience text richness         | L2    |       | Candidate tower embedding quality | HIGH     |
| Anti-keywords removed?           | L2    |       | Hard negatives in embedding       | HIGH     |
|                                  |       |       |                                   |          |
| RANKING (Layer 3)                |       |       |                                   |          |
| Network: connections at targets  | L3    |       | LinkSAGE GNN embedding shift      | MEDIUM   |
| InMail responsiveness            | L3    |       | GLMix per-candidate coefficient   | MEDIUM   |
|                                  |       |       |                                   |          |
| CANDIDATE CARD (Layer 4)         |       |       |                                   |          |
| Headline: hook, not bio          | L4    |       | CTR during MAB exploration        | CRITICAL |
| Photo: professional, current     | L4    |       | 14x more views                    | HIGH     |
| Open to Work (private)           | L4    |       | 3x response + Spotlight filter    | CRITICAL |
| Verified badge                   | L4    |       | Spotlight filter + ranking boost  | HIGH     |
| Top 3 roles tell the story?      | L4    |       | Only 3 positions visible on card  | HIGH     |
|                                  |       |       |                                   |          |
| FULL PROFILE (Layer 5)           |       |       |                                   |          |
| Experience: scope visible in 6s  | L5    |       | Team size, P&L, scale             | HIGH     |
| About: hook, not resume          | L5    |       | Secondary validation only         | MEDIUM   |
| Banner                           | L5    |       | Zero evidence of impact           | LOW      |
|                                  |       |       |                                   |          |
| RESUME READINESS                 |       |       |                                   |          |
| Tailored resume per archetype?   | —     |       | LinkedIn hooks. Resume closes.    | CRITICAL |
```

### Step 2: Titles (Layer 1 — Hard Filter)

**Rule: Always pick from LinkedIn's autocomplete dropdown.** This maps to the canonical Taxonomy Entity ID in the JAMES model. Free-text titles force the model to use fuzzy multi-aspect matching across 350,000+ titles, risking seniority misclassification.

**For each Experience entry:**
1. Clear the title field.
2. Start typing the title.
3. **Select from the dropdown autocomplete.**
4. Put scope clarification (org, domain, charter) in the **first line of the description**, not the title.

**Stack all roles under one company.** The JAMES model's Poincaré embedding traces `Product Lead → Head of Product → Lead PM → Senior PM` as a directed promotion path in hyperbolic space. Separate company entries break the transition graph — each role looks lateral, not promoted.

### Step 3: Headline (Layer 4 — Candidate Card CTR)

220 characters. The ONLY free-text field visible on the Candidate Card. During LiRank's MAB exploration window, your headline CTR determines whether you graduate to persistently high ranking or get suppressed.

**Formula:** `[Strongest Real Title] | [Domain + One Scale Proof Point]`

**Rules:**
- Lead with the strongest title you actually held (e.g., "Head of Product"), not your current title if it's weaker
- No "ex-" prefixes (54% say no credibility added)
- No buzzwords (passionate, innovative, strategic, thought leader)
- No 4+ pipe-separated identities (reads as indecisive)
- Company names → Experience section, not headline (it's already on the card)
- Shorter is almost always better at executive level

**Deliver:** 3 variants ranked by clarity.

### Step 4: About Section (Layer 5 — Post-Click Validation)

Not visible on candidate card. Primary function: keyword searchability + secondary validation after click-through. BERT-based skill extraction models also run over this text.

**Structure:** 2-3 short paragraphs maximum.
1. **What you built + at what scale.** Start with impact, not identity.
2. **What differentiates you.** Your unique combination.
3. **(Optional) What you're looking for.** Creates an InMail opening for recruiters.

**Rules:**
- Under 1,000 characters total
- No "I am a..." opener. Start with what you built.
- Use exact skill taxonomy language so BERT extraction fires: "model alignment" not "making models work better"
- Keywords should appear naturally in context. Keyword lists without context are flagged as low-signal.
- Match the user's actual voice

### Step 5: Experience Section (Layer 2 + Layer 4)

Serves two purposes: (1) feeds the candidate tower embedding (Layer 2), and (2) the top 3 roles appear on the Candidate Card (Layer 4).

**For each of the top 3-4 roles:**
1. **Title: from dropdown.** (See Step 2.)
2. **First line = scope hook.** Team size, P&L, user scale, reporting line. 3 seconds to read.
3. **Use exact skill taxonomy language.** "Built red-teaming frameworks" → triggers extraction. "Tested the model" → does not.
4. **One or two achievement lines** with embedded keywords. Not five.
5. **Show progression** via role stacking under one company.
6. **Stop before you've written a resume.** LinkedIn should create curiosity, not close it.

### Step 6: Skills (Layer 1 — Hard Filter)

**Process:**
1. Extract 10-15 skills from target JDs (use `./vikash_context/keywords/keyword_critique.md`).
2. Type each into LinkedIn's skill field and **select from autocomplete** (same taxonomy principle as titles).
3. Aim for 15-25 well-chosen skills. Pin the top 3.
4. **Remove skills from industries you're leaving** — they act as hard negatives in the Two-Tower DNN, pulling your embedding away from your target domain.
5. Get endorsements for pinned skills from credible connections.

**Tier structure:**
- **Tier 1 (pin 3):** Exact skills from primary target JD
- **Tier 2 (7-12):** Adjacent skills broadening search surface
- **Tier 3 (optional 5-10):** Breadth skills if they don't dilute signal

**Skill adjacency:** LinkedIn's Skills Graph tracks co-occurring skills. Listing anchor skills (e.g., "Model Alignment") automatically associates related skills (RLHF, AI Safety) at reduced weight. You don't need to list every variant.

### Step 7: Settings & Signals (Layer 3 + Layer 4)

- **"Open to Work" (private):** Always recommend. It's the #1 Spotlight filter and a ranking boost feature. Never the public green badge at VP+.
- **Location:** Must match target job markets. Wrong city = invisible at Layer 1.
- **Verified badge:** Complete via government ID or workplace email. Both a Spotlight filter AND a ranking feature.
- **Follow target companies:** Triggers "Engaged with Talent Brand" Spotlight (Layer 4) AND shifts your LinkSAGE GNN embedding toward their job cluster (Layer 3).
- **InMail responsiveness:** Reply to every InMail. Feeds directly into your per-candidate GLMix coefficients (Layer 3).
- **Creator Mode:** Only if already posting 2+/week. Otherwise it dilutes your profile with feed metrics.

### Step 8: Action Plan (Batch for One Exploration Window)

**Critical: Batch all changes together.** LiRank's MAB allocates one exploration window per major profile update. If you trickle changes over 2 weeks, you get several weak exploration windows with partial optimization. If you batch everything into one session, you get one strong window with your fully optimized profile.

```
BATCH 1 — DO ALL AT ONCE (2 hours):
 1. Fix all Experience titles via dropdown [Layer 1 hard filter]
 2. Stack roles under one company entry [Poincaré trajectory signal]
 3. Enable "Open to Work" private mode [3x response rate + Spotlight]
 4. Verify identity for "Verified Applicant" badge [Spotlight + ranking]
 5. Verify location matches target market [Layer 1 hard filter]
 6. Ensure professional photo exists [14x more views]
 7. Rewrite headline: strongest title + domain + proof point [Layer 4 CTR]
 8. Add/remove skills from taxonomy [Layer 1 hard filter]
 9. Rewrite top 3-4 Experience descriptions [Layer 2 embedding quality]
10. Trim About section to 2-3 paragraph hook [Layer 5 + skill extraction]
11. Follow target companies [Spotlight + GNN embedding]

THEN STOP AND DO THESE INSTEAD (higher ROI):
12. Tailor resume for each active archetype [LinkedIn hooks. Resume closes.]
13. Send 5 warm outreach messages [70-85% of VP+ roles come through networks]
14. Reply to all pending InMails [GLMix coefficient]
15. Ask a recruiter friend to review the profile

DON'T BOTHER UNLESS EVERYTHING ABOVE IS DONE:
16. Custom banner image [zero evidence]
17. Filling skills beyond 25 [no incremental value]
18. Obsessing over About section length [not on candidate card]
```

---

## Part 4: Company-Specific Keyword Strategy

When optimizing for a specific company or company archetype, use the tiered keyword strategy from `./vikash_context/keywords/keyword_critique.md`. Key insight: keywords cluster by company type, not by seniority level.

**Critical (GLMix implication):** Don't blend keywords. Each recruiter archetype has per-recruiter GLMix coefficients trained on their historical click/hire patterns. An Anthropic recruiter's coefficients are tuned for Frontier Lab keywords. Mixing in Enterprise GTM keywords makes your embedding fuzzy for all segments.

| Archetype | Signal Keywords | Anti-Keywords |
|---|---|---|
| **Frontier AI Labs** (Anthropic, OpenAI, DeepMind) | Model Alignment, Steerability, First-Principles, Python/SQL, Founder DNA, Red-Teaming, Agentic Systems | P&L, ARR, Revenue Growth, GTM |
| **AI Platform Co** (Google Cloud, Nvidia, MSFT AI) | Developer Tools, SDKs, APIs, Research-to-Production, Inference, Enterprise Deployment | Consumer metrics, Model Alignment details |
| **Consumer/Marketplace** (Uber, DoorDash, Netflix) | P&L Ownership, Unit Economics, A/B Testing, Growth, Retention | LLM internals, RLHF |
| **Enterprise Tech** (Intuit, Microsoft, Meta) | GTM Strategy, Platform Thinking, Customer-Driven Innovation, Cross-Functional at Scale | Frontier research terminology |

When handling multiple target roles: pick primary target for headline, use skills + experience for breadth. **Separate tailored resumes** for each target — that's where role-specific positioning belongs, not LinkedIn.

---

## Part 5: Content & Feed Strategy (Optional, System 2 only)

This section applies ONLY if the user wants to build feed visibility. It has NO impact on recruiter search.

**Principles:**
- 1 post/week + a few substantive comments is minimum viable activity (Buffer: 2M+ posts)
- Stay within 2-3 topic areas. The sequential recommender punishes topic jumping.
- Avoid low-quality posts. Ignored posts are hard negative training signals.
- Engagement signal hierarchy: Comments > Reactions > Clicks > Impressions
- Long-range dependencies: a post from 3 months ago still influences your topic embedding today.
- Write in your own voice. Generic content underperforms regardless of origin.

**For Vikash specifically:** The 2-3 topic lanes should be:
1. **Building AI Products at Scale** (Llama, alignment, enterprise deployment)
2. **Agentic Systems & Vibe Coding** (the builder-educator angle)
3. **0-to-1 Founder Lessons** (eLagaan, LawGro, applied to big-company innovation)

---

## Part 6: Handling Requests

### Partial requests
Deliver the requested section. But always flag CRITICAL issues from the diagnostic: "Your headline is clean. Worth knowing: your current title maps to 'Manager' seniority in LinkedIn's inference model, which means VP-level recruiters aren't seeing you. This is a Layer 1 hard filter issue."

### "Optimize for [specific company]"
1. Pull the relevant archetype from Part 4. Note the GLMix implication for keyword specificity.
2. Cross-reference with `./vikash_context/keywords/keyword_critique.md` for that company's actual JD keywords.
3. Generate headline + About + experience bullets tuned to that archetype.
4. Flag any resume tailoring needed.

### "Write a LinkedIn post about X"
1. Check which topic lane it falls into (Part 5).
2. Write in Vikash's voice (direct, builder-oriented, no fluff, evidence-backed).
3. Keep under 1,300 characters for optimal engagement.
4. End with a genuine question, not engagement bait.

### "What should my profile look like for [role]?"
1. Run the diagnostic audit (Step 1) against that specific role, mapping to pipeline layers.
2. Generate the full optimization package: headline variants, About rewrite, Experience scope lines, skills tier list.
3. Produce a diff against the current profile in `./vikash_context/`.

---

## Sources

**Full annotated index with architecture map:** [./references/README.md](./references/README.md)

**Engineering papers & blogs (10 verified mechanisms):**
- Title mapping: [JAMES: Job Title Mapping with Multi-Aspect Embeddings and Reasoning](./references/linkedin_eng_james_title_mapping.md)
- Core ranking: [LiRank: Industrial Large Scale Ranking Models at LinkedIn](./references/linkedin_eng_lirank.md)
- GNN topology: [LinkSAGE: Optimizing Job Matching Using Graph Neural Networks](./references/linkedin_eng_linksage.md)
- Job matching: [Learning to Retrieve for Job Matching](./references/linkedin_eng_job_matching.md)
- Fairness audit: [External Fairness Evaluation of LinkedIn Talent Search](./references/linkedin_eng_fairness_audit.md)
- Feed generation: [Engineering the Next Generation of LinkedIn's Feed](./references/linkedin_eng_feed_generation.md)
- Recruiter AI: [The AI behind LinkedIn Recruiter Search](./references/linkedin_eng_recruiter_ai.md)
- Skills taxonomy: [Building LinkedIn's Skills Graph](./references/linkedin_eng_skills_graph.md)
- Personalization: [GLMix: Generalized Linear Mixed Models](./references/linkedin_eng_glmix.md)
- Recruiter workflow: [How Recruiters Use LinkedIn Recruiter](./references/linkedin_recruiter_workflow.md)

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
