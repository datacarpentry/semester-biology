---
layout: page
element: notes
title: Data Entry
language: Excel
---

### Plan

* What's the first thing to do when you are ready to enter data?
* Plan a data structure follows tidy data rules
* Ideally plan before you collect data and match datasheets to entry format

### Where to enter data

* Spreadsheet
* Text file
* Database
* Form (web or GUI databases)

* All of these are reasonable options
* When used properly spreadsheets or forms for databases can provide additional
protection against bad data being entered
* Be careful of data conversion issues from spreadsheets

> Show posts/papers on dates and gene names
>
> * [https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-1044-7](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-1044-7)
> * [https://uc3.cdlib.org/2014/04/09/abandon-all-hope-ye-who-enter-dates-in-excel/](https://uc3.cdlib.org/2014/04/09/abandon-all-hope-ye-who-enter-dates-in-excel/)

### Quality Assurance

* Stopping bad data from ever being entered
* Set rules about what values can be entered into a column

* Select an area of cells, most often a column
* `Data -> Data Validation`
* Choose the data type: `Whole numbers` (only that type can be entered)
* Set limitations
    * Use `Data` to set the type of limitation: `between` 
    * Then use additional boxes to provide specifics: `1` and `10`
* Add a message to explain what goes in a cell in `Input Message`
* Add a useful error message using `Error Alert`

* Make lists of choices
    * `Allow` = `List`
    * Enter list values in `Sources`: DM, DO, DS, PP, PM

> Demo a data entry form in Excel or Google Forms

> Do [Exercise 2 - Data Entry Validation in Excel]({{ site.baseurl }}/exercises/Qaqc-data-entry-validation-in-excel-SQL/).

### Quality Control

* Looking for bad data that has already been entered
* Sort
* Graph
* Check for realistic ranges of values
