---
layout: page
element: notes
title: tidyr
language: SQL
---

### Remember the basic rules of tidy data structure

1. One column per type of information
2. One row per observation
3. One value in each cell

* Unfortunately lots of existing data doesn't follow these rules
* Need to convert them to to this tidy structure for analysis
* Use a package called `tidyr`

```
install.packages("tidyr")
library(tidyr)
library(dplyr)
```

### Gather

* One common issue is data spread over multiple columns that should be in one

> Copy link to Western Ghats tree data from datasets page

```
raw_data = read.csv("http://esapubs.org/archive/ecol/E091/216/Macroplot_data_Rev.txt", sep = "\t")
```

> View data

* Data on tree girth from the Western Ghats
* When a tree had multiple stems the diameter of each stem was entered in a separate column
* What would a better structure be?

> Lead discussion to correct structure

* To get the data in this form we can use `gather`
    * Removes redundant columns
    * Arguments:
        * `data.frame`
        * Column name for grouping of old column headers
        * Column name for grouping of old column values
        * Column range for old columns with values

```
clean_data <- raw_data %>%
  gather(stem, girth, TreeGirth1:TreeGirth5)
```

> View data

* Still has zeros for where there were no stems, so filter these out

```
clean_data <- raw_data %>%
  gather(stem, girth, TreeGirth1:TreeGirth5) %>%
  filter(girth != 0)
```

### Extract

* Want `stem` column to contain numbers 1-5 not `TreeGirth1`
* `extract()`
    * Extracts one or more values from a column
    * Uses regular expressions
    * Arguments:
        * `data.frame`
        * Column name
        * Names of the new columns
        * Regular expression

```
clean_data <- raw_data %>%
  gather(stem, girth, TreeGirth1:TreeGirth5) %>%
  filter(girth != 0) %>%
  extract(stem, 'stem', 'TreeGirth(.)')
```

### Separate

* Genus and species data are combined in a single column
* `separate()`
    * Separates multiple values in single column
    * Arguments:
        * `data.frame`
        * Column name
        * New column names
        * Separator value, character, or position

```
clean_data <- raw_data %>%
  gather(stem, girth, TreeGirth1:TreeGirth5) %>%
  filter(girth != 0) %>%
  extract(stem, 'stem', 'TreeGirth(.)') %>%
  separate(SpCode, c('genus', 'species'), 4)
```

### Unite and Spread

* Sometimes we need to go in the other direction
* Count the number of stems of each species on each plot

```
stem_counts <- clean_data %>% 
  group_by(PlotID, genus, species) %>% 
  summarize(count = n())
```

* Software for running analysis requires cross-tab (or wide) data
* Site in rows, species in columns, counts in cells
* First need a single species ID
* `unite`
    * Combine values from multiple columns into one
    * Arguments:
        * `data.frame`
        * New column name
        * Columns to combine

```
stem_counts_wide <- stem_counts %>% 
  unite(species_id, genus, species)
```

* Then make the data wide
* `spread`
    * Spread values across multiple columns
    * Arguments:
        * `data.frame`
        * Name of column to use for wide columns
        * Name of column containing the values for the cells
        * Optional `fill` argument for what to put in empty cells

```
stem_counts_wide <- stem_counts %>% 
  unite(species_id, genus, species) %>% 
  spread(species_id, count, fill = 0)
```
