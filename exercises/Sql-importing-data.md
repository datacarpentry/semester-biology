---
layout: exercise
title: Importing Data
subtitle: Importing Data
language: SQL
---

Hand entering data is great if you're collecting your own data and need
to enter it yourself, but it's a pretty terrible way to use already
available data, especially if it's more than a few dozen lines long.
This example will walk you through how to get data that already exists
into SQLite.

1. Download the main table for the full [Portal LTREB mammal survey
database](http://esapubs.org/archive/ecol/E090/118/Portal_rodents_19772002.csv) from Ecological Archives. *It's kind of large so it might take a few seconds*. This database is published as a Data Paper on [Ecological Archives](http://esapubs.org/archive/default.htm), which is generally a great place to look for ecology data.
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
variable, check the [metadata](http://esapubs.org/archive/ecol/E090/118/
Portal_rodent_metadata.htm).
​
9. Select `recordID` as the `Primary Key` and click `OK`.
10. Click `OK` when it asks if you are sure you want to import the data.


There are a few alternate methods to the previous step-wise approach.

- You can create the SQLite version of this database using the
[EcoData Retriever](http://ecodataretriever.org/) by first [installing the
software](http://ecodataretriever.org/download.html) and then running:    
```
retriever install sqlite PortalMammals
``` 
from the command line. 
- Or you can download an already assembled [copy of the database]({{ site.baseurl }}/data/portal_mammals.sqlite).

*We encourage you to familiarize yourself with multiple methods to be prepared for the various ways data can be available to you for future projects.*
