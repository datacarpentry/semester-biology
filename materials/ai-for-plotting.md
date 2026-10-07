---
layout: page
element: notes
title: AI - AI for Improving Plots
language: R
time: 1
---

## Should I use AI for this?

- Ask the meta question - given my goals how useful is using AI for this task?
  - Do I want to learn this or not?
  - Is the process of implementing part of my thinking (e.g. writing)?
  - Is it critical that I understand the details or not?
  - Would I enjoy doing this more myself?
  - Does my brain need a break from executive function?
  - Is it quicker, easier, cheaper to do it directly?

## AI for plotting details

- One place where folks spend a lot of time is fine-tuning plots
- We often don't really want to learn the details or enjoy it
- While it's critical to understand the plot
- Not critical to understand the formatting details

- *Paste the code in R and run it*

```r
library(ggplot2)

size_mr_data <- data.frame(
  body_mass = c(32000, 37800, 347000, 4200, 196500, 100000,
    4290, 32000, 65000, 69125, 9600, 133300, 150000, 407000,
    115000, 67000,325000, 21500, 58588, 65320, 85000, 135000,
    20500, 1613, 1618),
  metabolic_rate = c(49.984, 51.981, 306.770, 10.075, 230.073,
    148.949, 11.966, 46.414, 123.287, 106.663, 20.619, 180.150,
    200.830, 224.779, 148.940, 112.430, 286.847, 46.347,
    142.863, 106.670, 119.660, 104.150, 33.165, 4.900, 4.865),
  family = c("Antilocapridae", "Antilocapridae", "Bovidae",
    "Bovidae", "Bovidae", "Bovidae", "Bovidae", "Bovidae",
    "Bovidae", "Bovidae", "Bovidae", "Bovidae", "Bovidae",
    "Camelidae", "Camelidae", "Canidae", "Cervidae",
    "Cervidae", "Cervidae", "Cervidae", "Cervidae", "Suidae",
    "Tayassuidae", "Tragulidae", "Tragulidae"))
ggplot(size_mr_data, aes(x = body_mass, y = metabolic_rate)) +
  geom_point(size = 3) +
  facet_wrap(~family) +
  labs(x = "Body Mass", y = "Metabolic Rate")
```

- *Open a chatbot*

> I’m making a graph using ggplot2 in R.
>
> Here is the code that generates the graph:
>  
> ggplot(size_mr_data, aes(x = body_mass, y = metabolic_rate)) +
>   geom_point(size = 3) +
>   facet_wrap(~family) +
>   labs(x = "Body Mass", y = "Metabolic Rate")
>
> I’d like to modify the graph so that it doesn’t have the gray background

- *Ask students to specify things they want to change about the graph*
- *Improv*
- *Make the x-axis labels non-scientific and bigger so that they overlap and ask for rotation*

## Show AI what you want

- Can give models access to files or websites
- Lots of good resources for cool graphs
- <https://r-charts.com/>
- *Show GGPLOT2*
- Navigate to <https://r-charts.com/ggplot2/facets/>
- *Scroll to "Highlight each group showing all the data behind"*
- Can learn how to do this or how to describe it
- *Or you can upload an image to show the model*
- *Copy-paste image into chatbot*

> I’d like to add the effect shown in the attached graph
