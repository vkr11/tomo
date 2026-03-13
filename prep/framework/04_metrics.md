# Metrics & Experimentation Framework

> **Goal**: Demonstrate analytical rigor and data-driven decision making
>
> | Dimension | Description |
> |-----------|-------------|
> | **Signals** | Metric selection, counter-metric awareness, experiment design, debugging methodology |
> | **Weak Answer** | Picks vanity metrics, no counter-metrics, can't explain statistical significance |
> | **Strong Answer** | North star + guardrails, explains leading vs lagging, designs clean experiments, debugs systematically |
> | **IC5/IC6** | "I'd measure DAU and retention" |
> | **IC7/D1** | "North star: Weekly active creators. Guardrails: Consumer D7 retention, support ticket rate. I'd run a 5% holdback for 4 weeks to detect long-term effects. If DAU rises but creator churn spikes, we've failed." |

---

## Core Signals to Show

- [ ] Metric selection logic
- [ ] Counter-metric awareness
- [ ] Experiment design rigor
- [ ] Debugging methodology
- [ ] Statistical fluency

---

## Common Question Types

| Question | Key Elements to Address |
|----------|------------------------|
| "Define metrics for X" | North star, leading/lagging, guardrails |
| "Why did metric Y drop?" | Debugging framework, hypothesis tree |
| "Design an A/B test" | Hypothesis, variants, sample size, duration |
| "What's the counter-metric?" | Tradeoff awareness, unintended consequences |
| "How do you make tradeoffs?" | Framework for competing metrics |

---

## My Framework/Approach

### Step 1: Metric Selection
*How I choose the right metrics*

```
[ Your approach to selecting metrics ]
1. Start with user/business value
2. Define North Star metric
3. Identify leading indicators
4. Add guardrail metrics
5. Consider counter-metrics
```

### Step 2: Metric Hierarchy
*How I structure metrics*

```
North Star
├── Leading Indicator 1
├── Leading Indicator 2
├── Guardrail 1
└── Guardrail 2
```

### Step 3: A/B Test Design
*How I design experiments*

```
[ Your experiment design approach ]
1. Hypothesis: If X, then Y
2. Variants: Control + Treatment(s)
3. Sample size: MDE, power, duration
4. Randomization: unit of analysis
5. Success criteria: primary + guardrails
```

### Step 4: Debugging
*How I diagnose metric changes*

```
[ Your debugging framework ]
1. Validate data: Is it real?
2. Segment: Who/what/when?
3. Correlate: What else changed?
4. Hypothesize: Root cause candidates
5. Test: Validate with data
```

---

## Metric Framework Template

| Component | Definition | Example |
|-----------|------------|---------|
| **North Star** | Ultimate measure of value | Weekly Active Creators |
| **Leading Indicator** | Predicts future north star | Day 1 content creation |
| **Lagging Indicator** | Confirms past success | Monthly revenue |
| **Guardrail** | Things not to break | D7 retention, support tickets |
| **Counter-metric** | Tradeoff to monitor | Consumer engagement |

---

## A/B Test Checklist

### Before Launch
- [ ] Clear hypothesis documented
- [ ] Primary metric defined
- [ ] Counter-metrics identified
- [ ] Sample size calculated
- [ ] Duration determined
- [ ] Randomization verified
- [ ] Logging validated

### During Experiment
- [ ] Monitor for bugs/SRM
- [ ] Check guardrails
- [ ] No peeking (p-hacking)

### After Experiment
- [ ] Statistical significance
- [ ] Practical significance
- [ ] Segment analysis
- [ ] Learn from negative results
- [ ] Document learnings

---

## Debugging Decision Tree

```
Metric dropped
├── Is data correct?
│   ├── No → Fix instrumentation
│   └── Yes → Continue
├── Global or segmented?
│   ├── Global → External factor?
│   └── Segmented → Which segment?
├── When did it start?
│   └── Correlate with releases/events
├── What else changed?
│   └── Correlated metrics
└── Root cause hypothesis
    └── Test with experiment/data
```

---

## Key Stories (IC7/D1 Level)

### Story 1: [Title]
**Situation**: 
**Metric Challenge**: 
**Action**: 
**Result**: 
**IC7 Signal**: 

### Story 2: [Title]
**Situation**: 
**Metric Challenge**: 
**Action**: 
**Result**: 
**IC7 Signal**: 

---

## Practice Questions

- [ ] "Define success metrics for [product]"
- [ ] "Metric X dropped 10%—how do you debug?"
- [ ] "Design an A/B test for [feature]"
- [ ] "What are the counter-metrics for [change]?"

---

## Key Phrases & Terminology

| Term | When to Use |
|------|-------------|
| "North star + guardrails" | When defining metric system |
| "Leading vs lagging" | When showing temporal awareness |
| "5% holdback for 4 weeks" | When discussing long-term effects |
| "Sample ratio mismatch" | When discussing experiment validity |

---

## Statistical Concepts to Know

| Concept | Quick Definition |
|---------|-----------------|
| **p-value** | Probability of result if null is true |
| **Power** | Probability of detecting true effect |
| **MDE** | Minimum Detectable Effect |
| **Confidence interval** | Range of plausible effect sizes |
| **Sample ratio mismatch** | Unequal split indicating bug |
| **Novelty effect** | Short-term behavior change |
| **Primacy effect** | Long-term habituation |

---

## Anti-Patterns to Avoid

❌ Vanity metrics (DAU without context)  
❌ No counter-metrics  
❌ Can't explain statistical significance  
❌ No debugging structure  

---

## Notes & Learnings

*Add notes from practice sessions and real interviews here*
