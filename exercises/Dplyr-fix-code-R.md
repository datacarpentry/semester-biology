---
layout: exercise
old_title: Code fix - dplyr
topic: Code fix - dplyr
title: Fix the code
language: R
---

This is a follow-up to
[Scientific 0]({{ site.baseurl }}/exercises/Scientific-0-R).
If you haven't already downloaded the
[shrub volume data]({{ site.baseurl }}/data/shrub_volume_experiment.csv)
do so now and store it in your `data` directory.

The following code is supposed to import the shrub volume data and calculate the
average shrub volume for each experiment and, separately, for each site

```
read.csv("data/shrub_volume_experiment.csv")
shrub_data %>%
  mutate(volume = length * width * height) %>%
  group_by(site) %>%
  summarize(mean_volume = max(volume))
shrub_data %>%
  mutate(volume = length * width * height)
  group_by(experiment) %>%
  summarize(mean_volume = mean(volume))
```

1. Fix the errors in the code so that it does what it's supposed to
2. Add a comment to the top of the code explaining what it does
3. In a text file, discuss how you know that your fixed version of the code is
   right and how you would try to make sure it was right if the data file was
   thousands of lines long
