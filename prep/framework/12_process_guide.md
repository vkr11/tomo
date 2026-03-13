# Tomo Interview Prep: Process Guide

> **Purpose**: This is the step-by-step execution guide for using the Tomo system to prepare for IC7/D1/CPO interviews. Follow this process sequentially.

---

## Overview: The 5-Phase Process

```
Phase 1: Foundation     → Build career inventory
Phase 2: Enrichment     → Add market intelligence
Phase 3: Mining         → Extract stories from epics
Phase 4: STAR Writing   → Script the stories
Phase 5: Practice       → Mock interviews
```

**Time to Complete**: 6-8 weeks for full readiness.

---

## Phase 1: Foundation (Week 1-2)

### Goal
Convert raw career materials into structured, searchable documents.

### Inputs Required
- [ ] LinkedIn profile (PDF export)
- [ ] Current resume
- [ ] Performance reviews (last 3-5 years)
- [ ] Any self-written notes about your work
- [ ] Target job descriptions

### Process Steps

#### Step 1.1: Create Your Profile Structure
```bash
users/{your_name}/
├── background/
│   ├── career_summary.md       # Your main profile
│   ├── goals.md                # Job search targets
│   ├── project_inventory.md    # All epics/projects
│   └── performance/            # Upload perf reviews here
└── sessions/
    └── {date}_prep_session.md  # Daily prep notes
```

#### Step 1.2: Build `career_summary.md`
Use the template structure:
1. Summary (3-bullet elevator pitch)
2. Key Projects & Achievements (tables by company)
3. PM Education & Thought Leadership
4. Career Timeline
5. Skills & Domains
6. Consulting & Side Projects
7. Leadership & Org Scope
8. Flagship Case Studies (placeholder)
9. Executive Engagement
10. Business Impact Summary
11. Point of View (Thesis)
12. Publications, Patents & Talks
13. Awards & Recognition
14. References & Sponsors
15. Open TODOs

**Time**: 4-6 hours

#### Step 1.3: Build `goals.md`
Define:
- Mission statement
- Target roles (Track A: Big Tech IC7/D1, Track B: Startup CPO)
- Target domains (ranked)
- Evaluation criteria (must-haves, nice-to-haves, deal-breakers)
- Compensation benchmarks
- Timeline
- Target company list
- Success metrics

**Time**: 2-3 hours

#### Step 1.4: Build `project_inventory.md`
List ALL major projects you've worked on:
- Group by company/era
- Define "Epics" (6-18 month initiatives)
- Mark "Story Ready" status
- Add basic context (what it was, when)

**Time**: 3-4 hours

### Outputs
✅ `career_summary.md` (with TODOs marked)  
✅ `goals.md` (with target list)  
✅ `project_inventory.md` (initial list)

---

## Phase 2: Enrichment (Week 2-3)

### Goal
Add external validation, market intelligence, and "why it matters" context to your projects.

### Process Steps

#### Step 2.1: Run Market Research
For each major epic in `project_inventory.md`:

1. Use `keyword_research_prompt.md` with ChatGPT/Gemini
2. Search for:
   - Press releases
   - TechCrunch/The Verge coverage
   - Earnings call mentions
   - Engineering blogs
   - Regulatory filings (if applicable)
3. Extract:
   - Revenue/user scale
   - Technical keywords
   - Why it mattered (regulatory/market context)

**Time**: 1-2 hours per epic

#### Step 2.2: Update `project_inventory.md`
For each epic, add a "Context & Evidence" section with:
- External metrics (e.g., "$10B run-rate")
- Technical depth (e.g., "BISG, MPC, RLHF")
- Strategic narrative (e.g., "Turned settlement into moat")

**Time**: 30 min per epic

### Outputs
✅ Enriched `project_inventory.md` with market intelligence  
✅ High-impact keywords identified  
✅ "So what?" answers for every project

---

## Phase 3: Mining (Week 3-5)

### Goal
Extract the 7 story types from EACH major epic.

### The 7 Story Types (Per Epic)

For EACH epic, you must identify:

1. **Conflict/Influence**: Who did you disagree with? How did you handle it?
2. **Failure/Mistake**: What went wrong? What did you learn?
3. **Ambiguity/Strategy**: What was the hardest decision? How did you make it?
4. **Execution/Grit**: What coordination/timeline challenge did you face?
5. **Technical Depth**: What was the hard technical problem?
6. **Metrics/Data**: What A/B test or metric did you debug?
7. **People/Hiring**: Did you build a team? Who did you hire/develop?

### Process: The Mining Worksheet

