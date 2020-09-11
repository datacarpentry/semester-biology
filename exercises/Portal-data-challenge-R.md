---
layout: exercise
topic: dplyr
title: Portal Data Challenge
language: R
---

Develop a data manipulation pipeline for the Portal `surveys` table that produces a table of data for only the three Dipodomys species (`DM`, `DO`, `DS`).
The species IDs should be presented as lower case, not upper case.
The table should contain information on the date, the species ID, the weight and hindfoot length.
The data should not include null values for either weight or hindfoot length.
The table should be sorted first by the species (so that each species is grouped together) and then by weight, with the largest weights at the top.