---
layout: page
element: notes
title: Introduction to Databases
language: R
---

> Remind students to install Firefox.

> Walk through installing SQLite Manager Add-on.

## Why use a database management system

* Simple and effective software for storing, managing and retrieving information
* Widely used to store and maintain lots of existing data
* Fast processing across large amounts of data
    * Out-of-memory and remote processing for really large data
    * Can handle spatially explicit queries (GIS)
* Improve quality control of data entry
    * Set valid data type and value constraints.
    * Use data entry forms in  Excel, Access, Filemaker, etc.
    * Use quality control scripts to test entered data.

## Database management systems

* We will be working with 'Relational Databases'.
    * The concepts of relational database querying are core to understanding 
      how to do similar things using programming languages such as R or Python.
* We will primarily use SQLite.
    * Simple to use 
    * Almost no work to set up
    * Stored in single file
    * But, there are lots of alternatives
	  * Access - commonly used, GUI
	  * PostgreSQL - fast/powerful, lots of users

> Open and preview SQLite with `portal_mammals.sqlite`

### Key features of database management systems

* Data is separate from manipulations of the data
* Tables - store the data
* Queries - store questions about the data
    * If we update the data, the query asks the same question of the new data.

### Relational databases

* Data is stored in tables.
    * One table per type of data
    * Tables can be linked together to combine information.
* Each row contains a single record.
    * A single observation or data point
* Each column or field contains a single attribute.
    * A single type of information

> Show students the
>
> * objects panel with `Tables` and `Views` 
> * `Browse & Search` tab.

### Data Types

* Fields in databases have types that define the kind of data they contain.
* Each field/column can only have one type.
* We have to define the types in advance.
* Types include
    * Integer
    * Text
    * Decimal/Double/Real/Float
* Types are highly configurable for when space is limiting
    * Maximum value of integers
    * Maximum length of text
    * How many values before and after the decimal place

> Show students the `Structure` tab.

### Primary keys

* Every table "needs" a column (or set of columns) that is unique across
  records/row.
* This is called the `Primary Key`.
* The easiest way to do this is to use an `INTEGER` that increments every time a
  new record is added.
* Many databases that you import will already have a field like this.

### Database Control

There are many ways to add and modify data in a database management system.

1\. Enter the data into another program (e.g., a spreadsheet) and import it to SQLite.

> Do [Exercise 1 - Data entry validation in Excel]({{ site.baseurl }}/exercises/Qaqc-data-entry-validation-in-excel-SQL/). 

2\. Get the data from somewhere and import it ( *though, data isn't always ready 
to import into a database* )

> Do [Exercise 2 - Importing Data]({{ site.baseurl }}/exercises/Database-control-importing-data-SQL).

3\. Enter the data directly.

> Demo [Creating Tables]({{ site.baseurl }}/materials/sql-creating-tables).
>
> Do [Exercise 3 - Creating Tables]({{ site.baseurl }}/exercises/Database-control-creating-tables-SQL/).

> Demo [Updating Tables]({{ site.baseurl }}/materials/sql-updating-tables).
>  
> Do [Exercise 4 - Adding Records]({{ site.baseurl }}/exercises/Database-control-adding-records-SQL/) and [Exercise 5 - Updating Records]({{ site.baseurl }}/exercises/Database-control-updating-records-SQL/).

## SQL - structured query language

> Show students the `Execute SQL` tab.

* The language of databases
* Even graphical tools like Microsoft Access write SQL for you behind the scenes

```
CREATE DATABASE MammalSurveys;
CREATE TABLE SurveyDATA (
    IndivID  INT,
	SpeciesID  VARCHAR,
	BodyMass INT,
	HindFoot INT,
	PRIMARY KEY(IndivID)
);
```

> Assign remaining exercises.