#### Step 3.1: Select Your Top 5 Epics
Choose the 5 most significant epics from your career. Criteria:
- Lasted 6-18 months
- Had measurable impact
- Involved multiple challenges
- Demonstrates range (not all the same type of work)

**Recommended**: 
- 1-2 from current role
- 2-3 from previous roles
- Cover different domains (e.g., one Ads, one AI, one Infrastructure)

#### Step 3.2: Create Mining Worksheets
For each epic, create a file: `users/{name}/sessions/epic_mining_{epic_name}.md`

Use this template:

```markdown
# Epic Mining: {Epic Name}

## Epic Context
- **Company**: 
- **Timeframe**: 
- **Your Role**: 
- **Team Size**: 
- **Key Outcome**: 

## Story Type 1: Conflict/Influence
**Question**: "Tell me about a time you had a conflict with a cross-functional partner."

- **Who**: Who did you disagree with? (Name/role)
- **What**: What was the disagreement about?
- **Why**: What were their incentives? Yours?
- **How**: How did you approach it?
- **Outcome**: What happened? Did you win? Compromise? Lose?
- **Lesson**: What would you do differently?

**Maps to**:
- Pillar: 6 (Leadership)
- LP: Have Backbone

---

## Story Type 2: Failure/Mistake
**Question**: "Tell me about a time you failed."

- **What**: What went wrong?
- **Impact**: How bad was it? (Revenue? Users? Timeline?)
- **Why**: Root cause? (Your error? Team? External?)
- **Response**: What did you do to fix it?
- **Lesson**: What did you learn?

**Maps to**:
- Pillar: 6 (Leadership)
- LP: Learn & Be Curious

---

## Story Type 3: Ambiguity/Strategy
**Question**: "What was the hardest decision you made on this project?"

- **The Dilemma**: What were the options?
- **The Stakes**: Why did it matter?
- **Your Bet**: What did you decide?
- **The Reasoning**: How did you decide?
- **Outcome**: Were you right?

**Maps to**:
- Pillar: 1 (Strategy)
- LP: Are Right, A Lot

---

## Story Type 4: Execution/Grit
**Question**: "Tell me about a time you had to ship under pressure."

- **The Pressure**: What was the deadline/constraint?
- **The Blockers**: What got in the way?
- **Your Actions**: What did YOU do? (Not the team)
- **Trade-offs**: What did you sacrifice/de-scope?
- **Outcome**: Did you ship? What was the result?

**Maps to**:
- Pillar: 3 (Execution)
- LP: Deliver Results

---

## Story Type 5: Technical Depth
**Question**: "What was the hardest technical problem you solved?"

- **The Problem**: What was broken/needed building?
- **The Complexity**: Why was it hard? (Scale? Novel?)
- **Your Solution**: What approach did you take?
- **Trade-offs**: Why this vs. alternatives?
- **Outcome**: Did it work? How do you know?

**Maps to**:
- Pillar: 7 (Technical)
- LP: Invent & Simplify

---

## Story Type 6: Metrics/Data
**Question**: "Tell me about a time you debugged a metric drop."

- **The Metric**: What dropped? (DAU? Revenue? Conversion?)
- **The Drop**: How big? When did you notice?
- **Your Hypothesis**: What did you think caused it?
- **The Investigation**: How did you debug?
- **The Fix**: What was the solution?

**Maps to**:
- Pillar: 4 (Metrics)
- LP: Dive Deep

---

## Story Type 7: People/Hiring
**Question**: "Tell me about building a team."

- **The Need**: Why did you need to hire?
- **The Bar**: What profile did you look for?
- **The Process**: How did you source/interview?
- **The Hire**: Who did you bring in?
- **The Impact**: How did they change the team?

**Maps to**:
- Pillar: 5 (Management)
- LP: Hire & Develop the Best

---

## Completeness Check
- [ ] Conflict story extracted
- [ ] Failure story extracted
- [ ] Strategy story extracted
- [ ] Execution story extracted
- [ ] Technical story extracted
- [ ] Metrics story extracted
- [ ] People story extracted
```

#### Step 3.3: Fill In the Worksheets
**Method**:
1. Schedule 1-hour blocks per epic
2. Use performance reviews as memory triggers
3. Ask a colleague/friend to interview you about the project
4. Record yourself talking through it, then transcribe

**Time**: 1-2 hours per epic × 5 epics = 5-10 hours

### Outputs
✅ 5 completed mining worksheets  
✅ 35 story kernels (7 per epic × 5 epics)

---

## Phase 4: STAR Writing (Week 5-6)

### Goal
Convert story kernels into polished STAR narratives.

### Process Steps

