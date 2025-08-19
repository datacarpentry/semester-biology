---
layout: page
element: notes
title: gganimate
language: R
---

### Installation

```r
# gifski required for default gif output
install.packages(c("gganimate", "gifski", "lubridate", "rnoaa"))
```

### Example

* Example using weather data
* Get this data using `rnoaa`

```r
library(gganimate)
library(ggplot2)
library(lubridate)
library(rnoaa)

gnv_weather <- meteo_pull_monitors("USW00012816", date_min = "1984-01-01", date_max = "2024-12-31")
```

* Plot annual temperature pattern through time
* First make a plot of the annual temperature trend using ggplot

```r
gnv_weather$year = as.integer(year(gnv_weather$date))
gnv_weather$jday = yday(gnv_weather$date)
gnv_weather$tmax = gnv_weather$tmax / 10

ggplot(gnv_weather, aes(x = jday, y = tmax)) +
  geom_line()
```

* This plot shows the temperatures of each day of the year for all years from 1984 to 2024
* Let's animate them so we can see the pattern over time

* Add `transition_time` element to

```r
ggplot(gnv_weather, aes(x = jday, y = tmax)) +
  geom_line() +
  transition_time(year)
```

* Now let's add some information on year to the graph
* Do this by adding a title that shows the time (in our case year) for each frame

```r
ggplot(gnv_weather, aes(x = jday, y = tmax)) +
  geom_line() +
  labs(title = 'Year: {frame_time}') +
  transition_time(year)
```

* Add a shadow mark to the plot so that we can see where previous years were

```r
ggplot(gnv_weather, aes(x = jday, y = tmax)) +
  geom_line() +
  labs(title = 'Year: {frame_time}') +
  transition_time(year) +
  shadow_mark(color = 'gray', linewidth = 0.2)
```

* If we want more control over the animation store the ggplot object and use `animate()`

```r
p <- ggplot(gnv_weather, aes(x = jday, y = tmax)) +
  geom_line() +
  labs(title = 'Year: {frame_time}') +
  transition_time(year) +
  shadow_mark(color = 'gray', linewidth = 0.2) +
  ease_aes('linear')

animate(p, fps = 2, end_pause = 50)
```
