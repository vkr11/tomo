---
title: "Design for Learning"
date: 2025-10-23
slug: design-for-learning
url: https://aparnacd.substack.com/p/design-for-learning
audience: everyone
---

# Design for Learning

*(Part of the “Designing Intelligent Products” series, the first part starts [here](https://open.substack.com/pub/aparnacd/p/designing-intelligent-products)).*

Richard Sutton’s Bitter Lesson observed that systems built to learn eventually surpass those built by hand. I’ve [previously](https://open.substack.com/pub/aparnacd/p/the-bitter-lesson-product-version) wondered whether that same law applies to design. Will simpler, learned interfaces eventually outperform the most polished handcrafted ones?

[![](images/design-for-learning/8bee75357de3.jpeg)](https://substackcdn.com/image/fetch/$s_!KtPE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7708d7a-a7cd-48e4-97c9-cc0167b603af_3166x1634.jpeg)

But what does it mean to design an intelligent product for ***learning***?

Every product relies on two learning loops.

1. The **feedback** loop turns user interaction into data for improvement.
2. The **evaluation** loop ensures that the improvement actually happened in the product.

Both these learning loops have always existed through the eras of computing. What's changed over time though is where the learning happens, and who performs it.

### **PC Era: Manual Learning Loops**

In the beginning, all learning happened outside the software itself. Developers wrote rules, QA teams discovered flaws and verified fixes and users shared feedback, but spread across months if not years.

[![](images/design-for-learning/e2a33cf8bf9c.jpeg)](https://substackcdn.com/image/fetch/$s_!QF39!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F57865641-4fc3-4cca-86de-1a94a5647f04_3770x2127.jpeg)

Manual feedback loops: bug reports, checklists, manual QA

### **Web Era: Programmatic Learning Loops**

The web era compressed the distance between use and improvement.

In the PC era, learning was slow and sequential. A bug had to be reported, fixed, tested, and shipped. The web introduced feedback that was continuous and machine-readable. User interactions could be logged automatically, aggregated, and analyzed. The learning loops became **programmatic** instead of **manual**.

The **click** to me was the most universal of these learning primitives of the web era. It was small, clear, and measurable and every click represented a trace of intent, and when billions of them accumulated, patterns emerged.

When I worked on Google Search, we saw this transformation firsthand. Clicks, dwell time, and query reformulations all flowed back into the ranking algorithms. The system started to adapt at the pace of usage. At first, engineers still closed the loop by hand, studying data and tuning ranking signals. Over time, machine learning models start to absorb those same signals automatically, predicting which results would satisfy a query.

[![](images/design-for-learning/dd749fec62a4.jpeg)](https://substackcdn.com/image/fetch/$s_!90SC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd3c8661d-6904-4150-b353-4dfa1e1aaba5_3948x2259.jpeg)

Web Era: Programmatic Learning Loops

The evaluation loop evolved in parallel as well. QA was no longer just about whether buttons worked or pages loaded. It was about the relevance of results and the quality of ranking. Each proposed algorithmic change was tested against a fixed set of queries, and human raters judged whether the new results improved the experience.

We talk about the importance of evals and benchmarks a lot these days, but to me this was the real beginning of the **era of evals** that are automated, continuous, and grounded in data rather than manual inspection. Yet even here, the signals remained indirect. Clicks and rater judgments shaped algorithms statistically and in aggregate, not through a direct understanding of cause and effect.

### **AI Era: Self-learning Loops**

The AI era pushes learning inside the model system. Models now determine the algorithms that determine behavior. Each user action e.g. accepting, editing, or rejecting a generated output, becomes a signal that can update the model’s internal policy. Reinforcement learning ties each reward to the reasoning that produced it.

Instead of a human deciding to tweak the algorithm based on user actions like clicks, you can feed the rewardable actions directly back into the model. In other words, learning no longer happens *around* the model and instead happens *within* it.

[![](images/design-for-learning/6f7b277bb990.jpeg)](https://substackcdn.com/image/fetch/$s_!NR8Q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e4f67d8-b8f4-43ef-9cb6-bed98d12c7d4_3579x2204.jpeg)

AI Era: Self Learning Loops

### **From Usability to Learnability**

The goal of UX design has typically been about **usability**, teaching users how to use the product.

With AI products, UX design has an equally important other goal of **learnability**, teaching products how to learn from people.

It begins with defining **rewardable product primitives,** small, clear, frequent actions that map directly to model improvement.

For example:

* In coding tools, a Tab acceptance or edit creates a high-fidelity learning signal.

[![](images/design-for-learning/77bdbc673e2f.jpeg)](https://substackcdn.com/image/fetch/$s_!sieX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1ad256be-6787-49fb-bfa2-34be2acad193_3903x2507.jpeg)

* In writing assistants, keeping or deleting generated text trains the model on tone and relevance.
* In productivity tools, confirming or dismissing a suggestion calibrates confidence.

[![](images/design-for-learning/28951fe88292.jpeg)](https://substackcdn.com/image/fetch/$s_!51p3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4159b393-d8f1-4d72-beac-58ed89bcd780_3990x1846.jpeg)

I think we have the opportunity to design new product primitives that are the grammar of learnable systems, turning user interaction into structured, targeted, high-quality feedback to the model without burdening the user.

The evaluation loop also evolves alongside feedback. Evals can now run continuously, blending human and automated judgment. Benchmarks provide the standard of “what does good look like” and a regression baseline. Live telemetry and LLM-based scoring can measure the intelligence and performance.

Bottom line?

#### **When the model IS the product, all UX is RLHF.**

Every click, tab, press, accept shapes not only the user experience but improves the model intelligence.

### **Design for Learning**

Across the eras, software products have always had learning loops. In the PC era, it was manual and slow through people. In the web era, the learning was programmatic through user clicks and data aggregation. In the AI era, the opportunity is to design products to enable self-learning within the model.

Designing for learning means shaping both loops with intention i.e. UX primitives that teach the model, and evaluation that keeps learning grounded in human judgment.

Designing for learning also means not just focusing on usability on day one but learnability to day 100 and beyond.

[![](images/design-for-learning/9ab0e1477756.jpeg)](https://substackcdn.com/image/fetch/$s_!vXw4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3322ae6f-410a-4757-a497-035868892877_3725x1770.jpeg)

*Next up: Designing for Impact.*

*In the next essay in this series, we will shift the focus from product design to strategy and business I.e. what AI products are worth building in the first place.*