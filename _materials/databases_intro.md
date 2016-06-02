---
layout: page
element: notes
title: Introduction to Databases
language: R
---

**If you haven't already install Firefox**

**Walk through installing SQLite Manager add-on**

## Why use a database management system

* Designed for storing, managing, and retrieving information
* Lots of existing data is stored in them
* Fast for large amounts of data
* Out of memory processing for really large data
* Improve quality control of data entry (type constraints and use of forms in
  Access, Filemaker, etc.)
* Can handle a spatially explicit queries (GIS)
* The concepts of relational database querying are core to understanding how to
  do similar things using programming languages such as R or Python.

## Database management systems

* We will be working with Relational Databases
* We will use SQLite
    * Simple, almost no work to set up, single file
	* But there are lots of alternatives
	* Access - commonly used, GUI
	* PostgreSQL - fast/powerful, lots of users

**Open SQLite w/Portal DB**

## Key features of database management systems

* Data is separate from manipulations of the data
* Tables - store the data
* Queries - store questions about the data
    * If we update the data, the query asks the same question of the new data

## Relational databases

**Demo in SQLite**

* Data is stored in tables
    * One table per type of data
	* Tables can be linked together to combine information
* Each row contains a single record
    * A single observation or data point
* Each column contains a single attribute
    * A single type of information

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
