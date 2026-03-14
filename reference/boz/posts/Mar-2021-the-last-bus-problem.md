# The Last Bus Problem

*Source: https://boz.com/articles/bus-problem*

# The Last Bus Problem

I go to Sundance Film Festival every year in the relatively small mountain
town of Park City, Utah. The films are screened in makeshift theaters spread
across the town; a high school, a library, a shopping mall, and so on. The
town was not built for this amount of traffic but they manage it with
surprising efficiency by bringing in busses just for the festival. The busses
come by each location so frequently that you rarely check the schedule; you
just wait. So when a film lets out and there are a ton of people waiting for
busses it is a very polite affair.

Except for the last screening of the day.

The busses stop running not long after the final screenings let out. That
means there is concern that the bus there now may be the last bus. It is often
snowing. Accommodations are generally far from the theaters. Everyone wants to
get on that bus and many would push their fellow moviegoer aside for the
opportunity.

Personally, I rent a car. But whenever I observe this bus phenomenon I think
about the Facebook push process.

When I joined Facebook we pushed code once a week. That was a recent change
that accompanied the adoption of source control software. (Not long before I
joined; they just edited files live and copied them around to all the
servers.) Coming fromMicrosoft I thought the weekly push was a terrible idea.
There wasn’t enough time to test how code would interact. I advocated for
slower release cycles, perhaps monthly. We decided to give it a try.

Mark generally gave us a wide berth on engineering processes but he came down
hard on this. He was unequivocal: not only could we not move the push to
monthly, he wanted us to push code daily. As a consequence we had a daily push
for years accompanied by a larger weekly push for more complicated changes.

Today we’ve gone even further to a continuous release process.

Mark’s justification for increasing the push cadence was a desire to increase
our iteration speed as this gated the speed at which we could learn what
products were working and what to try next.

I observed a second, equally beneficial change in the behavior of developers.
When we had a weekly or (one-time) monthly push for code changes a huge number
of changes would arrive at the very last minute. When the build broke or was
unstable (which was often) it was invariably a consequence of one of these
late arriving changes.

The reason is simple, like moviegoers hustling to get on the last bus, the
developers saw the prospect of being delayed another week and abandoned all
caution to try to get their code a ticket to ride.

When we went to daily pushes, however, this behavior improved dramatically.
When the consequence of missing a release was waiting one day the pressure to
get code in was reduced dramatically. And the code that went in was relatively
more ready for deployment.

Building hardware roadmaps has proven to have a similar quality. When there is
only one product in the roadmap there is pressure from every technology team
to try to fit their feature in somehow. That is hardly the path to a [great
product](https://simpsons.fandom.com/wiki/The_Homer). But when you have
multiple products roadmapped out into the future people can target the
appropriate intercept for their feature based on quality and value.

The fundamental lesson here is that for any repeating process it is important
to consider both planning horizons and cycle time and the impact those have on
the incentives they create for teams. When possible, having transparency about
long term schedules and more continuous evaluation processes will remove
gamesmanship from the equation and allow teams to focus primarily on the
problem they are trying to solve.

PublishedMar 26, 2021