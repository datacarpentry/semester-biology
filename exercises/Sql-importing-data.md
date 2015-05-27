---
layout: exercise
title: Importing Data
language: SQL
---

Hand entering data is great if you're collecting your own data and need
to enter it yourself, but it's a pretty terrible way to use already
available data, especially if it's more than a few dozen lines long.
This example will walk you through how to get data that already exists
into SQLite.

​a. Download the main table for the full Portal LTREB mammal survey
database from [Ecological
Archives](http://esapubs.org/archive/ecol/E090/118/Portal_rodents_19772002.csv)
(it's kind of large so it might take a few seconds). This database is
published as a Data Paper on Ecological Archives
([http://esapubs.org/archive/default.htm](http://esapubs.org/archive/default.htm)),
which is generally a great place to look for ecology data.

b. Create a new database by clicking on 'New Database' in the `Database` drop-
down menu. Select a file name, like 'portal_mammals.sqlite', and location.

​c. Click on the `Import` icon.

​d. Click on `Select File` and navigate to where you saved the data file
and select it.

​e. Select `CSV` since this is a .csv file, you'll notice that you can also 
import from other SQL or modify the 'Fields separated' or 'enclosed by'. You'll 
want to make sure to select 'First row contains column names'. 

​f. Click `OK` when it asks if you want to modify the data.

g. Name the table that you are importing into `Surveys`.

​h. Identify the type for each field, using the `Data Type` drop-down menus. If 
it is not obvious if the data type is an `INTEGER` or `VARCHAR` for each 
variable, check the [metadata](http://esapubs.org/archive/ecol/E090/118/
Portal_rodent_metadata.htm).

​i. Select `recordID` as the `Primary Key` and click `OK`.

j. Click `OK` when it asks if you are sure you want to import the data.