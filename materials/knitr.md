---
layout: page
element: notes
title: Knitr
language: R
---

### Literate programming

* Combine text, code, figures, tables, etc.
* Write papers without having to remember to swap figures
* Automatically generate reports


### Getting started

* Open RStudio
* `File` -> `New File` -> `R Markdown`
    * Enter a title and author(s).
    * Choose 'Default Output Format' as `HTML`.
* Generates a basic stub of a `.Rmd` document
    * Customize "front matter" at the top of the document between the `---`. 
* Press `Knit` to create an `HTML` from the document
    * 1st time may ask you to install some packages
    * `install.packages("rmarkdown")` in console for permanence
* Runs the code in the code chunks and prints their output along with the
  markdown formatted text
* Can also create `PDF` & Word versions of our files
    * `PDF` Requires `pandoc` and `TeX` installation
    * Use the `Knit` dropdown or change `output: pdf_document`
* R Notebook
    * `output: html_notebook`
    * "Interactive R Markdown" 
        * execute individual code chunks
        * output in editor pane  

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
    * [https://github.com/ethanwhite/CV/blob/master/CV.md](https://github.com/ethanwhite/CV/blob/master/CV.md)

<pre><code>Explore patterns in population dynamics at Portal.

## Required Libraries</code></pre>

### R chunks 

* Set R code inside a set of <code>```</code> with the `{r}` designation

<pre><code>```{r}
```</code></pre>

* Code that you write inside chucnks gets executed during the "knit" process and 
the results are shown below.

<pre><code>```{r}
library(dplyr)
```</code></pre>

* Chunks have lots of useful options
  * Options are described at: [http://yihui.name/knitr/options/](http://yihui.name/knitr/options/)
  * Options will be listed in RStudio if you press tab inside
      the `{r}` brackets at the top of the chunk

<pre><code>```{r, message=FALSE}
library(dplyr)
```</code></pre>

<pre><code>```{r, message=FALSE}
library(dplyr)
library(ggplot2)
```</code></pre>

<pre><code>```{r, message=FALSE, warning=FALSE}
library(dplyr)
library(ggplot2)
```</code></pre>

* You can run code inside your text, too:
    * <code>`r cos(pi)`</code> turns into `-1` when you press the `Knit` button.
    * We will see and example of this later.

### Analysis Report Example

* Here's a text segment linked to a code chunk that begins an analysis report.

<pre><code>## Data

Data is from the [Portal project teaching database](http://figshare.com/articles/Portal_Project_Teaching_Database/1314459) 
published on Figshare. We need the surveys table for our analysis:

```{r, cache=TRUE}
download.file("https://ndownloader.figshare.com/files/2292172", 
              "surveys.csv")
data <- read.csv("surveys.csv")
```</code></pre>

* Setting `cache=TRUE` lets you reuse the results of this code chunk in
subsequent "knits" instead of re-calculating or re-downloading it each time.

<pre><code>## Analyze population time-series

Get the time-series of counts for all species.
          
```{r}
time_series <-
  data %>%
  group_by(species_id, year) %>%
  summarize(count = n()) %>%
  na.omit()

head(time_series)
```</code></pre>

* `echo=FALSE` let's you show the results of the code chunk without showing the code.

<pre><code>## Plot the time-series.

```{r, message=FALSE, echo=FALSE, cache=TRUE}
ggplot(time_series, aes(x = year, y = count)) +
  geom_point() +
  geom_line() +
  facet_wrap(~species_id) +
  scale_x_continuous(breaks = pretty_breaks(n=2))
```

## A simple model

```{r, echo=FALSE}
model <- data %>% group_by(year) %>% 
  summarize(count = n()) %>% 
  lm(count ~ year, data = .)

results <- anova(model)
```</code></pre>

* Here's the example of an inline code chunk.

<pre><code>We found a marginally significant linear relationship between the
total count and year (p = `r round(results[["Pr(>F)"]][1], 3)`; see
Table 1 for more details)

```{r, echo=FALSE}
knitr::kable(results, caption = "Table 1")
```</code></pre>

* `knitr::kable()` is a handy way to make nice-looking tables from data frames.

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