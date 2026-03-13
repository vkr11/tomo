# Technical Framework

> **Goal**: Demonstrate ability to partner with Eng on system-level decisions
>
> | Dimension | Description |
> |-----------|-------------|
> | **Signals** | Tradeoff fluency, scalability awareness, data pipeline understanding, build-vs-buy judgment |
> | **Weak Answer** | Superficial ("use microservices"), can't explain why, defers entirely to Eng |
> | **Strong Answer** | Articulates tradeoffs (latency vs consistency), understands infra cost implications, proposes phased approach |
> | **IC5/IC6** | "I'd use a NoSQL database for flexibility" |
> | **IC7/D1** | "At our scale (10M DAU), I'd start with Postgres for ACID, shard by user_id at 50M, and evaluate DynamoDB for the activity feed due to write-heavy pattern. Here's the cost model." |

---

## Core Signals to Show

- [ ] Tradeoff fluency
- [ ] Scalability awareness
- [ ] Data pipeline understanding
- [ ] Build-vs-buy judgment
- [ ] Cost model awareness

---

## Common Question Types

| Question | Key Elements to Address |
|----------|------------------------|
| "Design a system for X" | Components, data flow, scale considerations |
| "Which database?" | Use case fit, tradeoffs, scale path |
| "How would you scale 10x?" | Bottlenecks, horizontal vs vertical, caching |
| "Build or buy?" | Cost model, time-to-market, strategic control |
| "Where's the bottleneck?" | System debugging, profiling approach |

---

## My Framework/Approach

### Step 1: Clarify Requirements
*Questions I ask to scope the system*

```
[ Define your clarifying questions ]
- Scale: users, requests/sec, data volume?
- Latency requirements?
- Consistency vs availability tradeoff?
- Read vs write heavy?
```

### Step 2: High-Level Architecture
*How I structure the system*

```
[ Component diagram approach ]
- Client → API → Service → Data
- Caching layer
- Message queues for async
```

### Step 3: Data Model
*How I design the data layer*

```
[ Schema design, database choice rationale ]
```

### Step 4: Scale & Performance
*How I address scaling*

```
[ Horizontal scaling, sharding, caching strategy ]
```

### Step 5: Tradeoffs
*How I articulate tradeoffs*

```
[ Consistency vs availability, latency vs throughput, etc. ]
```

---

## Database Decision Matrix

| Type | Best For | Tradeoffs |
|------|----------|-----------|
| **Postgres** | ACID, relational data | Vertical scale limits |
| **MySQL** | Read-heavy, simple queries | Same as Postgres |
| **DynamoDB** | Write-heavy, key-value | No joins, eventual consistency |
| **MongoDB** | Flexible schema, documents | Scale complexity |
| **Redis** | Caching, sessions | Memory limits |
| **Elasticsearch** | Search, analytics | Operational overhead |

---

## Build vs Buy Framework

| Factor | Build | Buy |
|--------|-------|-----|
| **Control** | Full customization | Vendor roadmap |
| **Time** | Longer | Faster |
| **Cost (short)** | Higher | Lower |
| **Cost (long)** | Lower | License fees |
| **Expertise** | Need to hire/grow | Outsourced |
| **Strategic** | Core competency | Commodity |

**Default heuristic**: Buy commodities, build differentiators.

---

## Key Stories (IC7/D1 Level)

### Story 1: [Title]
**Situation**: 
**Task**: 
**Action**: 
**Result**: 
**IC7 Signal**: 

### Story 2: [Title]
**Situation**: 
**Task**: 
**Action**: 
**Result**: 
**IC7 Signal**: 

---

## Practice Questions

- [ ] "Design a system for [use case]"
- [ ] "How would you scale this to 100x users?"
- [ ] "Should we build or buy [capability]?"
- [ ] "Where's the bottleneck in this system?"

---

## Key Phrases & Terminology

| Term | When to Use |
|------|-------------|
| "At our scale (X DAU)..." | When grounding in reality |
| "Shard by [key] at [threshold]" | When discussing scaling |
| "CAP theorem tradeoff" | When discussing distributed systems |
| "Here's the cost model" | When discussing build vs buy |

---

## System Design Patterns

### Scaling Patterns
- **Horizontal scaling**: Add more machines
- **Vertical scaling**: Bigger machines
- **Sharding**: Partition data by key
- **Caching**: Reduce database load
- **CDN**: Edge caching for static content

### Reliability Patterns
- **Load balancing**: Distribute traffic
- **Circuit breaker**: Fail fast on dependencies
- **Retry with backoff**: Handle transient failures
- **Bulkhead**: Isolate failures

---

## Anti-Patterns to Avoid

❌ Superficial answers ("use microservices")  
❌ Can't explain WHY a choice  
❌ Defer entirely to Eng  
❌ No awareness of cost implications  

---

## Notes & Learnings

*Add notes from practice sessions and real interviews here*
