---
layout: page
element: notes
title: Database Structure
language: SQL
---

## Five basic rules of database structure

1. Order doesn’t matter 
2. No duplicate rows
3. Every cell contains one value
4. One column per type of information
5. No redundant information

### 1. Order doesn't matter

* The information should not be dependent on the order of the rows or the order 
of the columns

![Order of rows doesn't matter example]({{ site.baseurl }}/materials/database-struct-order-doesnt-matter.png)

### 2. No duplicate rows

![No duplicate rows example]({{ site.baseurl }}/materials/database-struct-no-dup-rows.png)

### 3. Every cell contains one value

* This is an example of what not to do.

![One value per cell example]({{ site.baseurl }}/materials/database-struct-one-val-per-cell.png)

* How would you query for `'Shrubland'`?

### 4. One column per type of information

* This is also an example of what not to do.

![One column per type of information example]({{ site.baseurl }}/materials/database-struct-one-col-per-type.png)

* How would you query for records with `'Grassland' AND 'Shrubland'`?

#### Restructure the examples of what not to do for #3 and #4.

![How to restructure to keep no duplicate rows and one value per cell]({{ site.baseurl }}/materials/database-struct-multiple-habitat-values.png)

* The proper structure lets us easily subset the data however we want.

#### Cross-tablulated data is difficult for SQL to work with.

![Cross-tab table restructure]({{ site.baseurl }}/materials/databases-crosstab-restructured.png)

### 5. No redundant information
  
![No redundant information example]({{ site.baseurl }}/materials/database-struct-no-redundant-information.png)

* Redundant information makes it more difficult to update or revise data. 
    * If something changes we want to be able to change it in one place, not hundreds of places.     
* Use multiple tables to avoid redundant information. 
    * Easier and less error prone
    * Use a Unique `RecordID` to link tables with complementary information.

## Multiple tables

* It is often not efficient to include all information of interest in a single
table.

![Table with redundant information]({{ site.baseurl }}/materials/databases-redundant-table.png)

* To solve these problems,
    * store data in multiple tables, and 
    * connect the data in different tables using `JOIN` to describe 
      relationships between tables (*hence "relational" database*)
* Each table contains a single data type

![Restructuring a redundant table into two]({{ site.baseurl }}/materials/databases-redundant-table-restructure.png)
