# Engineering the next generation of LinkedIn's Feed

**Authored by Hristo Danchev, March 12, 2026**

Source: https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed

---

The LinkedIn Feed serves more than 1.3 billion professionals, each on a unique career journey. Whether members are building their brand, sharing expertise, exploring new ideas, or learning from trusted voices, they come to LinkedIn to connect and grow. We want to connect every member to insights, ideas, and inspiration that move them forward. The most valuable content is timely, relevant to their professional goals, and grounded in trust.

While the Feed has long been AI-powered, recent LLM advances gave us the opportunity to rethink what's possible. That's why we're rolling out a new advanced ranking system, powered by LLMs and GPUs, that better understands what a post is actually about and how it relates to a member's evolving interests and career goals. By learning from past LinkedIn activities, it delivers more accurate and helpful recommendations than ever before.

## Unified retrieval through fine-tuned LLMs

We've moved from keywords to semantic intent. Our LLM-powered retrieval system uses a fine-tuned model to understand the relationship between a member's professional profile and the content on their Feed.

### From structured data to effective prompts

Instead of relying on raw data fields, we construct natural language prompts that represent both the member and the post. For members, this includes their professional summary, recent engagements, and career interests. For posts, we use transcriptions of videos, the text of articles, and even descriptions of images.

**Key engineering insight:** LLMs don't inherently understand magnitude, so raw numerical features tokenize poorly and lose ordinal meaning. Converting continuous values to percentile buckets wrapped in special tokens gives the model a stable, learnable vocabulary for quantity.

### Training dual encoders at scale

We distilled and fine-tuned a LLM using millions of member-to-item pairs from Feed engagement data. The dual encoder architecture uses a LLM to process both the member and item prompts, and in return it generates embeddings that are compared via cosine similarity. We optimized for retrieval using InfoNCE loss with sophisticated negative sampling. Each positive member-item pair is contrasted against two types of negatives: easy and hard.

- **Easy negatives** are randomly sampled posts that weren't shown to this member; these provide weak but stable contrastive signals.
- **Hard negatives** are posts that were actually impressed to the member but received no engagement, which turned out to be challenging cases where the model must learn nuanced distinctions between "relevant but not quite right" and "genuinely valuable." Adding just two hard negatives per member improved recall by +3.6%, which is a significant gain from a simple change.

### Online serving: freshness at scale + Consolidating complexity

While deep retrieval models have significantly improved our system's quality over time, they often introduced operational complexity. Initially, the Feed relied on multiple specialized retrieval models (e.g., one for ads, one for jobs, another for connections). We've now consolidated these into a single unified LLM retriever that understands the interrelationships between these different content types.

To maintain low-latency retrieval while using LLM-derived embeddings, we leverage Approximate Nearest Neighbor (ANN) search on a specialized vector database. Now, every new post is indexed in real-time, ensuring that members see the latest professional news within seconds of it being shared.

## Ranking: understanding your professional journey

Once the retrieval system finds a set of potentially relevant posts, the ranking system determines the optimal order. We've transitioned to a new Generative Recommender (GR) architecture capable of processing sequences of interactions.

### Teaching transformers to recommend

Our new ranking model is based on the Transformer architecture. Instead of looking at each post in isolation, it considers the sequence of your professional interactions over time.

- **Long-term context:** It understands that if you're a software engineer, your interest in "Python performance" might be a multi-month trend.
- **Short-term context:** It also recognizes if you just started looking for a job, immediately shifting the Feed toward career advice and opportunities.

The Generative Recommender (GR) model reimagines ranking by treating your feed interaction history as a sequence—a professional story told through the posts you've engaged with over time. Instead of scoring each post in isolation, GR processes more than a thousand of your historical interactions to understand temporal patterns and long-term interests.

The GR model uses industry-leading transformer architecture with causal attention, processing your posts chronologically alongside your actions on each post. We capture rich features such as viewer information (profile, headline, company, industry), content embeddings, engagement signals, and post metadata, while your actions (long dwells, likes, comments, shares) are embedded and interleaved with post representations, creating a unified sequence that captures both what you saw and how you engaged.

These interleaved post-action pairs flow through multiple transformer layers with causal attention, meaning each position can only attend to previous positions—mimicking the actual temporal flow of how you experienced content. The transformer's self-attention mechanism allows the model to weigh different parts of your history based on relevance.

**Key engineering insight:** Treating interactions as an ordered sequence rather than independent events lets the model capture trajectory, not just preference. This is especially high-leverage for sparse users: a sequential model extracts more signal from fewer interactions than a pointwise model ever can.

## Engineering for production scale

### The GPU economics challenge

Serving LLMs at scale is hard; doing so while satisfying Feed's low-latency requirement is extremely hard. We implemented several critical optimizations:

- **Key-Value (KV) Caching:** Since a member's history doesn't change between each post recommendation in a single Feed session, we cache the KV states of the historical portion of the sequence. This transforms the quadratic attention computation into a linear one for each candidate item, significantly reducing the GPU compute needed per recommendation.
- **FlashAttention-2:** We use memory-efficient attention kernels that reduce high-bandwidth memory (HBM) usage and increase throughput.
- **Quantization:** We use FP8 quantization for both weights and activations during inference, cutting memory usage by half without a measurable loss in model accuracy.
- **Speculative Decoding:** A smaller, faster model generates potential engagement predictions, which then our larger GR model evaluates in parallel.

Training happens 3.5x faster on a cluster of H100s, but that's just the tip of the iceberg. These optimizations allow us to train on larger histories (up to 1,024 items vs the previous 256) and use more complex architectures while keeping the model updated more frequently.

## Conclusion

Engineering the next generation of LinkedIn's Feed meant moving beyond traditional ranking. By leveraging fine-tuned LLMs for unified retrieval and transformer-based sequential models for ranking, we've built a Feed that truly understands the professional journey.

All of these achievements serve a single purpose: delivering a smarter, faster, more responsive Feed without you ever noticing the complexity underneath. The models are more sophisticated than ever, yet your experience remains seamless—content loads instantly, recommendations feel more relevant, and trending conversations reach you while they still matter.

## Acknowledgements

This work was made possible by the collective efforts of the Feed AI, Relevance Platform, GPU Infrastructure, and AI Infrastructure teams at LinkedIn. Special thanks to Hristo Danchev, Souvik Ghosh, Yiwen Zhang, and the entire Feed Engineering organization for their contributions to this groundbreaking system.
