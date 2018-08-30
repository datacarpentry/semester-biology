---
layout: page
element: notes
title: dplyr Joins
language: R
time: 30
---

### Joins

> Remember to:
>
> * display a fully joined version of the Portal data using:  
> `portal_bigtable <- inner_join(inner_join(surveys, species), plots)`

#### Why use multiple tables

* Not efficient to include all information in a single table.
* Redundant information makes it more difficult to update or revise data.
    * Make changes in one place, not hundreds of places.
* Use multiple tables
* Each table contains a single kind of information
    * `surveys`: information about individuals
    * `species`: information about species
    * `plots`: information about plots
* If a species name changes we only need to change it in the `species` table
* Connect tables using joins to describe relationships between tables

#### Basic join

* Joins combine two tables using one or more columns
* `inner_join` keeps information from both tables that share a join field value

```
species <- read.csv("species.csv")
combined <- inner_join(surveys, species, by = "species_id")
head(combined)
```

* One way to think about this join is that it adds the information in
  `species` to the `surveys` table

> Do [Shrub Volume Join]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-join-R).

#### Multi-table join

* Use multiple joins to link multiple tables

```
portal_full <- inner_join(combined, plots, by = "plot_id")
head(portal_full)
```
