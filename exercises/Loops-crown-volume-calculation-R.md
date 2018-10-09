---
layout: exercise
topic: Loops
title: Crown Volume Calculation
language: R
---

The
[UHURU experiment](http://www.esapubs.org/archive/ecol/E095/064/metadata.php) in
Kenya has conducted a survey of *Acacia* and other tree species in ungulate
exclosure treatments. Data for the tree data is
available [here](http://www.esapubs.org/archive/ecol/E095/064/TREE_SURVEYS.txt)
in a tab delimited (`"\t"`) format. Each of the individuals surveyed were
measured for tree height (`HEIGHT`) and canopy size in two directions (`AXIS_1`
and `AXIS_2`). Read these data in using the following code: 

```
tree_data <- read.csv("http://www.esapubs.org/archive/ecol/E095/064/TREE_SURVEYS.txt",
                 sep = '\t',
                 na.strings = c("dead", "missing", "MISSING",
                                "NA", "?", "3.3."),
                 stringsAsFactors = FALSE)
```


You want to estimate the crown volumes for the different species and have
developed equations for species in the *Acacia* genus:

```
volume = 0.16 * HEIGHT^0.8 * pi * AXIS_1 * AXIS_2
```

and the *Balanites* genus:

```
volume = 1.2 * HEIGHT^0.26 * pi * AXIS_1 * AXIS_2
```

For all other genera you'll use a general equation developed for trees:

```
volume = 0.5 * HEIGHT^0.6 * pi * AXIS_1 * AXIS_2
```

1. Write a function called `tree_volume_calc` that calculates the canopy volume for the *Acacia* species in the dataset. To do so, use an if statement in combination with the `str_detect()` function from the `stringr` R package. The code `str_detect(SPECIES, "Acacia")` will return `TRUE` if the string stored in this variable contains the word "Acacia" and `FALSE` if it does not. This function will have to take the following arguments as input: SPECIES, HEIGHT, AXIS_1, AXIS_2. Then run the following line: 

	`tree_volume_calc("Acacia_brevispica", 2.2, 3.5, 1.12)`

2. Expand this function to additionally calculate canopy volumes for other types of trees in this dataset by adding if/else statements and including the volume equations for the *Balanites* genus and other genera. Then run the following lines: 

	`tree_volume_calc("Balanites", 2.2, 3.5, 1.12)`
	`tree_volume_calc("Croton", 2.2, 3.5, 1.12)`

3. Now get the canopy volumes for all the trees in the `tree_data` dataframe and add them as a new column to the data frame. You can do this using `tree_volume_calc()` and either `mapply()` or using `dplyr` with `rowwise` and `mutate`. 
