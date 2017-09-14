---
layout: page
element: notes
title: Introduction to Databases
language: SQL
---

> Remember to 
>
> * Remind students to install Firefox.

> Walk students through installing SQLite Manager Add-on.

### Why use a database management system

* Simple and effective software for storing, managing and retrieving information
* Widely used to store and maintain lots of existing data
* Fast processing across large amounts of data
    * Out-of-memory and remote processing for really large data
    * Can handle spatially explicit queries (GIS)
* Improve quality control of data entry
    * Set valid data type and value constraints.
    * Use data entry forms in  Excel, Access, Filemaker, etc.
    * Use quality control scripts to test entered data.
* Concepts are core to understanding data manipulation in other languages

### Relational databases

* We will be working with 'Relational Databases'.
    * Data is stored in tables.
        * One table per type of data
            * Tables can be linked together to combine information.
        * Each row contains a single record.
            * A single observation or data point
        * Each column or field contains a single attribute.
            * A single type of information
    * The concepts of relational database management are core to understanding 
      how to do similar things using programming languages such as R or Python.
* We will primarily use SQLite.
    * Simple to use 
    * Almost no work to set up
    * Stored in single file
    * But, there are lots of alternatives
	* Access - commonly used, GUI
	* PostgreSQL - fast/powerful, lots of users

### Importing table into SQLite Manager

1. Download [the Portal Project survey data](https://ndownloader.figshare.com/files/2292172)
2.  Open SQLite Manager
3. `Database` -> `New Database` -> name `portal_mammals` -> `OK` -> `Open` (don’t select any files)
4. `Import` button or `Database` -> `Import`
5. `Select File` -> navigate to just downloaded `surveys.csv` -> `Open`
6. Check `First row contains column names` & select `Comma` option
7. `OK` to modify the data
8. Name table `surveys`
9. Select data types

    * Fields in databases have types that define the kind of data they contain.
    * Each field/column can only have one type.
    * We have to define the types in advance.
    * Types include
        * Integer
        * Text (varchar)
        * Decimal/Double/Real/Float
    * Types are highly configurable for when space is limiting
        * Maximum value of integers
        * Maximum length of text
        * How many values before and after the decimal place

10. Select `record_id` as the `Primary Key` and click `OK`.

    * Every table "needs" a column (or set of columns) that is unique across
      records/row.
    * This is called the `Primary Key`.
    * The easiest way to do this is to use an `INTEGER` that increments every
      time a new record is added.
    * Many databases that you import will already have a field like this.
    * Otherwise autogenerates one. 

> Show students the
>
> * objects panel with `Tables` and `Views`.
> * `Browse & Search` tab.
> * `Structure` tab.

> We've just done most of Exercise 3.
> Do [Exercise 3.11 - Importing Data]({{ site.baseurl }}/exercises/Database-control-importing-data-SQL).
