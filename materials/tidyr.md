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

### Pivot data from wide to long

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

* To get the data in this form we can use `pivot_longer`
    * Removes redundant columns
    * Arguments:
        * `data.frame`
        * Columns to include (or not include)
        * `names_to`: the name of the new column to put the column names in
        * `values_to`: the name of the new column to put the column values in

```r
clean_data <- raw_data %>%
  pivot_longer(TreeGirth1:TreeGirth5, names_to = "stem", values_to = "girth")
```

* The colon specifies all columns staring at `TreeGirth1` and ending at `TreeGirth2`
* Could also specify the columns to *not* pivot

```r
clean_data <- raw_data %>%
  pivot_longer(c(-PlotID, -SpCode), names_to = "stem", values_to = "girth")
```

> View data

* Still has zeros for where there were no stems, so filter these out

```r
clean_data <- raw_data %>%
  pivot_longer(c(-PlotID, -SpCode), names_to = "stem", values_to = "girth") %>%
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

```r
clean_data <- raw_data %>%
  pivot_longer(c(-PlotID, -SpCode), names_to = "stem", values_to = "girth") %>%
  filter(girth != 0) %>%
  extract(stem, 'stem', 'TreeGirth(.)')
```

* `TreeGirth.` means the word "TreeGirth" followed by a single value
* The `()` indicate what part of this to extract, so just the number at the end

### Separate

* Genus and species information are combined in a single column
* `separate()`
    * Separates multiple values in single column
    * Arguments:
        * `data.frame`
        * Column name
        * New column names
        * Separator value, character, or position

```r
clean_data <- raw_data %>%
  pivot_longer(c(-PlotID, -SpCode), names_to = "stem", values_to = "girth") %>%
  filter(girth != 0) %>%
  extract(stem, 'stem', 'TreeGirth(.)') %>%
  separate(SpCode, c('genus', 'species'), 4)
```

### Unite and Pivot Wider

* Sometimes we need to go in the other direction
* Count the number of stems of each species on each plot

```r
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

```r
stem_counts_wide <- stem_counts %>% 
  unite(species_id, genus, species)
```

* Then make the data wide
* `pivot_wider`
    * Spread values across multiple columns
    * Arguments:
        * `data.frame`
        * Name of column to use for wide columns
        * Name of column containing the values for the cells
        * Optional `fill` argument for what to put in empty cells

```r
stem_counts_wide <- stem_counts %>% 
  unite(species_id, genus, species) %>%
  pivot_wider(names_from = species_id, values_from = count)
```

* This leaves null values when there is no value in the starting table
* But we can replace this with something else using `values_fill`

```r
stem_counts_wide <- stem_counts %>% 
  unite(species_id, genus, species) %>%
  pivot_wider(names_from = species_id,
              values_from = count,
              values_fill = list(count = 0))
```

### Completing data with gaps

* Some write out a value once and then leave the following rows blank

```r
gappy_data <- read.csv("http://www.datacarpentry.org/semester-biology/data/gappy-data.csv")
gappy_data
```

* This works well for humans, but not for computers
* Can fill in these gaps using `fill`

```r
clean_data <- gappy_data %>%
  fill(Species)
```

* Fills down by default, but other directions are possible

* Often data only includes observed values, but we need to list other values
* Missing zeros or `NA`'s
  
```r
clean_data <- gappy_data %>%
  fill(Species) %>%
  complete(Species, Individual)
```

* Could also use this to add zeros to our long `stem_counts` data frame

```r
stem_counts <- clean_data %>% 
  group_by(PlotID, genus, species) %>% 
  summarize(count = n()) %>%
  complete(PlotID, nesting(genus, species), fill = list(count = 0))
```