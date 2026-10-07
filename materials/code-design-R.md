---
layout: page
element: notes
title: Code Design
language: R
---

### Code design with functions

* Functions let us break code up into logical chunks that can be understood in isolation
* Write functions at the top of your code then call them at the bottom
* The functions hold the details
* The function calls show you the outline of the code execution

```r
clean_data <- function(data){
  do_stuff(data)
}

process_data <- function(cleaned_data){
  do_dplyr_stuff(cleaned_data)
}

make_graph <- function(processed_data){
  do_ggplot_stuff(processed_data)
}

raw_data <- read_csv('mydata.csv')
cleaned_data <- clean_data(raw_data)
processed_data <- process_data(cleaned_data)
make_graph(processed_data)
```

### Documentation & Comments

* Documentation
    * How to use code
    * Use Roxygen comments for functions
* Comments
    * Why & how code works
    * Only if it code is confusing to read
