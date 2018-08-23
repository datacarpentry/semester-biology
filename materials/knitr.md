---
layout: page
element: notes
title: Knitr
topic: R
---

### Literate programming

* Combine text, code, figures, tables, etc.
* Write papers without having to remember to swap figures
* Automatically generate reports


### Getting started

* `install.packages("rmarkdown")` in console for permanence
* `File` -> `New File` -> `R Markdown`
    * Enter a title and author(s).
    * Choose 'Default Output Format' as `HTML`.
* Generates a basic stub of a `.Rmd` document
    * Customize "front matter" at the top of the document between the `---`.
* Delete everything below the second `---`

### Markdown

* Basic approach to formatting text
* Let's you do
    * `# Headers`
    * `*italics*`
    * `**bold**`
    * `[links](http://google.com)`
    * Lists
        * `*`
        * `1.`

	
<pre><code>
## Concept

Exploration of population dynamic patterns at **The Portal Project**.
How do counts of rodents like *Dipodomys* species change through time?

In this document I will:

1. Load data from the [Portal Project Teaching Database](http://figshare.com/articles/Portal_Project_Teaching_Database/1314459)
2. Process it into population time series
3. And make initial visualizations
</code></pre>

* Easy to read for humans
* Easy to convert into other things for computers

* Press `Knit` to create `HTML` from the document
* Can also create `PDF` & Word versions of our files
    * `PDF` Requires `pandoc` and `TeX` installation
    * Use the `Knit` dropdown or change `output: pdf_document`

* Markdown is common on lots of websites
* Used to create all of the exercises and lectures in this course
* Github will automatically render it
    * [https://github.com/ethanwhite/CV/blob/master/CV.md](https://github.com/ethanwhite/CV/blob/master/CV.md)

### R chunks 

* R Markdown allows you to include code to run in the document
* Click on `Insert` and choose R

<pre><code>
## Required Packages

```{r}
library(dplyr)
library(ggplot2)
```
</code></pre>


* Knitting runs the code and prints its output

<pre><code>
## Data

```{r}
data <- read.csv("https://ndownloader.figshare.com/files/2292172")
head(data)
```
</code></pre>


### Chunk options

* Chunks have lots of useful options
  * Options are described at: [http://yihui.name/knitr/options/](http://yihui.name/knitr/options/)
  * Options will be listed in RStudio if you press tab inside
      the `{r}` brackets at the top of the chunk

<pre><code>```{r, message=FALSE}
library(dplyr)
library(ggplot2)
```</code></pre>

* `cache=TRUE` reuses results of the code chunk in subsequent "knits". Save time
re-calculating or re-downloading it each time.

<pre><code>```{r, cache=TRUE}
data <- read.csv("https://ndownloader.figshare.com/files/2292172")
head(data)
```</code></pre>

* You can run code inside your text, too:

```
The data includes `r length(unique(data$species_id))` species.
```

### Analysis Example

<pre><code>## Analysis

Get the time-series of counts for all species.
          
```{r}
time_series <-
  data %>%
  group_by(species_id, year) %>%
  summarize(count = n()) %>%
  filter(species_id %in% c('DM', 'DO', 'DS')) %>%
  na.omit()

head(time_series)
```</code></pre>

* `echo=FALSE` let's you show the results of the code chunk without showing the code.

<pre><code>## Plot the time-series.

```{r, message=FALSE, echo=FALSE, cache=TRUE}
ggplot(time_series, aes(x = year, y = count)) +
  geom_point() +
  geom_line() +
  geom_smooth() +
  facet_wrap(~species_id)
```</pre></code>

### Notebook

* In RStudio run chunks using `Ctrl-Shift-Enter` or `Cmd-Shift-Enter`
* Displays results in the editor

* Notebook

* `output: html_notebook` or File -> New File -> R Notebook


### R Presentations

* `File` -> `New File` -> `R Presentation`
    * Save to location.
    * `Rpres` generates `MD` and directory of figures.

* Template `Rpres` file includes title page and sample code blocks.

<pre><code>Untitled
========================================================
author: 
date: 
autosize: true


First Slide
========================================================

For more details on authoring R presentations please visit <https://support.rstudio.com/hc/en-us/articles/200486468>.

- Bullet 1
- Bullet 2
- Bullet 3

Slide With Code
========================================================

```{r}
summary(cars)
```</code></pre>

* `Preview` in RStudio panel
* Convert to `HTML`
    * `More` -> `View in Browser` or `Save As Web Page...`
