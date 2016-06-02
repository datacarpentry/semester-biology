---
layout: exercise
topic: Expressions and Variables
title: Modify the Code 1
language: Python
---

The following code calculates the total net primary productivity (NPP)
per day for two sites based on the grams of carbon produced per square
meter per day, and the total area of the sites, and prints them out.

```
    site1_g_carbon_m2_day = 5
    site2_g_carbon_m2_day = 2.3
    site1_area_m2 = 200
    site2_area_m2 = 450
    site1_npp_day = site1_g_carbon_m2_day * site1_area_m2 
    site2_npp_day = site2_g_carbon_m2_day * site2_area_m2
    print(site1_npp_day)
    print(site2_npp_day)
```

Modify the code to produce the following items and print them out in
order:

1.  The sum of the total daily NPP for the two sites combined.
2.  The difference between the total daily NPP for the two sites. We only want
    an absolute difference, so use abs() function to make sure the
    number is positive.
3.  The total NPP over a year for the two sites combined.

