# Tomo Onboarding Guide

> **Purpose**: This document outlines how to onboard a new user to the Tomo interview prep system. It defines what information to collect, how to structure their profile, and how to help them build compelling career narratives.

---

## 1. Overview

Tomo is a structured system for interview preparation that helps candidates:
1. **Organize** their career history and achievements
2. **Define** clear job search goals and target roles
3. **Build** compelling STAR-format case studies
4. **Prepare** for senior-level interviews (IC7/D1, VP, CPO)

---

## 2. Onboarding Checklist

### Phase 1: Collect Raw Materials

| Document | Purpose | Format | Required? |
|----------|---------|--------|-----------|
| **LinkedIn Profile** | Career timeline, roles, companies | PDF export or URL | ✅ Yes |
| **Resume** | Polished summary of experience | PDF/DOCX | ✅ Yes |
| **Performance Reviews** | Ratings, feedback, projects | PDF/Text | ⚠️ Highly Recommended |
| **Self-Reviews** | Candidate's own view of their work | Text | ⚠️ Highly Recommended |
| **Manager Feedback** | 360 feedback, peer reviews | Text | Optional |
| **Awards/Recognition** | Internal or external awards | List | Optional |
| **Patents/Publications** | Thought leadership proof | Links/PDFs | Optional |
| **Job Descriptions** | Target roles they're pursuing | Links/PDFs | ✅ Yes |

### Phase 2: Conduct Intake Interview

Ask the candidate the following questions:

#### A. Career Goals
1. What type of role are you targeting? (IC vs. People Manager)
2. What level? (Staff, Principal, Director, VP, CPO)
3. What company type? (Big Tech, Growth Startup, Early Stage)
4. What domains interest you most?
5. What's your timeline for landing a new role?
6. Are you open to relocation? Remote-only?
7. What's your compensation expectation?

#### B. Career Highlights
1. What are the 3–5 projects you're most proud of?
2. For each project:
   - What was the situation/context?
   - What was your specific role?
   - What actions did YOU take?
   - What was the measurable result?
   - What did you learn?
3. What's the largest team you've managed?
4. What's the biggest revenue/cost/risk impact you've had?
5. What executives have you worked with directly?

#### C. Gaps & Development Areas
1. What areas do you want to improve?
2. What questions do you struggle to answer in interviews?
3. What's your biggest career regret or pivot?
4. What feedback have you received that was hard to hear?

#### D. Values & Preferences
1. What kind of manager do you work best with?
2. What kind of company culture do you thrive in?
3. What's a deal-breaker for you in a job?
4. Why are you leaving your current role? (if applicable)

---

## 3. Profile Structure

After collecting inputs, create the following files in `users/{username}/background/`:

```
users/
└── {username}/
    └── background/
        ├── career_summary.md      # Main profile document
        ├── goals.md               # Job search objectives
        ├── project_inventory.md   # Full list of projects
        ├── linkedin-profile.pdf   # Raw LinkedIn export
        ├── linkedin-profile.txt   # Extracted text from LinkedIn
        └── performance/           # Performance reviews (if provided)
            ├── 2024_h1.md
            ├── 2023_h2.md
            └── ...
    └── resources/
        └── keyword_research_prompt.md # SEO & Market Intel prompt
```

---

## 4. Career Summary Template

The `career_summary.md` should include the following sections:

| Section | Purpose |
|---------|---------|
| **1. Summary** | 3-bullet elevator pitch |
| **2. Key Projects & Achievements** | Tables grouped by company/initiative |
| **3. PM Education & Thought Leadership** | Teaching, writing, speaking |
| **4. Career Timeline** | Chronological roles with highlights |
| **5. Skills & Domains** | Core competencies |
| **6. Consulting & Side Projects** | Active side work |
| **7. Leadership & Org Scope** | Team sizes, XFN partners |
| **8. Flagship Case Studies (STAR)** | 2–3 deep narratives |
| **9. Executive Engagement** | C-suite interactions |
| **10. Business Impact Summary** | Consolidated metrics |
| **11. Point of View (Thesis)** | What they believe |
| **12. Publications, Patents & Talks** | Thought leadership |
| **13. Awards & Recognition** | Validation |
| **14. References & Sponsors** | Key relationships |
| **15. Open TODOs** | Prep checklist |

