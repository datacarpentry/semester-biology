---
layout: exercise
topic: Functions
title: Penguin Body Condition
language: R
---

Body condition describes the mass of an animal relative to the mass expected given its size.
Individuals that are heavier than expected are considered to be in better condition.

If the file [`penguins.csv`]({{ site.baseurl }}/data/penguins.csv) is not in your working directory then download it.

1. Write a function called `est_mass_from_flipper` that takes `flipper_length` (in mm), `a`, and `b` as arguments. Set default arguments for `a = 0.018` and `b = 2.33`. The function should estimate the expected body mass using `mass = a * flipper_length ^ b`. Use the function to estimate the expected mass of a penguin with a flipper length of 200 mm.

2. Write a function called `calc_body_condition` that takes `observed_mass` and `expected_mass` as arguments and returns the body condition, where body condition is `observed_mass / expected_mass`. Use the function to calculate the body condition of a penguin that weighs 4200 g but was expected to weigh 4000 g.

3. Load `penguins.csv` using `read_csv()`. Use `mutate()` and the two functions you wrote to add a new column named `body_condition` to the data frame.

4. Calculate the average `body_condition` for each `sex` of each `species`.

5. Make an unstacked histogram of body condition with the bars colored by island with one subplot (facet) 
for each year.
