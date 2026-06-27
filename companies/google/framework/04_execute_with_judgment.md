# Pillar 4: Execute with Judgment

> **Google's Definition**: "Balance level of detail with prioritization. Understand the product lifecycle, including technical and non-technical considerations for launching or sunsetting products."
>
> | Dimension | Description |
> |-----------|-------------|
> | **Primary Signal** | Can you ship products through ambiguity, make tough tradeoffs, and manage the full lifecycle (build → launch → scale → sunset)? |
> | **Weak Answer** | Idealistic plans with no constraints. No awareness of tradeoffs. Avoids hard calls (sunset, descope). Doesn't mention stakeholder alignment. |
> | **Strong Answer** | Acknowledges constraints (time, resources, quality). Makes explicit tradeoff decisions. Considers the full lifecycle. Manages stakeholders through difficult calls. Shows judgment under pressure. |
> | **L5/L6** | "I'd build a roadmap and execute against it." |
> | **L7** | "Given the constraint of [X], I'd descope [Y] to protect the critical path. Here's how I'd communicate that tradeoff to Engineering, Sales, and Leadership. And here's my kill criteria if the bet doesn't work..." |

---

## Core Signals to Show

- [ ] **Prioritization Under Constraints**: Ship the right thing, not everything
- [ ] **Tradeoff Articulation**: Explicitly state what you're sacrificing and why
- [ ] **Lifecycle Awareness**: Build → Launch → Measure → Iterate → Sunset
- [ ] **Stakeholder Management**: Align XFN partners through difficult decisions
- [ ] **Kill Criteria**: Know when to sunset or pivot — and have the courage to do it

---

## Execution Frameworks

### The Iron Triangle

Every product decision is a tradeoff between these three constraints. You can only optimize two:

```
        SCOPE
       /     \
      /       \
  SCHEDULE --- RESOURCES
```

**Google Calibration**: Google generally optimizes for **Scope (quality) + Resources (talent)** and lets **Schedule flex** — they famously delay launches to get it right. Show that you understand this cultural preference, but also that you know when speed matters (competitive threats, market timing).

### The Launch Decision Matrix

| Question | If Yes | If No |
|----------|--------|-------|
| Does it meet the quality bar? | Proceed | Delay or descope |
| Is it safe? (privacy, security, bias) | Proceed | **Hard stop** — fix first |
| Do we have measurement in place? | Proceed | Instrument first |
| Have stakeholders been aligned? | Proceed | Align before launch |
| Do we have a rollback plan? | Proceed | Build one |

### The Sunset Framework

| Step | What to Do |
|------|-----------|
| **1. Data Case** | Is usage declining? Is the cost of maintenance > value delivered? |
| **2. Migration Path** | Where do current users go? Is there a graceful transition? |
| **3. Communication** | Give ample notice. Explain the *why*. Offer alternatives. |
| **4. Execution** | Staged wind-down, not a cliff. Monitor for edge cases. |

---

## Google's Official Sample Questions

### 1. "Pick a product of your choice. What are its goals? What's in your monthly business review deck?"

**Strong Answer (Example: Google Maps):**
- **North Star Goal**: Help every person navigate and understand the physical world
- **Business Objective**: Drive local commerce revenue (Maps ads, local business profiles)
- **Monthly Business Review Deck**:
    1. **Health Metrics**: DAU, Navigation starts, ETA accuracy, crash rate
    2. **Growth Metrics**: New user acquisition by geo, Maps SDK adoption by partners
    3. **Revenue Metrics**: Local ads revenue, cost-per-click trends, advertiser count
    4. **Quality Metrics**: User-reported errors, map freshness, Street View coverage gaps
    5. **Strategic Bets**: AI-powered features adoption (Immersive View, EV routing), Gemini integration progress
    6. **Risks & Blockers**: Regulatory changes (EU DMA), data partnership renewals

### 2. "A strategically important app is 1 month from launch but below CSAT targets. What do you do?"