---

## 5. Goals Template

The `goals.md` should include:

| Section | Purpose |
|---------|---------|
| **1. Mission Statement** | One-liner career objective |
| **2. Target Roles** | Tracks (Big Tech IC vs. Startup Leader) |
| **3. Target Domains** | Ranked preferences |
| **4. Evaluation Criteria** | Must-haves, nice-to-haves, deal-breakers |
| **5. Compensation Benchmarks** | Salary + equity expectations |
| **6. Job Search Timeline** | Phased plan |
| **7. Target Company List** | Draft list with checkboxes |
| **8. Success Metrics** | Quantified goals |
| **9. Open Questions** | Decisions to revisit |

---

## 6. Case Study Development

For each flagship project, guide the candidate through STAR:

### STAR Framework

| Element | Prompt Questions |
|---------|------------------|
| **Situation** | What was the context? What problem existed? Why did it matter? |
| **Task** | What were YOU specifically asked to do? What was your mandate? |
| **Action** | What actions did YOU take? (Not the team — YOU.) Be specific. |
| **Result** | What was the measurable outcome? Revenue, users, risk mitigated? |
| **Lesson** | What did you learn? What would you do differently? |

### Case Study Selection Criteria

Choose 2–3 projects that demonstrate:
- [ ] **Strategic thinking** — ambiguous problem, you created the roadmap
- [ ] **Execution excellence** — shipped something complex on time
- [ ] **Cross-functional leadership** — led eng, design, legal, policy
- [ ] **Business impact** — quantifiable revenue/cost/risk outcome
- [ ] **Adversity/failure** — handled a setback, pivoted, learned

---

## 7. Interview Prep Workflow

Once profile is complete, guide candidate through:

### Week 1–2: Foundation
- [ ] Finalize career_summary.md
- [ ] Complete goals.md
- [ ] **Run Keyword Research:** Use `keyword_research_prompt.md` with an LLM
- [ ] **Optimize SEO:** Update Resume and LinkedIn with high-signal keywords
- [ ] Identify 3 flagship case studies

### Week 3–4: Story Development
- [ ] Write full STAR narratives for each case study
- [ ] Practice telling each story in 5 min, 10 min, 15 min versions
- [ ] Identify "so what" and "why it matters" for each

### Week 5–6: Mock Interviews
- [ ] Product Sense mock
- [ ] Execution mock
- [ ] Leadership & Drive mock
- [ ] Technical mock (if applicable)

### Week 7+: Active Search
- [ ] Apply to target list
- [ ] Track applications in goals.md
- [ ] Debrief after each interview

---

## 8. Common Pitfalls to Avoid

| Pitfall | How to Fix |
|---------|------------|
| **Too generic** | Push for specific metrics and actions |
| **"We" instead of "I"** | Ask "What did YOU do?" repeatedly |
| **Missing impact** | Ask "So what? Why did it matter?" |
| **Too much context** | Keep Situation to 2–3 sentences |
| **No lessons learned** | Every story needs a reflection |
| **Underselling** | Help them own their achievements |

---

## 9. Sample Intake Questions Script

Use this script during the onboarding call:

```
INTRO
"Let's spend 45–60 minutes building your career profile. I'll ask you 
about your background, goals, and key projects. Don't worry about 
being polished — we'll refine everything together."

GOALS (10 min)
"Let's start with what you're looking for..."
- What type of role?
- What level?
- What companies?
- What timeline?

CAREER OVERVIEW (10 min)
"Walk me through your career at a high level..."
- Major roles and transitions
- Key inflection points

DEEP DIVES (30 min)
"Now let's go deep on 2–3 projects..."
- Pick your most impactful project
- [STAR questions for each]

WRAP-UP (5 min)
"What questions do you have for me?"
"What feels unclear or incomplete?"
```

---

## 10. File Naming Conventions

| File Type | Naming Convention | Example |
|-----------|-------------------|---------|
| LinkedIn export | `linkedin-profile-{date}.pdf` | `linkedin-profile-18-jan-2025.pdf` |
| Performance review | `{year}_{half}.md` | `2024_h1.md` |
| Case study | `case_{project_name}.md` | `case_llama_safety.md` |
| Target company notes | `company_{name}.md` | `company_openai.md` |

---

*Last updated: 2026-01-18*
