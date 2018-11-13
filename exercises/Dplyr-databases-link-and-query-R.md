---
layout: exercise
topic: dplyr Databases
title: Link and Query
language: R
---

1. Connect to `portal_mammals.sqlite` as object `portaldb` using `dplyr`.
2. Start by reminding yourself about which tables are in the database using
   `src_tbls()`
3. Then remind yourself of the fields in the `surveys` and `plots` tables using
   the list subset operator `$ops$vars`.
4. Select and print out the average hind foot length and average weight of:
    - all *Dipodomys spectabilis* individuals on the *control* plots
    - male *D. spectabilis* on the *control* plots
    - female *D. spectabilis* on the *control* plots
