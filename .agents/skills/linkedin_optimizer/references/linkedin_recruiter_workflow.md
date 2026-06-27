# How Recruiters Use LinkedIn Recruiter (2025-2026)
> *An operational teardown of the SaaS product that recruiters use to filter, rank, and source candidates. Understanding this UI dictates how we optimize profiles.*

LinkedIn Recruiter is a separate $10,000/year enterprise product, entirely distinct from the standard LinkedIn interface. It functions as an applicant tracking and pipeline management system.

## 1. The Sourcing Workflow

When a recruiter opens a new requisition (e.g., "Director of Product, AI"), they don't browse the feed. They execute a highly structured, data-driven workflow:

1. **Project Setup:** The recruiter creates a "Project" (essentially a folder for the specific job opening).
2. **Search String (The Funnel Top):** They enter a Boolean search or use the new "AI-Assisted Search" (which translates natural language into Boolean queries). Example: `("Director of Product" OR "Head of Product") AND ("Generative AI" OR "LLM") AND "San Francisco"`.
3. **Filter Application (The Hard Gates):** They apply strict metadata filters. There are 40+ granular filters available. The most heavily used are:
   - **Current Job Title** (This is why picking from the standardized dropdown is critical)
   - **Locations**
   - **Skills** (Must match exact taxonomy)
   - **Years of Experience**
4. **Spotlights (The Engagement Filter):** They apply "Spotlight" filters to immediately surface candidates most likely to respond:
   - *Open to Work* (Private/Recruiter-only signal)
   - *Engaged with Talent Brand* (Follows the company page)
   - *Company Alumni*
5. **The Candidate Card (The 6-Second Review):** The search results page does NOT show full profiles. It shows a list of "Candidate Cards." The recruiter makes a Yes/No/Skip decision right here.

---

## 2. Anatomy of the Candidate Card
The Candidate Card is the most critical piece of real estate on LinkedIn. If your Candidate Card doesn't hook the recruiter, they will never click to see your full profile. 

**What the Recruiter sees on the card:**
- Profile Photo & Name
- **Headline** (This is the only free-text hook you control directly on the card)
- **Current Position & Company** 
- **Past 2 Positions**
- **Education**
- **Top Shared Connections**
- **"Likelihood of Interest" indicators** (Open to Work, followed company)

**What is EXCLUDED from the Candidate Card:**
- The About Section
- Experience bullet points
- Recommendations
- Publications/Projects

> 💡 **Optimization Insight:** Your Headline must do 90% of the heavy lifting. It cannot just be your title. It must contain your seniority, your domain, and your primary proof-point. 

---

## 3. Recruiter vs. Recruiter Lite
It is important to know the difference in the software the person on the other end is using:
- **Corporate Recruiter ($10k+/yr):** Has access to the entire LinkedIn network (1st, 2nd, and 3rd-degree connections). Has access to advanced filters like "Years in Current Position" and complex Spotlights.
- **Recruiter Lite ($1.5k/yr, often used by agency recruiters or small startups):** Can only search 1st, 2nd, and 3rd-degree connections. Has fewer filters.

---

## 4. Operational Best Practices (From the Recruiter's Perspective)

1. **Recency Bias:** Modern recruiters filter by the *most recent 3-5 years of experience*. They don't care if you coded in Python 15 years ago. If the target skill isn't clustered in your top 2 roles, you get filtered out.
2. **Company-First Sourcing:** Executive recruiters often don't start with Job Titles. They start with **Target Companies** (e.g., "Show me everyone at Meta, Google, and OpenAI"). Then they filter that subset by department or function. This is why having a Tier 1 company on your resume acts as a massive gravity well for search volume.
3. **Pipeline velocity:** They have monthly quotas. They will overwhelmingly click on the "Open to Work" tab before they look at the "All Candidates" tab, because OTW candidates have a 3x higher response rate, allowing the recruiter to hit their sourcing targets faster.
