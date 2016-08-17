---
title: Knitr
layout: default
---

### Literate programming

* Combine text, code, figures, tables, etc.
* Write papers without having to remember to swap figures
* Automatically generate reports


### Getting started

* File -> New File -> R Markdown
* Enter a title and author(s)
* Shows a basic stub of a document
* Press `Knit PDF` to create a pdf from it
    * 1st time may ask you to install some packages
* Runs the code in the code chunks and prints their output along with the
  markdown formatted text


### Markdown

* Basic approach to formatting text
* Let's you do
    * `*italics*`
    * `**bold**`
    * `[links](http://google.com)`
    * Lists
        * `*`
        * `1.`
    * `# Header`
* Easy to read for humans
* Easy to convert into other things for computers
* Common on lots of websites
* Used to create all of the exercises and lectures in this course
* Github will automatically render it
    * https://github.com/ethanwhite/CV/blob/master/CV.md


### Example

	Explore patterns in population dynamics at Portal.

	## Required Libraries 
	```{r}
	library(dplyr)
	library(ggplot2)
	```

	## Data

    Data is from the [Portal project teaching database]() published on Figshare.
    We need the surveys table for our analysis:

	```{r}
	download.file("http://files.figshare.com/2292172/surveys.csv", "surveys.csv")
	data <- read.csv("surveys.csv")
	```

	## Analyze population time-series

	Get the time-series of counts for all species.

	```{r}
	time_series <-
	  data %>%
	  group_by(species_id, year) %>%
	  summarize(count = n()) %>%
	  na.omit()

	head(time_series)
	```

	Plot the time-series.

	```{r}
	ggplot(time_series, aes(x = year, y = count)) +
	  geom_point() +
	  geom_line() +
	  facet_wrap(~species_id)
	```

* Clean up by adding
    * `message=FALSE` to first and last chunk
    * `echo=FALSE` to last chunk
    * `library(scales)` & `scale_x_continuous(breaks=pretty_breaks(n=2))`

### Output formats

* In addition to pdf we can also create html & Word versions of our files
* Use the `Knit` dropdown or change `output`: `html_document`