#### Step 4.1: Select Your "Core 15"
From the 35 story kernels, pick the 15 strongest:
- The 5 "Essential Stories" from `00_master_guide.md`:
  1. Turnaround
  2. 0→1
  3. People Crisis
  4. Technical Bet
  5. Failure
- 10 supporting stories that cover gaps

#### Step 4.2: Write Full STAR Scripts
For each of the 15, write a 2-minute script:

```markdown
## Story: {Name}

**Setup (20 seconds)**
"At {Company} in {Year}, I was leading {Epic}. The context was {Why it mattered}..."

**Situation (10 seconds)**
"Specifically, {The problem/opportunity}..."

**Task (10 seconds)**
"My job was to {Your specific mandate}..."

**Action (60 seconds)**
"I did three things:
1. {Action 1 + why}
2. {Action 2 + why}
3. {Action 3 + why}"

**Result (20 seconds)**
"{Metric}. This taught me {Principle}."

**Maps to**: Pillar {#}, LP: {Name}
```

**Time**: 30-45 min per story × 15 = 8-12 hours

#### Step 4.3: Practice Out Loud
- Record yourself telling each story
- Listen back: Are you using "I" (not "we")? Are you quantifying?
- Trim to exactly 2 minutes

**Time**: 15 min per story × 15 = 4 hours

### Outputs
✅ 15 polished STAR scripts  
✅ Audio recordings of each

---

## Phase 5: Practice (Week 7-8+)

### Goal
Simulate real interview conditions.

### Process Steps

#### Step 5.1: Mock Interviews
- **Week 7**: 2 mocks (Strategy + Execution)
- **Week 8**: 2 mocks (Leadership + Technical)
- **Ongoing**: 2 mocks/week until interviews

**Use**:
- `00_master_guide.md` for pillar focus
- `11_story_to_pillar_mapping.md` to select stories

#### Step 5.2: Refine After Each Mock
After every mock:
1. What pillar did you struggle with?
2. Go back to that epic's mining worksheet
3. Extract a better story or refine the existing one

### Outputs
✅ 8+ mock interviews completed  
✅ Confidence in story delivery

---

## Daily Execution Checklist

### Week 1-2: Foundation
- [ ] Mon: Gather all materials (LinkedIn, resume, perf reviews)
- [ ] Tue-Wed: Draft `career_summary.md`
- [ ] Thu: Draft `goals.md`
- [ ] Fri: Draft `project_inventory.md`

### Week 2-3: Enrichment
- [ ] Mon: Research Epic 1 (market intel)
- [ ] Tue: Research Epic 2
- [ ] Wed: Research Epic 3
- [ ] Thu: Research Epic 4
- [ ] Fri: Research Epic 5, update inventory

### Week 3-5: Mining
- [ ] Week 3: Mine Epic 1 & 2 (all 7 stories each)
- [ ] Week 4: Mine Epic 3 & 4
- [ ] Week 5: Mine Epic 5, select Core 15

### Week 5-6: STAR Writing
- [ ] Week 5: Write 8 STAR scripts
- [ ] Week 6: Write 7 STAR scripts, record all

### Week 7-8+: Practice
- [ ] 2 mocks per week
- [ ] Refine stories based on feedback
- [ ] Apply to jobs, track in `goals.md`

---

## How to Use This Doc

1. **Start Here**: Read this doc fully before starting.
2. **Track Progress**: Check off items as you complete them.
3. **Link to Framework**: Reference the framework docs as needed:
   - `00_master_guide.md` (8 Pillars)
   - `10_story_building_strategy.md` (Narrative Hierarchy)
   - `amazon_leadership_principles.md` (LP Mapping)
   - `11_story_to_pillar_mapping.md` (Bridge)
4. **Iterate**: This is not linear. You'll refine stories as you practice.

---

## Common Pitfalls to Avoid

| Pitfall | How to Fix |
|---------|------------|
| **"We" instead of "I"** | In every story, ask "What did I PERSONALLY do?" |
| **No metrics** | Every result needs a number (%, $, users, time) |
| **Too much context** | Situation should be 10 seconds, not 2 minutes |
| **No lesson** | Every story must end with "This taught me..." |
| **Memorizing word-for-word** | Practice the structure, not the script |
| **Skipping mining** | You can't write good STARs without mining first |

---

## When You're Done

You should have:
- ✅ 5 deeply mined epics (35 story kernels)
- ✅ 15 polished STAR scripts
- ✅ Clear mapping to all 8 pillars
- ✅ Confidence to answer ANY behavioral question
- ✅ Ready for IC7/D1/CPO interviews

---

*Last updated: 2026-01-18*
