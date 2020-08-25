---
layout: page
element: notes
title: Tidy Data
language: SQL
---

* Tidy data is data that is well designed for working with using computers
* Creating tidy data as you collect it will make it much easier to analyze it later
* Let's start by looking at some messy data and thinking about what makes it
messy and what we could do to improve it.

> Do the exercise on [Improving Messy Data]({{ site.baseurl }}/exercises/Tidy-data-improving-messy-data-SQL).
>
> * Put the data up on the screen
> * Ask the class for things they would improve and how to fix them
> * Talk through anything that can be improved about their answers


### Make it a rectangle

* Only rows and columns, no additional structure
* One column for each type of information
* One row for each observation (i.e., data point)

#### Bad:

| Plot | SpeciesA | SpeciesB |
|------|----------|----------|
| 1    | 3        | 1        |
| 2    | 2        | 4        |

#### Good:

| Plot | Species | Abundance |
|------|---------|-----------|
| 1    |    A    |     3     |
| 1    |    B    |     1     |
| 2    |    A    |     2     |
| 2    |    B    |     4     |


### One cell one value

* Every cell contains one piece of information

#### Bad:

| Mass  |
|-------|
| 26g   |
| 0.2kg |

#### Good:

| Mass | Unit |
|------|------|
| 26   | g    |
| 0.2  | kg   |


### Don't confuse the computer

* Don't use colors, fonts, italics, or anything visual as data. It's hard to tell the computer to treat yellow cells or bolded numbers differently.
* Avoid spaces in names. Computers use spaces to separate commands. Use `_` or CamelCase to include multiple words.
* Avoid special characters like @ * and ^. These often mean special things to computers, which can make data harder to work with.

#### Bad:

| Min Temp  |
|-----------|
| 76.5      |
| 62.2      |
| **100.3** |

| Min Temp  |
|-----------|
| 76.5      |
| 62.2      |
| 100.3*    |

#### Good:

| min_temp | calibration_error |
|----------|-------------------|
| 76.5     | 0                 |
| 62.2     | 0                 |
| 100.3    | 1                 |


### Be clear and consistent

* Use short meaningful names. 
* Use consistent names, abbreviations, and capitalizations
* Use good null values (not -999, blanks good, some prefer NA etc. but language specific)
* Write dates as YYYY-MM-DD or have separate Year, Month, and Day columns

#### Bad:

| d              | s       |    a      |
|----------------|---------|-----------|
| 02/26/2020     |  dior   |     3     |
| 02/26/2020     |  disp   |     1     |
| March 24, 2020 |  DIor   |   -999    |
| March 24, 2020 |  DISP   | Missing   |

#### Good:

| Date       | Species | Abundance |
|------------|---------|-----------|
| 2020-02-26 |  dior   |     3     |
| 2020-02-26 |  disp   |     1     |
| 2020-03-24 |  dior   |     NA    |
| 2020-03-24 |  disp   |     NA    |


### Use one table for each category of data

* Avoid duplicated chunks of data using multiple tables
* Use one table for each category of data

#### Bad:

| Family       | Genus     | Species     | Plot | Abundance |
|--------------|-----------|-------------|------|-----------|
| Heteromyidae | Dipodomys | Spectabilis | 1    | 2         |
| Heteromyidae | Dipodomys | Spectabilis | 2    | 7         |
| Heteromyidae | Dipodomys | Spectabilis | 3    | 5         |
| Heteromyidae | Dipodomys | Spectabilis | 4    | 3         |
| Heteromyidae | Dipodomys | Ordii       | 1    | 5         |
| Heteromyidae | Dipodomys | Ordii       | 2    | 9         |
| Heteromyidae | Dipodomys | Ordii       | 3    | 12        |
| Heteromyidae | Dipodomys | Ordii       | 4    | 11        |

* Difficult to update (e.g., if taxonomy updates)
* More error prone
* Takes up more space

#### Good:

| SpeciesID | Plot | Abundance |
|-----------|------|-----------|
| disp      | 1    | 2         |
| disp      | 2    | 7         |
| disp      | 3    | 5         |
| disp      | 4    | 3         |
| dior      | 1    | 5         |
| dior      | 2    | 9         |
| dior      | 3    | 12        |
| dior      | 4    | 11        |

| SpeciesID | Family       | Genus     | Species     |
|-----------|--------------|-----------|-------------|
| disp      | Heteromyidae | Dipodomys | Spectabilis |
| dior      | Heteromyidae | Dipodomys | Ordii       |

* Only need to make changes in a single location
* Less repetative typing


### Export data into easy to read formats

* Save data in plain text files.
* Files -> Save As -> Select .csv
