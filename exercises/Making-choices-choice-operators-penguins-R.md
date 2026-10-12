---
layout: exercise
topic: Making Choices
title: Choice Operators with Penguins
language: R
---

If the file [`penguins.csv`]({{ site.baseurl }}/data/penguins.csv) is not in your working directory then download it.

Load `penguins.csv` using `read_csv()`.
Extract the `species`, `island`, and `body_mass_g` columns into vectors named `species`, `island`, and `body_mass`.

Use these vectors to print whether or not the following statements are `TRUE` or `FALSE`.

1. The body mass of the first penguin is greater than 3500 g.
2. `"Emperor"` is in `species`.
3. The species of the first penguin is `"Adelie"` or its body mass is greater than 4000 g.
4. The body mass of the second penguin is between 3700 and 3900 g.
5. Each body mass is `NA`.
6. For each observation either the `island` is `"Torgersen"` or the `species` is `"Gentoo"`.
