Maybe do this material in conditionals?


### Handling nulls (more generally)

* To remove only rows with `NA` in specific columns use `filter`

```
filter(surveys_by_species, weight != NA)
```

* Why didn't that work?
* Null values like `NA` are special
* We don't want to accidentally say that two "missing" things are the same
    * We don't know if they are
* So use special commands
* `is.na()` checks if the value is `NA`
* Combine this with `!` for "not"

```
filter(surveys_by_species, !is.na(weight))
```

* So `!is.na(weight)` is conceptually the same as "weight != NA"

```
surveys_by_species_nonull <- filter(surveys_by_species,
                                    !is.na(weight))
species_weight <- summarize(surveys_by_species_nonull,
                            avg_weight = mean(weight))
```

> Do [Portal Data Manipulation 4-6]({{ site.baseurl }}/exercises/Portal-data-manip-R/).