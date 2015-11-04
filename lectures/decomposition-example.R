# Compare the abundance time-series of large (>50 g)
# and small (<50 g) small mammals

# Import data
# Handle missing values - weight
# Identify large vs small individuals
  # one individual
  # apply to all individuals
# Turn the data into time-series of counts
# Graph the time-series
library(dplyr)
library(ggplot2)

get_data <- function(){
  # Import data from surveys.csv
  data <- read.csv('surveys.csv')
  return(data)
}

get_size_class <- function(weight, threshold){
  # Determine if a weight is large or small
  if (weight > threshold){
    size_class <- "large"
  }
  else {
    size_class <- "small"
  }
  return(size_class)
}

add_size_classes <- function(df){
  # Add size class data to a data frame
  # Input: data frame with weight column containing size information
  data_size_class <-
    df %>% 
    na.omit() %>% 
    rowwise() %>% 
    mutate(size_class = get_size_class(weight, 50))
  return(data_size_class)
}

get_size_class_ts_data <- function(df){
  # Convert individual data to time-series data for each of a set of size classes
  # Input: data frame with a year column for time
  #        and a size_class column
  ts_data <-
    df %>% 
    group_by(year, size_class) %>% 
    summarize(counts = n())
  return(ts_data)
}

plot_ts_data <- function(df){
  #Plot time-series data by size class
  # Input: data frame with year, size_class, and counts columns
  ggplot(df, aes(x = year, y = counts, color = size_class)) +
    geom_line()
}

data <- get_data()
data_size_class <- add_size_classes(data)
ts_data <- get_size_class_ts_data(data_size_class)
plot_ts_data(ts_data)