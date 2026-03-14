# Unit of Work

*Source: https://boz.com/articles/unit-of-work*

# Unit of Work

The environment you are working in has some rate of change. That entropy could
be because of competitors, regulators, consumer behaviors, or a half dozen
other things external to you. But there is always some rate at which the
fundamentals governing the space shift even if you do nothing.

Your team also has some fundamental unit of work at different timescales. There
are strategies that play out over years, roadmaps that play out over months,
features built over weeks, and so on.

At each timescale, the relationship between the rate of entropy and the unit of
work is important to understand. If the unit of work is bigger than the rate of
change then you are in a divergent state and will fall hopelessly behind. On
the other hand if your unit of work is smaller than the rate of change that
suggests that you are likely driving the entropy for others in the space. In
the steady state this is related to a concept I have [written about
before](https://boz.com/articles/ops) called the [OODA
loop](https://en.wikipedia.org/wiki/OODA_loop), which is worth reading up on.

But there is also an acute form of this problem. Sometimes in the course of
building you realize you have an irreducibly large bit of work to do that
doesn’t fit inside the entropy window. In software these often take the form of
rearchitectures or system
[rewrites](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/).
The likely outcome of one of these is that midway through the very expensive
program you find yourself having to start it over because the environment you
are building for continues to evolve.

The surprising takeaway is that it is really only worth embarking on a major
rewrite or similar scale initiative if you think failing to do so will
certainly make your product uncompetitive in the long term.

PublishedJan 18, 2024