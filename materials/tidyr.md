---
layout: page
element: notes
title: tidyr
language: SQL
---

> Set up R console:

```
library(tidyr)
```

### Remember the five basic rules of database structure

1. Order doesn’t matter 
2. No duplicate rows
3. Every cell contains one value
4. One column per type of information
5. No redundant information

### Restructure tables with messy data 

* Cells with multiple values break rule #3.
* Redundant column information or cross-tabulated data breaks rule #4.

![How to restructure to keep no duplicate rows and one value per cell]({{ site.baseurl }}/materials/database_struct_multiple_habitat_values.png)

* Here is another messy dataset.

```
scary_sightings <- data.frame(
  animals = c("lions", "tigers", "bears"),
  brick_road = c("1-Y", "0-N", "0-N"),
  emerald_city = c("17-N", "8-Y", "64-N")
)
```

```
> scary_sightings
  animals brick_road emerald_city
1   lions        1-Y         17-N
2  tigers        0-N          8-Y
3   bears        0-N         64-N
```

* What do the values in the table represent?
    * `lions` and `tigers` and `bears` are names of `animals`
    * `1-Y`, `17-N`, etc. represent: 
        * Counts of animals sighted on the `brick_road` or in the `emerald_city`
        * And, were the animal sightings scary? `Y` or `N`

> Ask students,
> 
> * "What makes `scary_sightings` messy?"
> * "What are the variables in `scary_sightings`?"

* Tidy variables in `scary_sightings`
    * `animals` 
        * `lions` and `tigers` and `bears`
    * `site` 
        * `brick_road` and `emerald_city`
    * `sightings`
        * count
    * `scared`
        * `Y` or `N`

### `tidyr` helps restructure messy data

* `gather()`
    * Removes redundant columns
    * Arguments:
        * Piped `data.frame`
        * Column name for grouping of old column headers
        * Column name for grouping of old column values
        * Column range for old columns with values

```
less_scary <- scary_sightings %>%
  gather(site, scary_counts, brick_road:emerald_city)
```

```
> less_scary

  animals         site scary_counts
1   lions   brick_road          1-Y
2  tigers   brick_road          0-N
3   bears   brick_road          0-N
4   lions emerald_city         17-N
5  tigers emerald_city          8-Y
6   bears emerald_city         64-N
```

* `separate()`
    * Separates multiple values in single column
    * Arguments:
        * Piped `data.frame`
        * Column name
        * New column names
        * Separator value or character

```
sightings <- less_scary %>%
  separate(scary_counts, c("count", "scary"), sep="-")
```

```
> sightings
  animals         site count scary
1   lions   brick_road     1     Y
2  tigers   brick_road     0     N
3   bears   brick_road     0     N
4   lions emerald_city    17     N
5  tigers emerald_city     8     Y
6   bears emerald_city    64     N
```

> Do [Exercise 5 - Tree Biomass]({{ site.baseurl }}/exercises/Tidyr-tree-biomass-R).