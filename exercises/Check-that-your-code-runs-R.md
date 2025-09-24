---
layout: exercise
topic: Data Analysis
title: Check That Your Code Runs
language: R
---

Sometimes you think you're code runs, but it only actually works because of something else you did previously. To make sure it actually runs you should save your work and then run it in a clean environment.

Follow these steps in RStudio to make sure your code really runs:

1\. Restart R (see above) by clicking `Session` in the menu bar and selecting `Restart R`:

![Screenshot showing clicking session from the menu bar and selecting Restart R]({{ site.baseurl}}/exercises/restart-r-screenshot.png)

2\. If the `Environment` tab isn't empty click on the broom icon to clear it:

![Screenshot showing the Environment tab with the cursor hovering over the broom icon]({{ site.baseurl}}/exercises/clear-rstudio-environment-screenshot.png)

The `Environment` tab should now say "Environment Is Empty":

![Screenshot showing the Environment tab with only the words Environment Is Empty]({{ site.baseurl}}/exercises/empty-rstudio-environment-screenshot.png)

3\. Rerun your entire homework assignment using "Source with Echo" to make sure it runs from start to finish and produces the expected results.

![Screenshot showing the RStudio Source with Echo item hovered in the Source dropdown]({{ site.baseurl}}/exercises/rstudio-source-with-echo-screenshot.png)

4\. Make sure that you saved your code with the name `assignment` somewhere in the file name. You should see the file in the `Files` tab and the name of the file should be black (not red with an `*` in the tab at the top of the text editor):

![Screenshot showing the Files tab with the cursor hovering over the assignment file]({{ site.baseurl}}/exercises/saved-assignment-in-files.png)

![Screenshot showing the file name in the editor tab and it is black and there is no *]({{ site.baseurl}}/exercises/saved-assignment-tab.png)

5\. Make sure that your code will run on other computers
  - No `setwd()` (use RStudio Projects instead)
  - Use `/` not `\` for paths
