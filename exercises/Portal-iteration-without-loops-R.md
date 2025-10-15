---
layout: exercise
topic: Loops
title: Portal Data Iteration Without Loops
language: R
---

This exercise covers iteration without loops in R using Portal data. You'll practice vectorization, apply functions, and integration with dplyr using real ecological data from the Portal Project.

If [surveys.csv](https://ndownloader.figshare.com/files/2292172), [species.csv](https://ndownloader.figshare.com/files/3299483), and [plots.csv](https://ndownloader.figshare.com/files/3299474) are not in your working directory then download them.

Load the three data files using `read_csv`.

1\. Create a vectorized function called `estimate_metabolic_rate` that takes `weight` as input and returns metabolic rate using the equation: `metabolic_rate = 0.073 * weight ^ 0.75`.
Run it on the following vector:

`weights <- c(15, 25, 35, 45, 20, 70, 72)`.

2\. Use `mutate()` and `estimate_metabolic_rate` to create a version of the data in `surveys` with a column called `metabolic_rate` for all animals that have weight measurements. Remove the rows without metabolic rates. Select the `year`, `species_id`, and `metabolic_rate` columns.

3\. Create a function called `classify_by_weight` that takes a single weight value and returns:
   - "small" if weight < 20g
   - "medium" if weight is 20-50g
   - "large" if weight > 50g
   - "unknown" if weight is missing (`NA`)

Use `sapply` to apply `classify_by_weight` to the `weights` vector from (1).

4\. Use `mutate`, `classify_by_weight`, and the `surveys` table to produce a data frame that has data on the `year`, `plot_id`, `species_id`, and `weight_class` (where `weight_class` is the output of `classify_by_weight`). Join this data with the `plots` table to add information on `plot_type`. Filter the data to only include data where `plot_type` is "Control".

5\. Group the results of (4) based on `plot_id` and `weight_class` (using `group_by`) and count the number of individuals in each group (using `summarize`).

6\. Create a function called `energy_budget()` that takes `genus`, `species`, and `weight` as inputs (you'll need to join the `surveys` and `species` tables to get this data together). It should return daily energy needs for each individual in surveys based on the values of `genus` and `species` using the following equations:
   - If `genus` is "Dipodomys" : `energy = 0.065 * avg_weight ^ 0.75 * 24`
   - If `genus` is "Chaetodipus" and `species` is "penicillatus": `energy = 0.080 * avg_weight ^ 0.75 * 24`
   - If `genus` is "Chaetodipus" and `species` is "baileyi": `energy = 0.26 * avg_weight ^ 0.75 * 24`
   - All other species: `energy = 0.073 * avg_weight ^ 0.75 * 24`

Run the function with `mapply()` and the following inputs:
   - `genus`: `c("Dipodomys", "Chaetodipus", "Neotoma")`
   - `species`: `c("merriami", "penicillatus", "albigula")`
   - `weight`: `c(45, 22, 156)`

7\. Use `mutate` and `rowwise` to calculate energy budget for each individual in `surveys`. Drop rows with `NA` for the new `energy_budget` column. Group and summarize the data to get an total energy budget for each combination of `year`, `month`, and `day` by summing all of the values of `energy_budget` in each group.
