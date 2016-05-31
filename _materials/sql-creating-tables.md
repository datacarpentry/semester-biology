---
layout: page
element: notes 
title: Creating Tables
language: SQL
---

To create new tables in a database we use the [CREATE
TABLE](http://www.w3schools.com/sql/sql_create_table.asp) command. This
command is basically a list of field names and their associated types,
plus contraints we want to put on the field. For example, if we wanted
to create the Experiments table in the Software Carpentry lectures we
would use a command like:

```
CREATE TABLE Experiment(\
  LoginID TEXT,\
  Project TEXT,\
  Experiment TEXT,\
  Hours REAL,\
  ExperimentDate NUM\
)
```

If we wanted to put add a unique RecordID field to be the primary key
and prevent a few important values from being NULL, then we could create
the table using this statement:

```
CREATE TABLE Experiment(
  RecordID INTEGER PRIMARY KEY AUTOINCREMENT,
  LoginID TEXT NOT NULL,\
  Project TEXT NOT NULL,\
  Experiment TEXT NOT NULL,\
  Hours REAL,\
  ExperimentDate NUM\
)
```