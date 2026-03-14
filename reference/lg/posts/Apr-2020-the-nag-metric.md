---
title: "The Nag Metric"
subtitle: "So your key metric went up... but at what cost?"
date: 2020-04-30
slug: the-nag-metric
url: https://lg.substack.com/p/the-nag-metric
audience: everyone
---

# The Nag Metric

*So your key metric went up... but at what cost?*

[![](images/the-nag-metric/cd1487dcfcdd.jpeg)](https://substackcdn.com/image/fetch/$s_!rIMi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F992bfce7-373a-41b1-b0f3-790b7990dc82_3872x2592.jpeg)

One of the most repeated conversations I hear in my product-building history sounds something like this:

> A: We need more people to sign up/try this feature/engage with this content/convert to payer.
>
> B: Okay. Let's add more call-to-actions and make them more prominent.

Conversely, it can also manifest like this:

> A: I've hidden this action behind a secondary menu.
>
> B: Hmm, that's going to affect our metrics negatively. Are you sure you want to do that?

This type of conversation always left me wanting. It felt like we were doing the intellectual equivalent of recommending that one gets good grades in school in order to have a good life. It's not *bad* advice, per se. Just incomplete.

Look, it's not rocket science: if you crow loudly about a thing you want people to do, they're going to do it more than if you didn't make a fuss about it. This is true for product call-to-actions, and it's true if you want your significant other to pick up their dirty socks from the floor.

At the same time, few of us want to be labeled nags. Fewer of us like to feel that we're being nagged. And I can't think of anyone who would rather do something because they felt pestered to do it, versus feeling free to make that choice.

Certainly, pointing something out to someone can be helpful, especially if they weren't aware of it. Reminders are useful too when that person *wanted* to do that thing but some barrier got in the way.

But nagging? Constantly popping up to tell someone your agenda over and over again when they already got your message and didn't prioritize it? That's annoying. That decreases people's trust with you over the long run and tarnishes your brand. That makes your significant other feel a flicker of irritation instead of the loving fuzzies whenever they see you.

Okay, so maybe you intuitively agree with this. The question is, how can we quantify *nagginess* to make the appropriate tradeoffs against some metric that is sure to go up when we nag more?

### Step 1: Look at the **conversion rate** on the call-to-action (CTA)

***Conversion Rate** = how many times users take a particular action / how many times users see the CTA*

Very low conversion signals that you're putting something that's not very useful or relevant in front of people. Of course, what's considered "good" varies with what the action is and what the market comparables are. If a salesperson sells a Ferrari for every 100 customers she talks to, I'd be impressed. This same conversion rate would be terrible if, say, she were selling lemonade.

In order to have a productive conversation about conversion rate, it’s worth digging into what’s considered “healthy” or “standard” for that type of action.

### Step 2: Look at the **number of people** who get little or no benefit from the CTA

Pure conversion rate doesn't give you a sense of how many people are impacted. If an action's conversion rate is 1/100, that could mean:

* 100 people saw it and one person took the action
* 1,000,000 people saw it and 10,000 took the action
* 1000 people saw it 100 times, and everybody took the action 1 out of those 100 times

Each of the above gives us a different story. In the first case, 99 people were presented with something irrelevant or maybe even annoying. In the second, 990,000 were. In the third, we don't know enough but it's possible that if that one action were really high-value, maybe nobody felt the CTA was irrelevant.

The same conversion rate, and possibly 0, 99, or 990,000 having no (or negative) benefit... Yikes, the difference is huge!

Explicitly enumerating how many people have little or no (or negative) benefit with the CTA makes tangible what the human impact is in a way that a fractional conversion rate doesn’t.

### Step 2: Calculate the Nag Score

The last thing that conversion rate doesn't account for is the actual annoyingness of the CTA.

Allow me to introduce the concept of the *Nag Score*, which is an attempt to quantify this.

*Nag Score* = % of screen real estate dedicated to the CTA \* Attention Multiplier

The lower the Nag Score, the better.

Attention Multiplier is a rating between 0 and 5, where 0 is “This CTA is invisible”, 1 is “This CTA is of average prominence compared to what users see and expect” and 5 is “This CTA is an obnoxious, noisy, and seizure-inducing experience that you can't get out of.”

Let's look at a few examples.

Instagram has a "like" call-to-action—a heart—on every post, though no more than one like button ever shows up at a time on the screen.

The heart is about 7400 pixels.

The screen of my phone has about 2.75 million pixels.

[![](images/the-nag-metric/2e626e917601.png)](https://substackcdn.com/image/fetch/$s_!g4RI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F338bd7d0-5d18-4c8c-98ec-907c3af9283a_1125x2436.png)

7.4K / 2.75M is 0.0027, or 0.27% of the screen.

How about the Attention Multiplier? The design of the button itself is minimal—it's a thin, simple outline stroke in black. Your eye is not drawn to it because there's a much bigger full-color image right about it. As buttons go, this feels less noticeable than the average “like” button that you see across social media apps.

I'm going to go with an Attention Multiplier of 0.5.

So overall, the Nag Score of Instagram's like button = 0.27 \* 0.5 = 0.136

This is extremely low. Nice work Instagram!

Let's take another example that's more egregious. I'm not going to call out any specific companies, but imagine there's a site that you browse to once a day. Every time you go, the site pops up a full-screen interstitial asking you to take some action with a tiny dismissal button in the top right.

Okay, so what's the Nag Score here?

The % of screen real estate dedicated to the pop-up is 100, since you can't browse or see anything else when a full-screen interstitial is up.

In terms of Attention Multiplier, I'm going to go with 4, since a full-screen interstitial blocks you from doing anything else until you've managed to precisely hit that tiny dismiss button, which is pretty damn annoying. (It'd be a 5 if it also played sound!)

This gives us a Nag Score of 400. That's almost 3000 times higher than the IG like button!

Similar to conversion rate, the specific number doesn’t automatically tell us whether it’s “good” or “bad” (unless it’s incredibly high) without more context like the perceived value of the action, how often it’s seen, etc. But the *comparison* is useful*.* Are you increasing or decreasing the Nag Score with any given change? Is your overall Nag Score higher than your competitors’?

---

### So what can we take away here?

With **conversion rate**, **number of people who don’t benefit from the CTA**, and **Nag Score** in our toolbox, we can engage in much more robust tradeoff conversations.

Observe some examples in action:

> A: We need more people to sign up/try this feature/engage with this content/convert to payer.
>
> B: Our conversion rate is already lower than what's standard. Instead of experimenting with more CTAs, we should probably take a closer look at our value prop.

> A: I've hidden this action behind a secondary menu. I expect the number of actions taken to go down, but 100,000 fewer people per month will see something they never interact with, and the conversion rate should increase.
>
> B: Sounds like a reasonable thing to do.

> A: Using this new button style on every post lifted metric X by 15%!
>
> B: Yes, but it also had a 500% lift on our Nag Score. This doesn't seem like a good tradeoff.

In addition to products, this also works in real life\*:

> A: You left your socks on the floor again.
>
> B: Your conversion rate is decreasing and your Nag Score is on the rise.

---

\* not sure it does, actually. But tell me if it works for you, especially during this lockdown period.

*Photo by [terremonto](https://flickr.com/photos/terremonto/)*

---