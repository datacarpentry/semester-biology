---
layout: page
element: notes
title: dplyr Joins
language: R
time: 30
---

### Setup

```r
install.packages(c('dplyr', 'readr', 'tidyr')
download.file("https://ndownloader.figshare.com/files/2292172", "surveys.csv")
download.file("https://ndownloader.figshare.com/files/3299474", "plots.csv")
download.file("https://ndownloader.figshare.com/files/3299483", "species.csv")
download.file("https://www.datacarpentry.org/semester-biology/data/shrub-volume-data.csv", "shrub-volume-data.csv")
```

### Joins

> Remember to:
>
> * display a fully joined version of the Portal data using:
> `portal_bigtable <- inner_join(inner_join(surveys, species), plots)`

#### Why use multiple tables

* When we talked about data structure we discussed splitting data into multiple tables.
* This lets us avoid redundant information, like listing the full taxonomy for every individual of a species, which makes storage more efficient and allows us to make changes in one place, not hundreds of places.
* Each table contains a single kind of information
* Let's look at this in the Portal dataset

```r
library(dplyr)
library(readr)

surveys <- read_csv("surveys.csv")
species <- read_csv("species.csv")
plots <- read_csv("plots.csv")
```

* In the Portal dataset
    * `surveys`: information about individuals
    * `species`: information about species
    * `plots`: information about plots
* If a species name changes we only need to change it in the `species` table

#### Basic join

* Connect tables using joins
* To enable us to make these connections the tables need one or more columns that link them together
* In the case of the Portal data there is one column that links the `surveys` and `species` tables, `species_id`
* There is also one column that links the `surveys` and `plots` tables, `plot_id`

* Let's join the surveys and the species tables together using an "inner join"
* To do this we use the `inner_join` function
* It takes three arguments:
  * The first of the two tables we want to join
  * The second of the two tables we want to join
  * The column(s) that provide the linkage between the two tables wrapped in the `join_by` function

```r
combined <- inner_join(surveys, species, join_by(species_id))
```

* Looking at the `combined` table, we can see that on every row with a particular value for `species_id` the join has added the matching values for `genus`, `species`, and `taxa`
* One way to think about this join is that it adds the relevant information in the `species` table to the `surveys` table
* Often for scientific data we can think about there being one main table, the `surveys` table in our case, and multiple supplementary tables that provide additional details

* Inner joins keep information from both tables when both tables have a matching value in the join column
* Here's a visualization of what an inner join looks like:

![Illustration of an inner join showing two tables being joined.
First table has 1, 2, 3 in column 1 and x1, x2, x3 in column 2.
Second table has 1, 2, 4, in column 1 and y1, y2, y4 in column 2.
Combined table has 1 and 2 in column 1, x1 and x2 in column 2, and y1 and y2 in column 3.
]({{ site.baseurl }}/materials/inner-join.gif)

* Any rows in either table that don't have a matching value in the other table are dropped
* So when we did our join all of the rows with missing `species_id` values were dropped
* Scroll to Line 324 in the `surveys` table
* `record_id`'s 324-326 are missing species IDs
* If we look in `combined` we'll see that those rows are not present
* There are other joins that behave differently
* Left joins keep all rows in the first, or left, table
* So if we want to keep rows with missing species IDs we could use `left_join`

```r
combined <- left_join(surveys, species, join_by(species_id))
```

* There are also right joins, which keep all rows in the second, or right, table
* And full joins, which keep all rows from both tables
* For our exercises we'll focus on using inner joins

#### Multi-table join

* But we often need to combine more than two tables
* To join more than two tables we start by joining two tables
* And then join the resulting table to a third table, and so on
* So, for Portal, we could start by joining the `surveys` and the `species` tables and then combine the resulting table with the `plots` table

```r
full_data <- surveys |>
  inner_join(species, join_by(species_id)) |>
  inner_join(plots, join_by(plot_id))
```

> Do [Portal Data Joins]({{ site.baseurl }}/exercises/Portal-data-joins-R/).
