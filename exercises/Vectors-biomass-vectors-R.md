---
layout: exercise
topic: Vectors
title: Biomass vectors
language: R
---

You have data on the diameter of all of the trees in three sites and each site includes a mix of managmeent stratagies.
Tree masses can be estimated using diameter based on the equation `mass = 0.124 * diameter ^ 2.53`.
The biomass is the sum of the masses of all the trees at a site.
Copy the vectors below into your R script.


```r
site <- c(1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3)
diameter <- c(10.5, 14.2, 13.7, 15.3, 12.8, 9.8, 11.4, 10.9,
               12.1, 13.5, 14.7, 8.5, 9.2, 10.1, 11.3, 12.4,
               13.6, 14.8)
management <- c("active", "active", "passive", "passive",
                "active", "passive", "active", "active",
                "passive", "passive", "active", "active",
                "passive", "active", "passive", "active",
                "passive", "active")
```

*Using only the tools we covered in class* and the information above, answer the following questions:

1. What is the mass of the largest tree, which site is it in, and what is its management status?
2. Which site has the greatest total biomass and what is that biomass?
3. What is the average mass of a tree in each site?
4. What is the difference in total biomass for each site between the "active" management and "passive" management strategies?
