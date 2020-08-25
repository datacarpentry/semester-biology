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
* Let's create a data table with information on the date of sampling, the plot being sampled, and Species ID and mass of each individual small mammal that we catch.
* Header row: `Plot`, `SpeciesID`, `Mass`

* To setup a quality assurance rule let's select the Plots column
* `Data -> Data Validation`
* Plot numbers are integers so choose the data type: `Whole numbers` (only that type can be entered)
* Set limitations
    * Use `Data` to set the type of limitation: `between` 
    * There are 24 plots so use boxes to provide limit the possible values to between `1` and `24`
* Add a message to explain what goes in a cell in `Input Message`
    * "Valid plot numbers are 1-24"
* Add a useful error message using `Error Alert`
    * "Plot numbers must be whole numbers 1-24"

* Now enter some plot data
* The numbers 1-24 are entered normally
* If we try to enter an invalid number, e.g., 222, we get an error
* If we hover over a cell we see the description of what is valid

* We can also limit decimal numbers
* Select `Mass` column
* `Data -> Data Validation` -> `Allow` = `Decimal`
* Masses have to be positive, so set `Minimum` = 0
* The largest mammal that can fit in the small traps used in this study is 300 g, so set `Maximum` = 300


* Limit entries to a list of choices
* This allows us to control data entry for fields like Species ID
* Select `SpeciesID` column
* `Data -> Data Validation` -> `Allow` = `List`
* Enter list values in `Sources`: DM, DO, DS, PP, PM
* Trying to enter a value not on the list results in an error
* This also generates a drop-down menu, so we can select the SpeciesID instead of typing it in

### Entering Dates

* As I mentioned at the beginning dates (and things that look like dates) can get changed by Excel
* E.g., if we enter the date 2020-02-26 and hit Enter it will get converted to 2/26/2020
* One solution to this is to tell Excel that the dates are text
* Select the Date column
* `Home` -> `Number` -> Dropdown -> Text
* This will ensure that dates will remain in the form you entered them and will export properly for analysis in R or other languages

> Demo a data entry form in Excel or Google Forms

> Do [Exercise 2 - Data Entry Validation in Excel]({{ site.baseurl }}/exercises/Qaqc-data-entry-validation-in-excel-SQL/).

### Quality Control

* Looking for bad data that has already been entered
* Sort
* Graph
* Check for realistic ranges of values
