---
layout: page
element: notes
title: Shiny
language: R
---

## Package installation

```
install.packages('shiny', 'portalr')
```

## Starting a new App

* New -> Shiny Web App
* Name of App
* Location
* Creates a small example app

## Running the App

* Click the `Run App` button
* This example app makes histograms of times between eruptions of the Old Faithful Geyser
* By default runs in a separate window, but can change to viewer or browser

## Basic structure

* UI - User Interface
    * Describes what the user sees and how they interact with it
* Server
    * Performs calculations, makes graphs, etc.
* Call to `shinyApp` actually create the Shiny App

## Our project

* Make an app that displays time-series of mammal community dynamics at Portal
* Let the use choose which species then want to visualize

## UI

* `titlePanel` controls the title of the page
* `sidebarLayout` controls what is shown in the sidebar
* `mainPanel` controls what is shown in the main page

* Change the title of the page to "Portal Rodent Species Dynamics"

```
titlePanel("Portal Rodent Species Dynamics")
```

* Run App

* Change the sidebar to let us select from the available species

### Loading data

* First get the data using `portalr`

```
library(portalr)
library(dplyr)
library(ggplot2)

abundances <- abundance(shape = "long", time = "date", clean = FALSE)
```

* Then get a list of the species

```
species_list <- unique(abundances$species)
```

* Doesn't need to update during session so put it outside of `server` and `ui`

### Changing Sidebar

* Now change the `sidebarPanel` widget to a `selectInput` box
    * Drop down to select one or more options
    * Arguments
        * Input ID - variable name for storing the selected value
        * label - the header for this piece of the UI
        * choices - the values the user can choose from

```
selectInput("species",
            "Species",
            species_list)
```

* Run App

## Server

* The `server` function is where calculations are done and graphs are made

### Changing the graph

* `renderPlot` function lets us create a plot that can be included in the UI 
* First filter the datset using `dplyr`, then plot with `ggplot`
* `input$species` indicates the value collected from the `selectInput` drop-down

```
output$distPlot <- renderPlot({
    filtered_abundances <- abundances %>% 
      filter(species == input$species)
    ggplot(filtered_abundances, aes(x = censusdate, y = abundance)) +
      geom_line()
```

* This plot will be made in the main panel because `plotOutput("distPlot")`
  displays the output of `output$distPlot

* Run App

## Selecting multiple species

* Can also choose multiple species at once
* Change the UI to allow selecting more than one species
* Change the server to filter and graph multiple species

```
selectInput("species",
            "Species",
            species_list,
            multiple = TRUE)
```

```
filter(species %in% input$species)
```

```
ggplot(filtered_abundances, aes(x = censusdate, y = abundance, color = species))
```

* Run App

## Change the date range

* Allow focus on narrower date range
* Update data code to get min and max dates

```
min_date <- min(abundances$censusdate)
max_date <- max(abundances$censusdate)
```

* Update the UI to have a slider to specify the date range

```
sliderInput("dates",
            "Date Range",
            min = min_date,
            max = max_date,
            value = c(min_date, max_date))
```

* Update the server to filter based on the dates in this input

```
filter(censusdate >= input$dates[1], censusdate <= input$dates[2])
```

## Sharing your app

* Anyone can run your file in RStudio
* Can be run directly from GitHub

```
shiny::runGitHub('portal-explorer', 'weecology')
```

* Can also publish the app on the web
* Need an account on https://shinyapps.io
* Setup and the click `Publish Application` button

[https://ethanwhite.shinyapps.io/portal-explorer/](https://ethanwhite.shinyapps.io/portal-explorer/)


## Add an optional smoother (optional extension for longer time-periods)

* Allow us to look at trends in the time-series

* Add a checkbox to the UI

```
checkboxInput("smoother", 
            "Smoother")
```

* Add an optional smoother to out plot
* Make the basic plot then use a conditional to add (or not) the smoother

```
ts_plot <- ggplot(filtered_abundances, aes(x = censusdate, y = abundance, color = species)) +
    geom_line()
if (input$smoother){
    ts_plot <- ts_plot + geom_smooth()
```
