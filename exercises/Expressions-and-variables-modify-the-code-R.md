---
layout: exercise
topic: Expressions and Variables
title: Modify the Code
language: R
---

The following code estimates the total net primary productivity (NPP) per day
for two sites. It does this by multiplying the grams of carbon produced in a
single square meter per day by the total area of the site. It then prints the
daily NPP for each site.

```
site1_g_carbon_m2_day <- 5
site2_g_carbon_m2_day <- 2.3
site1_area_m2 <- 200
site2_area_m2 <- 450
site1_npp_day <- site1_g_carbon_m2_day * site1_area_m2
site2_npp_day <- site2_g_carbon_m2_day * site2_area_m2
site1_npp_day
site2_npp_day
```

Modify the code to produce the following items and print them out after the
daily NPP values (the ones currently printed by the code):

1.  The sum of the total daily NPP for the two sites combined.
2.  The difference between the daily NPP for the two sites. We only want
    an absolute difference, so use abs() function to make sure the
    number is positive.
3.  The total NPP over a year for the two sites combined (the sum of the total
    daily NPP values multiplied by 365).
