# Pillar 7: AI & Technical Fluency

> **NEW for 2025/2026 — This is the round that separates good candidates from great ones.**
>
> | Dimension | Description |
> |-----------|-------------|
> | **Primary Signal** | Can you think about AI systems as a PM — understanding capabilities, limitations, architecture, and tradeoffs — without being an ML engineer? |
> | **Weak Answer** | "We'd use AI to make it better." No understanding of how models work. Can't discuss tradeoffs. Defers entirely to Engineering. Treats AI as magic. |
> | **Strong Answer** | Articulates specific AI architecture choices (RAG vs fine-tuning vs prompting). Discusses tradeoffs (latency vs quality, precision vs recall, cost vs accuracy). Understands safety/ethics implications. Can design an AI product end-to-end. |
> | **L5/L6** | "I'd add an AI feature to summarize content." |
> | **L7** | "For summarization at Google's scale, I'd use a RAG pipeline with Gemini Pro for quality-critical use cases and Gemini Flash for latency-sensitive ones. The key tradeoff is hallucination rate vs response time. I'd implement guardrails using grounding with Google Search, set a confidence threshold, and measure success via factual accuracy (human-rated sample) and task completion rate." |

---

## Core Signals to Show

- [ ] **AI Product Intuition**: Understand *what* AI can and can't do today
- [ ] **Architecture Literacy**: RAG, fine-tuning, prompting, vector databases, inference pipelines
- [ ] **Tradeoff Fluency**: Latency vs quality, precision vs recall, cost vs accuracy
- [ ] **Safety & Ethics**: Hallucinations, bias, privacy, responsible AI guardrails
- [ ] **Metrics for AI**: How to measure success when output is non-deterministic
- [ ] **Cross-functional Collaboration**: Translate user problems into ML requirements for engineers and researchers

---

## AI Architecture Decision Matrix

### When to Use What

| Approach | Best For | Tradeoffs | Google Example |
|----------|---------|-----------|----------------|
| **Prompting (Zero/Few-shot)** | Simple, well-defined tasks | Fast, cheap, but less controllable | "Summarize this email" in Gmail |
| **RAG (Retrieval-Augmented Generation)** | Knowledge-intensive tasks requiring factual accuracy | Reduces hallucinations, but adds latency (retrieval step) | AI Overviews in Search (grounded in web data) |
| **Fine-tuning** | Domain-specific tasks requiring specialized behavior | Expensive to train, risk of overfitting, but highest quality | Medical or legal document summarization |
| **Agents (Multi-step)** | Complex tasks requiring planning and tool use | Powerful but unpredictable, hard to evaluate | "Book me a flight" via Gemini |
| **On-device (Small models)** | Privacy-sensitive, latency-critical | Limited capability, but no network dependency | Gemini Nano on Pixel (Smart Reply, call screening) |

### The RAG Pipeline (Know This Cold)

```
User Query → Embedding Model → Vector Search (retrieve relevant docs)
                                        ↓
                               Context + Query → LLM → Response
                                        ↓
                               Grounding Check → Safety Filter → User
```

**Key PM decisions in a RAG pipeline:**
1. **Chunk size**: How big are the documents we index? (Tradeoff: bigger = more context, but noisier)
2. **Retrieval quality**: How many documents to retrieve? (Tradeoff: more = better recall, but slower)
3. **Model selection**: Which LLM? (Tradeoff: larger model = better quality, but higher cost/latency)
4. **Grounding**: Do we cite sources? How do we verify factual accuracy?
5. **Safety filters**: What content do we block? How aggressive are the filters?

---

## AI Metrics Framework

Measuring AI products is different from traditional products because outputs are non-deterministic:

| Metric Category | Metrics | Why It Matters |
|----------------|---------|---------------|
| **Quality** | Factual accuracy (human-rated), coherence, relevance | Is the AI output actually *correct*? |
| **Safety** | Hallucination rate, toxicity rate, bias score | Does the AI cause harm? |
| **Performance** | Latency (p50, p99), throughput, cost per query | Is the AI fast and affordable at scale? |
| **User Satisfaction** | CSAT, task completion rate, re-query rate | Does the user actually find it helpful? |
| **Adoption** | Feature activation %, DAU of AI feature, opt-out rate | Are users choosing to use it? |

