---
title: "Designing Intelligent Products: Design for Trust"
date: 2025-10-05
slug: designing-intelligent-products-design
url: https://aparnacd.substack.com/p/designing-intelligent-products-design
audience: everyone
---

# Designing Intelligent Products: Design for Trust

### Principle: Make the UI Proportional to the AI

In the previous essay in the Designing Intelligent Products series, I talked about how showing your work, i.e. visible reasoning, can build trust.

Another key element of trustworthiness, in products as in people, is the ability to say “I don’t know” when unsure. Trust grows with proportional UX, when ***confidence*** ***feels*** ***proportional*** ***to*** ***correctness***.

### Proportional UX in prior eras

Each era of computing had its own small ways to make this proportional UX legible.

In the desktop era, the red squiggly underline in word processors signaled that a word or a phrase might be wrong, while leaving the final decision with the user.

[![](images/designing-intelligent-products-design/295c2ab64c3f.jpeg)](https://substackcdn.com/image/fetch/$s_!1ZTL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27f64ae9-5545-4430-b828-d52cde60443f_3943x2006.jpeg)

The red squiggly line

On the web, search engines incorporated the ability to spell correct queries users typed. When a query was ambiguous, they asked “Did you mean …?” and when the error was obvious, they corrected it automatically.

[![](images/designing-intelligent-products-design/052e383607e0.jpeg)](https://substackcdn.com/image/fetch/$s_!9JA7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77a795aa-a393-4bf8-ae1f-62f568759dea_3375x2172.jpeg)

Low confidence spell correct UX

[![](images/designing-intelligent-products-design/522f18e2eac0.jpeg)](https://substackcdn.com/image/fetch/$s_!EDKo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81b4d65e-0c3a-4f91-8d2f-a76ba7c98258_3348x2292.jpeg)

High confidence spell correct UX

In mobile, a good example of proportional UX is the blue dot in Maps, drawn with a shaded radius, that showed not just the location but also the precision of the location estimation.

[![](images/designing-intelligent-products-design/f3e37567847c.jpeg)](https://substackcdn.com/image/fetch/$s_!BylQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7660120-9221-4f17-ac89-bdf1dc152862_1850x2769.jpeg)

Blue dot in maps, radius indicating precision

### The AI era primitives — Nerd mode vs. Tech Bro mode

Today’s AI systems oscillate between two extremes. Search engines stay in what I call the “Nerd mode”: generally right but hedged and cautious, while Chatbots slip into “Tech Bro” mode: fluent, confident, persuasive even when wrong.

[![](images/designing-intelligent-products-design/33900dfceb98.jpeg)](https://substackcdn.com/image/fetch/$s_!U_Ye!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcfdd5ceb-9bd1-4933-820c-ae6aee6b33a6_1685x1418.jpeg)

Nerd mode

[![](images/designing-intelligent-products-design/1169aeecfe08.jpeg)](https://substackcdn.com/image/fetch/$s_!0_Wp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9244b142-5490-463a-8120-76f94b1f2821_1522x1683.jpeg)

Tech Bro mode

Overconfidence is particularly problematic because of *Gell-Mann* *amnesia* -- When we read something in our own area of expertise, we spot the errors instantly e.g. the numbers that don’t add up, the shaky logic, the oversimplifications that miss the point. Then we move on to a topic we know less about and accept it completely, forgetting how unreliable the previous page was. It’s a cognitive reset that erases skepticism the moment the subject changes. AI chatbots play out this dynamic. We could spot the hallucinations in an area we know very well and discount the answer, but a few prompts later, on a subject we can’t easily verify, we trust them again.

Recent papers show that hallucination isn’t some glitch in the model, it is structural in that the loss functions and benchmarks that train the models reward producing some output over none. This means we have to explicitly design for this in the product.

[![](images/designing-intelligent-products-design/6bd752712c05.jpeg)](https://substackcdn.com/image/fetch/$s_!tanX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71f9dddc-6571-42f4-84d3-014180c55e19_4080x1750.jpeg)

### Toward new primitives

So what is the squiggly line for the AI era? It is yet to be built IMO but here a few directional ideas that might work.

Example 1: confidence meter, a consistent signal that surfaces how sure the model is about its output, using the uncertainty it already tracks internally (flatter probability distributions, narrower logit margins, diverging reasoning paths etc).

[![](images/designing-intelligent-products-design/9f207f642e80.jpeg)](https://substackcdn.com/image/fetch/$s_!-mxW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d80dde6-38cc-4baf-8d18-3ce89c6d88bb_2529x3417.jpeg)

Another idea is using different tone or specific catch phrases, depending on how confident the product is in underlying responses.

[![](images/designing-intelligent-products-design/d75d9bb9efd0.jpeg)](https://substackcdn.com/image/fetch/$s_!q6hJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d3988ce-ae8c-4861-acf5-10dd46bde704_3128x1937.jpeg)

Designing for trust means designing for proportion: confidence that reflects correctness, interfaces that reveal uncertainty, and systems that know when to say “I don’t know.”

*Next up: Designing for Trust (Part 2c): The WOW/WTH Ratio*