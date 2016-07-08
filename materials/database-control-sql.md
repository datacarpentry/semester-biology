---
layout: page
element: notes 
title: Database Control
language: SQL
---

> Open Excel spreadsheet. Fill in a couple of columns.

> Open SQLite Manager, if it is not already open.

### Database Control

* There are many ways to add and modify data in a database management system.
    * Enter the data into another program (e.g., a spreadsheet) and import it to SQLite.
    * Get the data from somewhere and import it. 
        * *Though, data isn't always ready to import into a database*
    * Enter the data directly.

### Enter the data into another program

* Quality Assurance in Excel
    * Select column.
    * On the `Data` menu tab, select `Data Validation`.
    * `Settings` tab
        * `Allow:` selects type of data.
        * `Data:` selects condition of value inputs
            * `Value:`
            * `Minimum:`
            * `Maximum:`
    * `Input Message` tab
        * Show input message when cell is selected for entry.
    * `Error Alert` tab
        * `Style:` controls response to invalid input value
            * `Stop`
            * `Warning`
            * `Information`  
        
> Do [Exercise 1 - Data entry validation in Excel]({{ site.baseurl }}/exercises/Qaqc-data-entry-validation-in-excel-SQL/). 

### Import existing data 

> Walk through [Exercise 2 - Importing Data]({{ site.baseurl }}/exercises/Database-control-importing-data-SQL), Tasks 1-10.

> Do [Exercise 2 - Importing Data]({{ site.baseurl }}/exercises/Database-control-importing-data-SQL), Task 11.

### Enter the data directly

> Show students the SQLite Manager `Execute SQL` tab.

* [`CREATE TABLE`](http://www.w3schools.com/sql/sql_create_table.asp) 
    * name table
    * list field names and data types
        * may constrain data values
            * `Null`
            * `Unique`
            * value length

```
CREATE TABLE Experiment(
  LoginID TEXT,
  Project TEXT,
  Experiment INTEGER,
  Hours REAL,
  ExperimentDate TEXT
);
```

* We realized we want to add some more specific configuration to the table.
* Restart requires:

```
DROP TABLE Experiment
```

* Add unique `RecordID` field to be the primary key
* Prevent important values from being `NULL`

```
CREATE TABLE Experiment(
  RecordID INTEGER PRIMARY KEY AUTOINCREMENT,
  LoginID TEXT NOT NULL,
  Project TEXT NOT NULL,
  Experiment INTEGER NOT NULL,
  Hours REAL,
  ExperimentDate TEXT(10)
);
```

> Do [Exercise 3 - Creating Tables]({{ site.baseurl }}/exercises/Database-control-creating-tables-SQL/).

* Add new records
    * [`INSERT INTO`](http://www.w3schools.com/sql/sql_insert.asp) 
    * If values for all fields are being added:

```
INSERT INTO Experiment 
VALUES (1, 'ipav', 'Conditioning', 1, 3.2, '1910-07-05');
```

* Add incomplete records
    * If you are only adding values for some of the possible fields
        * Indicate which fields the values correspond to:

```
INSERT INTO Experiment (LoginID, Project, Experiment, Hours, 
ExperimentDate) 
VALUES ('jane', 'Great Apes', 1, 7, '1967-04-13');
```

> Do [Exercise 4 - Adding Records]({{ site.baseurl }}/exercises/Database-control-adding-records-SQL/).

### Modifying existing records

* [`UPDATE`](http://www.w3schools.com/sql/sql_update.asp) 
    * name table 
    * `SET` values of any or all of the fields 
    * `WHERE` conditions are met
        * *Don't forget the `WHERE` clause or the update statement will
update **all** of the records in the database.*

```
UPDATE Experiment 
SET Hours=7.5, ExperimentDate='1967-04-19' 
WHERE RecordID=2;
```

### Deleting records

* [`DELETE`](http://www.w3schools.com/sql/sql_delete.asp)
    * name table
    * `WHERE` conditions are met
        * *Don't forget the `WHERE` clause or the update statement will
update **all** of the records in the database.*

```
DELETE FROM Experiment 
WHERE LoginID='ipav';
```

> Do [Exercise 5 - Updating Records]({{ site.baseurl }}/exercises/Database-control-updating-records-SQL/).

### SQL - structured query language

* The language of databases
* Even graphical tools like Microsoft Access write SQL for you behind the scenes

```
SELECT * FROM Experiment;
```

> Assign remaining exercises.

