---
layout: exercise
topic: Database Tools
title: Forms 3
language: Access
---

This is a follow up to the [Forms 2 exercise]({{ site.baseurl }}/exercises/Database-tools-forms-2-Access)

Modify your basic data entry form to prevent bad data values from being entered
into your database. You can do this using the Data tab on the Property Sheet in
the Design View. The following rules should apply:

1.  Months should be numbers from 1-12
2.  Days should be numbers from 1-31
3.  Years should be numbers from 2014-2020 (older data is possible, but
    this form is form entering new data)
4.  Plots should be numbers from 1-24
5.  Stakes should be numbers from 11 to 77
6.  Species should be selected from a drop down list (called a combo box in
    Access) that includes only the species IDs that are present in the
    `new_code` field of the `Species` table. If the `Species` table is updated
    the new values should automatically appear in the combo box.
7.  Sex should be M or F or nothing
8.  Age should be J or nothing
9.  Hind Foot Length should be a number between 1 and 70
10. Weight should be a number between 1 and 350
