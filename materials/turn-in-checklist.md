---
layout: page
title: Assignment turn in checklist
---

#### Clean up your code

Code should be easy to read and understand.

- Only include code and comments necessary for the assignment. Remove anything else (e.g., notes taken during class, commented code that isn't needed anymore).
- Remove extra/duplicate files. Only turn in what is necessary for the assignment.
- Clearly label problems using comments.

#### Make sure your code runs like you think it does

Code should run from the start of the file to the end of the file without problems. To make sure this is true:

- Clear the R environment by clicking on the broom icon on the `Environment` tab.
- Run the entire file by either clicking the `Source` button or using the `Ctrl-Shift-Enter` keyboard shortcut.

#### Work with data files appropriately

Code should run the same way regardless of which computer it is run on. In order to grade your code someone will need to run it on another computer. To make sure your code will work on another computer:

- Do not use setwd()
- Use relative paths, not absolute paths. E.g., use `data/mydata.csv` instead of `C:\Users\Batman\DataCarp\data\mydata.csv`.
- Make filenames in the code match the actual filenames exactly including capitalization