### Precision vs Recall (You MUST Know This)

| | Predicted Positive | Predicted Negative |
|---|---|---|
| **Actually Positive** | True Positive (TP) | False Negative (FN) — **Missed it** |
| **Actually Negative** | False Positive (FP) — **False alarm** | True Negative (TN) |

- **Precision** = TP / (TP + FP) → "Of the things we flagged, how many were correct?"
- **Recall** = TP / (TP + FN) → "Of all the things that existed, how many did we find?"

**PM Decision**: The tradeoff depends on the product context:
- **Spam filter** → Optimize for *Precision* (don't flag real emails as spam)
- **Cancer detection** → Optimize for *Recall* (don't miss any real cases)
- **Search results** → Balance both (relevant results *and* comprehensive coverage)

---

## AI Safety & Responsible AI (Google-Specific)

Google has published [AI Principles](https://ai.google/responsibility/principles/). Know these:

1. Be socially beneficial
2. Avoid creating or reinforcing unfair bias
3. Be built and tested for safety
4. Be accountable to people
5. Incorporate privacy design principles
6. Uphold high standards of scientific excellence
7. Be made available for uses that accord with these principles

**In an interview, you should proactively discuss:**
- **Hallucinations**: How will you detect and mitigate? (grounding, confidence thresholds, disclaimers)
- **Bias**: How will you test for demographic bias in training data and outputs?
- **Privacy**: Is user data used for training? How do you handle PII?
- **Adversarial attacks**: How do you prevent prompt injection or jailbreaking?
- **User trust**: How does the user know the AI is confident vs uncertain?

---

## Sample AI Product Design Questions

### 1. "Design an AI-powered Study Buddy for students."

**Strong Answer Structure:**
1. **User Segments**: High school students cramming for exams vs college students doing deep research vs lifelong learners
2. **Pain Points**: Can't find the right resources, don't know what they don't know, study alone without feedback
3. **AI Solution**: A conversational tutor powered by Gemini that:
    - Ingests the student's course material (RAG over their notes/textbook)
    - Generates practice questions calibrated to their weak areas
    - Explains concepts using Socratic questioning (doesn't just give answers)
4. **Technical Architecture**: RAG pipeline (student uploads → embedding → vector DB → Gemini generates questions grounded in their material)
5. **Hallucination Guardrail**: All generated answers are grounded in the uploaded source material. If confidence is below threshold, the system says "I'm not sure — here's the relevant section for you to review."
6. **Metrics**: Task completion (% of practice sets completed), knowledge gain (pre/post quiz scores), retention (D7, D28), hallucination rate (human-rated sample)

### 2. "Should we add AI smart replies to Google Chat?"

**Strong Answer Structure:**
1. **User Need**: Speed in workplace communication. People spend too much time typing quick acknowledgments.
2. **The "Should We?" Question**: Is AI the right tool, or is a simple heuristic sufficient?
    - Smart Reply already works well for short responses ("Thanks!", "Sounds good", "Let me check")
    - AI adds value for *contextual* replies that require understanding the thread
3. **Tradeoffs**:
    - **Pro**: Saves time, increases messaging velocity, showcases Gemini in Workspace
    - **Con**: Risk of sending embarrassing/wrong suggestions, privacy concern (AI reads messages), users may over-rely and disengage
4. **Recommendation**: Ship it as opt-in with a staged rollout. Start with low-risk suggestions (acknowledgments), expand to contextual replies. Implement "undo send" as a safety net.
5. **Metrics**: Reply time reduction, adoption rate, suggestion acceptance rate, user-reported errors

### 3. "An AI feature has a 10% higher hallucination rate than expected. How do you troubleshoot?"

**Strong Answer:**
1. **Scope**: Is it all queries or specific categories? (Medical queries vs casual chat?)
2. **Hypotheses**:
    - Training data quality degraded (new data ingestion introduced noise)
    - Retrieval pipeline regression (vector DB returning less relevant chunks)
    - Model update changed behavior (new version has different calibration)
    - Adversarial inputs (users found prompt injection patterns)
3. **Investigation**: Pull a sample of hallucinated outputs. Manually review: Was the correct information in the retrieval context? If yes → model issue. If no → retrieval issue.
4. **Mitigation**: Tighten confidence thresholds (show "I'm not sure" more often). Add grounding citations. Roll back model version if regression is confirmed.
5. **Prevention**: Implement automated hallucination benchmarks in CI/CD. Set up alerts on factual accuracy metrics.

---

## System Design Basics (Traditional Technical Round)

Even in AI-focused rounds, you may be asked general system design:

| Pattern | When to Discuss | Example |
|---------|----------------|---------|
| **Horizontal Scaling** | High traffic, stateless services | "We'd shard user data by user_id across regions" |
| **Caching** | Read-heavy workloads | "Redis cache in front of the DB reduces latency from 200ms to 20ms" |
| **Message Queues** | Async processing | "Pub/Sub for decoupling the ingestion pipeline from the serving layer" |
| **CDN** | Static content delivery | "Edge caching for images and video thumbnails" |
| **Load Balancing** | Traffic distribution | "Round-robin across replicas with health checks" |

---

## Practice Questions

- [ ] "Design an AI-powered email triage system for Gmail"
- [ ] "How would you build a real-time translation feature for Google Meet?"
- [ ] "Should Google Photos use AI to auto-organize albums? Walk me through the architecture."
- [ ] "Design the evaluation framework for Gemini's response quality"
- [ ] "Explain the tradeoff between fine-tuning and RAG for NotebookLM"
- [ ] "An AI feature is occasionally generating toxic content. How do you respond?"
- [ ] "Design an AI agent that can book restaurants on behalf of the user (like Google Duplex 2.0)"

---

## Key Vocabulary (Don't Get Caught Without These)

| Term | What It Means (PM-Level) |
|------|-------------------------|
| **RAG** | Retrieve relevant documents, feed them to an LLM as context → reduces hallucinations |
| **Fine-tuning** | Further training a base model on domain-specific data → better quality, higher cost |
| **Embedding** | Converting text/images into numerical vectors for similarity search |
| **Vector Database** | A database optimized for storing and searching embeddings (e.g., Vertex AI Vector Search) |
| **Inference** | Running a trained model to generate a prediction/response |
| **Latency (p50/p99)** | Median and 99th percentile response time — p99 is what users actually feel |
| **Hallucination** | Model generating plausible-sounding but factually incorrect information |
| **Grounding** | Connecting AI output to verifiable source data (e.g., web search, uploaded documents) |
| **Prompt Injection** | Adversarial input designed to make the model ignore safety instructions |
| **RLHF** | Reinforcement Learning from Human Feedback — how models learn to be "helpful and harmless" |
| **Guardrails** | Safety filters and business rules applied before AI output reaches the user |
| **Token** | The atomic unit of text that LLMs process (~0.75 words per token) |
| **Context Window** | Maximum amount of text the model can "see" at once (e.g., 1M tokens for Gemini) |

---

## Anti-Patterns to Avoid

❌ **"We'd use AI"** without specifying *how* (RAG? Fine-tuning? Prompting?)
❌ **Treating AI as magic** — Every AI capability has limitations and failure modes
❌ **No safety discussion** — Always proactively address hallucinations, bias, and privacy
❌ **Ignoring cost** — AI inference at Google scale is expensive. Show cost awareness.
❌ **Deferring entirely to Engineering** — You don't need to build the model, but you need to make architecture *decisions*
❌ **No metrics for AI** — "It works well" is not a metric. Define precision, recall, hallucination rate, CSAT.

---

## Notes & Learnings

*Add notes from practice sessions and real interviews here*
