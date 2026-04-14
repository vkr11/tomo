# LinkedIn Optimizer: Engineering References Index

This directory holds the primary engineering source material that powers the `linkedin_optimizer` skill. By grounding the skill in actual LinkedIn engineering architectures, we bypass "influencer wisdom" and optimize directly for the algorithmic mechanisms that govern recruiter visibility and candidate ranking.

## 1. Title Taxonomy & Seniority Inference
**[JAMES: Job Title Mapping with Multi-Aspect Embeddings and Reasoning](./linkedin_eng_james_title_mapping.md)** (arXiv:2202.10739)
- **What it is:** The mathematical model behind LinkedIn's central "Economic Graph Taxonomy."
- **Key Insight:** Explains how LinkedIn resolves messy free-text titles into canonical "Taxonomy Entity IDs." It reveals the use of a "Job Transition Graph" embedded in Poincaré hyperbolic space to trace career trajectories (e.g., Senior PM → Lead PM → Head of Product) and infers executive seniority based on sequential promotion paths.

## 2. Core Search Ranking Engine
**[LiRank: Industrial Large Scale Ranking Models at LinkedIn](./linkedin_eng_lirank.md)** (arXiv:2402.06859)
- **What it is:** The master ranking framework deployed for both Feed and Recruiter Search.
- **Key Insight:** Details the "Explore/Exploit" Multi-Armed Bandit strategy. New profiles or updated profiles are surfaced in a temporary "exploration" window; high engagement (like a recruiter clicking your Candidate Card instead of scrolling past) rapidly shifts you into the "exploit" bucket, granting persistently high search ranking.

## 3. Network-Aware Job Matching
**[LinkSAGE: Optimizing Job Matching Using Graph Neural Networks](./linkedin_eng_linksage.md)** (arXiv:2402.13430)
- **What it is:** LinkedIn's implementation of Graph Neural Networks (GNNs).
- **Key Insight:** Proves that text matching is not the only factor. The model evaluates your *network topology* — if you are heavily connected to engineers at a specific company (e.g., Anthropic), the GNN mathematically pulls your embeddings closer to that company's job postings, even if your raw keywords don't match perfectly.

## 4. Recruiter Match Diagnostics
**[Learning to Retrieve for Job Matching](./linkedin_eng_job_matching.md)** (arXiv:2402.13435)
- **What it is:** A deep dive into the Two-Tower DNN architecture used for candidate retrieval.
- **Key Insight:** Confirms that LinkedIn treats candidates as "Items" and recruiters/jobs as "Users", generating dense vector embeddings for both. Explains how hard filters (Title, Location) act as the primary gating mechanism before the Two-Tower DNN calculates semantic similarity.

## 5. Algorithmic Filtering & Bias
**[External Fairness Evaluation of LinkedIn Talent Search](./linkedin_eng_fairness_audit.md)** (arXiv:2511.10752)
- **What it is:** An external audit of the Recruiter Search platform.
- **Key Insight:** Validates what recruiters *actually* see (the Candidate Card). Confirms that visual processing of the candidate card takes less than 6 seconds, making the "Headline" the most critical click-through hook on the platform.

## 6. Feed Personalization & Recommender
**[Engineering the Next Generation of LinkedIn's Feed](./linkedin_eng_feed_generation.md)** (Engineering Blog)
- **What it is:** The shift from classical ML ranking to a Generative Recommender (GR) using transformer architectures.
- **Key Insight:** Explains how feed visibility works. Emphasizes "sequential interaction history" (the model looks at the last 1,000+ items a user interacted with) and proves that dense, high-quality, topic-specific posting is rewarded over generic high-frequency posting.

## 7. Recruiter Recommendation Architecture
**[The AI behind LinkedIn Recruiter search and recommendation systems](./linkedin_eng_recruiter_ai.md)** (Engineering Blog)
- **What it is:** The end-to-end architecture overview of the Recruiter product.
- **Key Insight:** Explains GLMix (Generalized Linear Mixed Models) used to personalize search results for *individual recruiters*.

## 8. Skills Extraction & Taxonomy Mapping
**[Building LinkedIn's Skills Graph to Power a Skills-First World](./linkedin_eng_skills_graph.md)** (Engineering Blog)
- **What it is:** Detailed breakdown of how the Skills Graph is built.
- **Key Insight:** Explains how LinkedIn maps unstructured text from paragraphs into their standardized Skills taxonomy using "market-aware" extraction and BERT-based models. Bullet point phrasing must trigger the extraction models cleanly.

## 9. Foundational Personalization Layer
**[GLMix: Generalized Linear Mixed Models for Large-Scale Response Prediction](./linkedin_eng_glmix.md)** (KDD Synthesis)
- **What it is:** The math behind how recruiter rankings diverge. 
- **Key Insight:** Two recruiters running the exact same search see different rankings because each recruiter has ID-level regression coefficients based on their historical clicks and hires. Emphasizes the need for distinct "Archetype" keyword clusters over generic generalist profiles.
