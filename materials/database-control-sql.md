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

* Create a new table by clicking on `Create Table` in the `Table` dropdown menu.
* Fill in `Table Name:`
* Complete the `Define Columns` section. 
    * Fill in `Column Names`.
    * Choose `Data Type`. 
    * Choose toggle options.
        * `Primary Key?` and `Autoinc?`
        * `Allow Null?`
        * `Unique?`
* Click `OK`.
* Click `Yes`.

> Do [Exercise 3 - Creating Tables]({{ site.baseurl }}/exercises/Database-control-creating-tables-SQL/).

> Show students the SQLite Manager `Browse & Search` tab.

* Add new records by clicking on the `Add` button from the `Browse & Search` panel.
* Check `Table Name:`.
* `Enter Field Values`.
* Click `OK`.
* Click `OK`.
* Add another entry or click `Cancel`.

> Do [Exercise 4 - Adding Records]({{ site.baseurl }}/exercises/Database-control-adding-records-SQL/).

### Modifying existing records

* Select record on `Browse & Search` panel.
* Click on the `Edit` button.
* Modify record in `Enter Field Values`.
* Click `OK`.
* Click `OK`.
* Click `Cancel`.

### Deleting records

* Select record on `Browse & Search` panel.
* Click on the `Delete` button.
* Click `Yes`.

> Do [Exercise 5 - Updating Records]({{ site.baseurl }}/exercises/Database-control-updating-records-SQL/).

### Deleting a table

* Click on `Drop Table` in the `Table` dropdown menu.
* Click `Yes`.

### SQL - structured query language

* The language of databases
* Even graphical tools like Microsoft Access write SQL for you behind the scenes

> Show students the SQLite Manager `Execute SQL` tab.

```
SELECT * FROM Experiment;
```

> Assign remaining exercises.

