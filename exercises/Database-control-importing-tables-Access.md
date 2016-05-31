---
layout: exercise
topic: Database Control
title: Importing Tables
language: Access
---

#### Import Data in MS Access

Hand entering data is great if you're collecting your own data and need
to enter it yourself, but it's a pretty terrible way to use already
available data, especially if it's more than a few dozen lines long.
This example will walk you through how to get data that already exists
into Access.

​a. Download the main table for the full Portal LTREB mammal survey
database from [Ecological
Archives](http://esapubs.org/archive/ecol/E090/118/Portal_rodents_19772002.csv)
(it's kind of large so it might take a few seconds). This database is
published as a Data Paper on Ecological Archives
([http://esapubs.org/archive/default.htm](http://esapubs.org/archive/default.htm)),
which is generally a great place to look for ecology data.

b.Create a new database by selecting a file name and location and
clicking `Create`

​c. Click on the `External Data` tab in Access

​d. Select `Text File` since this is a text file, you'll notice that
you can also import from Excel and from other Access databases

​e. Click on `Browse` and navigate to where you saved the data file
and select it

​f. Make sure that `Import the source data into a new table in the
current database` is selected and click `OK`

​g. Since the data are comma delimited, click `Next`

​h. Make sure the `Comma` is selected as the delimiter, check the
`First Row Contains Field Names` option, and click `Next`

​i. Check to make sure that the types for each field are reasonable.
Access only checks this first few rows of data to determine these types,
so if type of data in a column changes further down this can can cause
import errors. If it was me I'd take are careful look `hft` and
`wgt` (which are weights and hindfoot lenths and should therefore be
numbers) and at `tag`, either by opening the file in Excel or by
checking the portion of the table from the [Creating Tables
problem]({{ site.baseurl }}/exercises/Database-control-creating-tables-Access) to see what might be an issue. When you're
finished click `Next`

​j. Select `Choose my own primary key`, choose `recordID`, and click
`Next`

​k. Name the table that you are importing into `Surveys` and
click `Finish`