**Strong Answer:**
1. **Diagnose**: What specifically is driving low CSAT? Is it a single critical bug, overall polish, or a fundamental UX problem?
2. **Triage into buckets**:
    - **Must-fix (blocks launch)**: Critical bugs, safety issues, broken core flows
    - **Should-fix (degrades but doesn't block)**: Performance issues, minor UX friction
    - **Nice-to-fix (post-launch)**: Polish, edge cases, secondary flows
3. **The Decision**:
    - If must-fix items can be resolved in 1 month → **Ship on time** with a post-launch polish sprint
    - If must-fix items require more time → **Delay launch**. A bad launch for a "strategically important" app damages brand trust and is harder to recover from than a delay
4. **Communicate**: Present the tradeoff to leadership with data: "Here are the 3 must-fix items, their estimated effort, and the risk of launching without them. My recommendation is [ship/delay] because [reason]."

### 3. "Imagine I'm a VC offering you $20M to build any technology-enabled product. How would you get started?"

**Strong Answer:**
1. **Problem Space** (Week 1-2): Identify 3 large, underserved markets with structural tailwinds (AI, regulation, demographics). Interview 20+ potential users.
2. **Validation** (Week 3-4): Pick the biggest pain point with the highest willingness-to-pay. Build a concierge MVP (manual behind the scenes, polished front-end).
3. **Unit Economics** (Month 2): Validate CAC, LTV, and margin. Can this be a venture-scale business ($1B+ TAM)?
4. **Build** (Month 3-6): Hire a small, senior engineering team. Ship V1. Obsess over one metric (activation rate).
5. **Scale** (Month 6-12): Find the growth loop (viral, content, sales-led). Allocate remaining capital to the proven channel.
6. **Key Principle**: "Fall in love with the problem, not the solution. Be ready to pivot the product, but never the mission."

---

## The OKR Framework (Google's Operating System)

Google runs on OKRs. You must speak this language fluently:

| Component | Definition | Example |
|-----------|-----------|---------|
| **Objective** | Qualitative, ambitious, inspirational | "Make Google Maps the world's most trusted navigation tool" |
| **Key Result 1** | Quantitative, measurable, time-bound | "Increase navigation starts by 15% in Q3" |
| **Key Result 2** | Quantitative, measurable, time-bound | "Reduce ETA error rate from 12% to 8%" |
| **Key Result 3** | Quantitative, measurable, time-bound | "Launch AI-powered parking predictions in 5 metros" |

**Google norm**: OKRs should be 60-70% achievable. If you're hitting 100%, you're not being ambitious enough.

---

## Practice Questions

- [ ] "You have 3 engineers and 6 months. Prioritize these 10 features for YouTube."
- [ ] "Should Google sunset Hangouts? Walk me through the decision."
- [ ] "Your team just shipped a feature that's getting negative press. What do you do?"
- [ ] "Write Q3 OKRs for Google Photos."
- [ ] "You're PM for Gmail. The CEO wants a complete redesign. How do you approach this?"
- [ ] "A partner API your product depends on is being deprecated in 90 days. Walk me through your plan."

---

## Anti-Patterns to Avoid

❌ **Over-promising** — "We'll build all 10 features in Q1" (unrealistic without tradeoffs)
❌ **Avoiding the hard call** — Show you can say "no" to features, stakeholders, and even executives
❌ **No rollback plan** — Every launch should have a revert strategy
❌ **Ignoring maintenance cost** — Every feature you ship, you own forever
❌ **No kill criteria** — Define upfront: "If [metric] doesn't hit [threshold] by [date], we sunset/pivot"

---

## Key Phrases & Terminology

| Phrase | When to Use |
|--------|-------------|
| "Given the constraints, I'd prioritize..." | When making tradeoff decisions |
| "The kill criteria would be..." | When proposing a new bet |
| "I'd descope [X] to protect the critical path" | When managing schedule pressure |
| "Here's how I'd communicate this to [stakeholder]..." | When showing stakeholder management |
| "The OKR I'd set is..." | When framing goals |

---

## Notes & Learnings

*Add notes from practice sessions and real interviews here*
