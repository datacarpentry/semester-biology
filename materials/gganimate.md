---
layout: page
element: notes
title: gganimate
language: R
---

### Installation

* Some R packages are not published to CRAN
* Can install from other places using `devtools`

```
install.packages("devtools")
devtools::install_github("dgrtwo/gganimate")
```

### Example

* Example using weather data
* Get this data using `rnoaa`

```
install.packages('rnoaa')
library('rnoaa')
gnv_weather <- meteo_pull_monitors("USW00012816", date_min = "1984-01-01", date_max = "2016-12-31")
```
* Plot annual temperature pattern through time
* First make a plot of the annual temperature trend using ggplot

```
library(ggplot2)
library(gganimate)

gnv_weather$year = format(gnv_weather$date, "%Y")
gnv_weather$jday = format(gnv_weather$date, "%j")
gnv_weather = filter(gnv_weather, tmax > 

ggplot(gnv_weather, aes(x = jday, y = tmax / 10)) +
  geom_point()
```

* Then add `frame` element to `aes()`

```
p <- ggplot(gnv_weather, aes(x = jday, y = tmax / 10, frame = year))
  + geom_point()

gganimate(p)
```

* Uses the `animation` package
* Fore complicated but more powerful

```
saveGIF({
  for (yr in 1984:2016){
    data = filter(gnv_weather, year == yr)
    plot(data$jday, data$tmax)
  }
})
```
