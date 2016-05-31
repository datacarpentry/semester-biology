---
layout: exercise
topic: Database Control
title: Creating Tables
language: Access
---

​a. Create a new MS Access database named `assignment2_yourname`

​b. Create a table named `SurveysByHand` with the following fields:
`SampleID, Plot, Year, Species, Mass, HindFoot, Tag`. Choose the types
appropriately for the following data. Make `ID` the primary key.

`Table 1. Five data points from the Portal LTREB long-term rodent
sampling database`

```
| ID    | plot | year | species | weight | hindfoot |    tag |
| ----- | ---- | ---- | ------- | ------ | -------- | ------ |
| 21012 |    4 | 1993 |      DM |     42 |       36 | 1EA0F9 |
| 22012 |    4 | 1995 |      DM |     31 |       37 | 0D373C |
| 23012 |   17 | 1996 |      DM |     25 |       37 | 64C6CC |
| 24012 |   21 | 1996 |      PP |     26 |       22 | 1F511A |
| 25012 |   22 | 1997 |      DM |     53 |       35 |   2624 |
```
​c. Take a minute and think about why we shouldn't use `tag` as the
primary key. When considering this question you need to know a simple
fact about mammal trapping. Sometimes individuals escape at some point
during processing (they may be small, but boy can they bite!) before all
information can be collected or before the individual can be tagged.

​d. Enter the data above into your table

​e. Save and close the table. Congratulations - you've created your
first relational database!
