---
layout: page
element: notes
title: Combining Concepts
language: R
---

* Combining concepts is tricky and comes down to problem solving
* Remember the rules for problem decomposition
    * Break thinks into a few parts
    * Keep breaking them down until each part seems doable
    * Code and test one part at time

## Patterns

* There are some common patterns than can be useful

### Subsetting

```
library(dplyr)

data = data.frame(time = 1:100, runif(100, 1, 10))
window = 10
for (tmin in 1:max(data$time)-window) {
  window_data = filter(data, time >= tmin, time < tmin + window)
}
```

### Nesting

```
data = data.frame(time = 1:100, runif(100, 1, 10))
windows = c(1, 5, 10, 20)
for (window in windows){
  for (tmin in 1:max(data$time)-window) {
    window_data = filter(data, time >= tmin, time < tmin + window)
  }
}
```

### Counting

```
library(dplyr)

data = data.frame(time = 1:100, runif(100, 1, 10))
window = 10
windows_with_no_data = 0
for (tmin in 1:max(data$time)-window) {
  window_data = filter(data, time >= tmin, time < tmin + window)
  if (nrow(window_data) == 0){
      windows_with_no_data = windows_with_no_data + 1
  }
}
```

### Nested conditionals

```
est_mass <- function(volume, veg_type, age){
  if (veg_type == "tree") {
    if (age < 5) {
	  mass <- 1.6 * volume^0.8
	  } else {
	  mass <- 2.65 * volume^0.9
	}
  } else if (veg_type == "grass" | veg_type == "shrub") {
	mass <- 0.65 * volume^1.2
  } else {
	print("I don't know how to convert volume to mass for that vegetation type")
	mass <- NA
  }
  return(mass)
}

est_mass(1.6, "tree", age = 2)
est_mass(1.6, "shrub", age = 5)
```

* First checks if the vegetation type is "tree"
* If it is checks to see if it is < 5 years old
* If so does one calculation, if not does another
* But nesting can be difficult to follow so try to minimize it