---
layout: page
element: notes
title: Advanced Filtering
language: R
time: 0.25
---

### Multiple filter conditions

* We can filter on multiple conditions at once
* In computing we combine conditions in two ways "and" & "or"
* "and" means that all of the conditions must be true
* Do this in `dplyr` using either additional comma separate arguments

```
filter(surveys, species_id == "DS", year > 1995)
```

* Or by using `&`

```
filter(surveys, species_id == "DS" & year > 1995)
```

* "or" means that one or more of the conditions must be true
* Do this using `|`
* Say we wanted data on all of the *Dipodomys* species.

```
filter(surveys, species_id == "DS" | species_id == "DM" | species_id == "DO")
```

### Filtering by aggregated properties

* You can also filter based on aggregated values
* If we wanted to estimate species weights only for species with > 100 individuals

```r
species_weights <- surveys %>%
  group_by(species) %>%
  filter(n() > 100) %>%
  summarize(avg_weight = mean(weight, na.rm = TRUE))
```
