# Introduction to databases

## Database management systems

* Designed for storing, managing, and retrieving information
* We will be working with Relational Databases
    * We will use Microsoft Access
    * But there are lots of alternatives

## Key features of database management systems

* Data is separate from manipulations of the data
* Tables - store the data
* Queries - store questions about the data
    * If we update the data, the query asks the same question of the new data

## Relational databases

* Data is stored in tables
    * One table per type of data
	* Tables can be linked together to combine information
* Each row contains a single record
    * A single observation or data point
* Each column contains a single attribute
    * A single type of information

### Example

![Basic table structure](databases_basic_table_structure.png)

## Multiple tables

* It is often not efficient to include all information of interest in a single
table.

![Table with redundant information](databases_redundant_table.png)

* To solve these problems we store data in multiple tables
* And connect the data in different tables using Joins or Relationships (hence
  "relational" database)
* Each table contains a single data type

![Restructuring a redundant table into two](databases_redundant_table_restructure.png)

## Alternative structures

Cross-tablulated data

![Cross-tabulated data table](databases_crosstab_table.png)

![Cross-tab table restructure](databases_crosstab_restructured.png)

## Types

* Fields in databases have types that define the kind of data they contain
* Each field/column can only have one type
* We have to define the types in advance
* Types include
    * Integer
	* Text
	* Decimal/Double
* Types are highly configurable because space is limiting
    * Maximum value of integers
	* Maximum length of text
	* How many values before and after the decimal place

## Primary keys

* Every table "needs" a column (or set of columns) that is unique across
  records/row
* This is called the primary key
* The easiest way to do this is to use an Integer that increments every time a
  new record is added
* Many databases that you import will already have a field like this

## SQL - structured query language

* The language of databases
* Even graphical tools like Microsoft Access write SQL for you behind the scenes

```sql
CREATE DATABASE MammalSurveys;
CREATE TABLE SurveyDATA (
    IndivID  INT,
	SpeciesID  VARCHAR,
	BodyMass INT,
	HindFoot INT,
	PRIMARY KEY(IndivID)
);
```
