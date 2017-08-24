---
layout: exercise
topic: Basic Queries
title: WHERE
language: SQL
---

A population biologist (Dr. Undomiel) who studies the population dynamics of
*Dipodomys spectabilis* would like to use some data from the Portal Project, but
she doesn't know how to work with large datasets. Being the kind and benevolent
person that you are, write a query to extract the data that she needs. She wants
only the data for her species of interest (`DS` in the `species_id` column),
when each individual was trapped, and what sex it was. She doesn't care about
the plot the individual was trapped on or the size of the individuals. She also
doesn't need the species codes because you're only providing her with the data
for one species, and since she isn't looking at the database itself the two
character abbreviation would probably be confusing. Save this query as a view
with the name `spectabilis_population_data`.

Scrolling through the results of your query you notice that the data on sex is
missing for some species. You send Dr. Undomiel a short e-mail* asking what she
would like you to do regarding this complexity. Dr. Undomiel asks that you
create two additional queries so that she can decided what to do about this
issue later. Add a query that retrieves the same data as above, but only for
cases where the sex is known to be male, and an additional query with the same
data, but only where the sex is known to be female. Save these as views with the
names `spectabilis_population_data_males` and
`spectabilis_population_data_females`.

*Short for elven-mail
