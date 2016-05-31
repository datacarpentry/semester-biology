---
layout: exercise
topic: Database Control
title: Importing Data
language: SQL
---

Hand entering data is great if you're collecting your own data and need
to enter it yourself, but it's a pretty terrible way to use already
available data, especially if it's more than a few dozen lines long.
This example will walk you through how to get data that already exists
into SQLite.

1. Download the main table for the [Portal LTREB mammal survey
database](https://ndownloader.figshare.com/files/2292172). *It's kind of large so it might take a few seconds*. This database is published as a Data Paper on 
[Ecological Archives](http://esapubs.org/archive/default.htm), which is generally a great place to look for ecology data.
2. Create a new database by clicking on `New Database` in the `Database` drop down menu. Select a file name, like `portal_mammals.sqlite`, and location.
​
3. Click on the `Import` icon.
​
4. Click on `Select File` and navigate to where you saved the data file
and select it.
​
5. Select `CSV`. *You'll notice that you can also import from other SQL or
modify the `Fields separated` or `enclosed by`*. You'll want to make sure to
select `First row contains column names`.
​
6. Click `OK` when it asks if you want to modify the data.
7. Name the table that you are importing into `Surveys`.
8. Identify the type for each field, using the `Data Type` drop-down menus. If
it is not obvious if the data type is an `INTEGER` or `VARCHAR` for each
variable, check the [metadata](http://esapubs.org/archive/ecol/E090/118/metadata.htm). **Important: if you specify the wrong data type it
can cause some data to not be imported and/or prevent you from doing some kinds
of data manipulations.** ​
9. Select `recordID` as the `Primary Key` and click `OK`.
10. Click `OK` when it asks if you are sure you want to import the data.
11. Now import the [plots](https://ndownloader.figshare.com/files/3299474), and
    [species](https://ndownloader.figshare.com/files/3299483) tables.
