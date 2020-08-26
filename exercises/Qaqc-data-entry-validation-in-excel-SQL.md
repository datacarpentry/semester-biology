---
layout: exercise
topic: QAQC
title: Data entry validation in Excel
language: SQL
---

Create a spreadsheet in Excel for data entry. It should have five columns: Date, Site, Species, Mass, and Length.

Set the following data validation criteria to prevent invalid data from getting entered:

1. The Date column should be set so that it doesn't convert dates to other formats.
2. Use data validation so that Site can only be one of the following `A1`, `A2`, `B1`, `B2`. Set the error message on this validation criteria to provide information on what the valid values are.
3. Use data validation so that Species can only be one of the following `Dipodomys spectabilis`, `Dipodomys ordii`, `Dipodomys merriami`. Set the error message on this validation criteria to provide information on what the valid values are.
4. Use data validation so that Mass can only be a decimal greater than or equal to zero but less than or equal to 500. Set the error message on this validation criteria to provide information on what the valid values are.
5. Length should be an integer (i.e., a whole number) between 1 and 10. Set the error message on this validation criteria to provide information on what the valid values are.

Check that the validation rules and data formating are working, but do not include any entered data in the final file.
 
Save this file as `data_entry_form.xlsx`.
