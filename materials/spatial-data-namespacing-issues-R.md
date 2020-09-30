---
layout: page
element: notes
title: Spatial Data Namespacing Issues
language: R
--- 

### Namespacing

```
library(dplyr)
library(raster)
```

* `raster`'s `select` function overwrites `dplyr`'s `select` function
* *Demo error*

```r
select(do_data, Dipodomys_ordii.latitude)
```

* To use `dplyr`'s function

```r
dply::select(do_data, Dipodomys_ordii.latitude)
```