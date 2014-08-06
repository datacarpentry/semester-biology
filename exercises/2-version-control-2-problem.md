--- layout: post title: 2. Version Control 2 [problem] created:
1315797048 categories: - !binary |- Mg== - !binary |- YWR2 - !binary |-
Mg== - !binary |- YWR2 ---

Growth of biological populations are often modeled using logistic
growth, which posits that some limit will eventually stop a population
from increasing in size. The simplest form of this type of growth is
logistic growth and takes the following form:

**N\_tplus1 = N\_t + r\*N\_t\*((K-N\_t)/K)**

where **N\_t** is the abundance at time **t**, **N\_tplus1** is the
abundance at time **t+1**, **r** is the maximum per capita reproductive
rate, and **K** is the carrying capacity. The **(K-N\_t)/K** term
captures the impact of the members of a species on each other - the more
individuals of the species there are, the lower each individuals net
reproductive rate.

Working late into the evening your professor has thrown together a small
example program that determines the equilibrium population sizes from
logistic growth and the time it takes to reach those equilibria. The
file is in your repository and is named logistic\_growth.py.
Unfortunately he's gotten sloppy because of the late hour and he's made
a few mistakes. Fix the errors on lines 3 and 13, save the file, and
then commit it back to your repository with an appropriate commit
message.
