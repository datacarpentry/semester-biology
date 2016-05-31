---
layout: page
element: notes
title: Database Structure
language: R
---

## Five basic rules of database structure

1. Order doesn’t matter
    * The information should not be dependent on the order of the rows or the
      order of the columns
2. No duplicate rows
3. Every row - column combination contains one value
4. One field per type of information
5. No redundant information

## Order doesn't matter

![Order of rows doesn't matter example](database_struct_order_doesnt_matter.png)

## No duplicate rows

![No duplicate rows example](database_struct_no_dup_rows.png)

## One value per cell

Don't do this.

![One value per cell example](database_struct_one_val_per_cell.png)

How would you query for Shrubland?

## One column per type of information

Don't do this either.

![One column per type of information example](database_struct_one_col_per_type.png)

How would you query for records with Grassland and Shrubland?

## Proper structure

![How to restructure to keep no duplicate rows and one value per cell](database_struct_multiple_habitat_values.png)

This lets us easily subset the data however we want.

## No redundant information

![No redundant information example](database_struct_no_redundant_information.png)
