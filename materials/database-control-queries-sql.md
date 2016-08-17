---
layout: page
element: notes 
title: Database Control Queries
language: SQL
---

* This is an advanced treatment of [Database Control]({{ site.baseurl }}/materials/database-control-sql) using queries instead of SQLite Manager tabs.

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