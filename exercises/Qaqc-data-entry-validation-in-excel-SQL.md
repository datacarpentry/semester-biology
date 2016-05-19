---
layout: exercise
topic: QAQC
title: Data entry validation in Excel
language: SQL
---

You're starting a new study of small mammals at the [NEON site at Ordway-Swisher](http://ordway-swisher.ufl.edu/NEON.aspx). 
Create a spreadsheet in Excel for data entry. It should have four columns: Year, Site, Species, and Mass.

Set the following data validation criteria to prevent any obviously wrong data
from getting entered:

1. Year must be an integer between 2015 and 2025.
2. Site should be one of the following `A1`, `A2`, `B1`, `B2`.
3. Species should be one of the following `Dipodomys spectabilis`, `Dipodomys
   ordii`, `Dipodomys merriami`.
4. Mass should be a decimal greater than or equal to zero but less than or equal
   to 500 since mass is measured in grams in this study and nothing bigger than
   half a kilogram will possibly fit into your
   [Sherman traps](https://en.wikipedia.org/wiki/Sherman_trap). Change the error
   message on this validation criteria to explain why data is invalid and what
   the valid values are.

Save this file as `yourname_ordway_mammal_data.xlsx`.
