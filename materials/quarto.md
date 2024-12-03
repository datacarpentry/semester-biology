---
layout: page
element: notes
title: Quarto
language: R
---

### Literate programming

* Combine text, code, figures, tables, etc.
* Quickly generate websites
* Automatically generate reports
* Easy to share results and code with collaborators

### Getting started

```r
install.packages(c("quarto", "dplyr", "ggplot2", "gt", "readr"))
```

* `File` -> `New File` -> `Quarto Document`
* Title: `Portal Population Dynamics`
* Default Output Format: `HTML`
* Uncheck `Use visual markdown editor`
* `Create`
* Generates a basic stub of a `.qmd` document
* The material between the `---`'s is called "front matter"
* Metadata about the document
* Title, author, and what we want to create from this file by default
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

1. Load data from the [Portal Project](https://portal.weecology.org)
2. Process it into population time series
3. And make initial visualizations
</code></pre>

* Easy to read for humans
* Easy to convert into other things for computers

* Press `Render` to create `HTML` from the document
* Can also create `pdf` & Word versions of our files
* Change output to `pdf` or `docx`

* Switch back to html
* Click the gear icon and select `Preview in Viewer Pane`
* `Render`
* This shows the rendered page right in RStudio

* Markdown is common on lots of websites
* Used to create all of the exercises and lectures in this course

### Visual editor

* We can also view and interact with the markdown in a style similar to a word processor
* Click `Visual`
* Markdown is now rendered in the editor
* Can use the editor bar to make markdown changes
* UNBOLD: The Portal Project
* Click `Source`
* See that it is no longer bolded using **

### R chunks 

* Quarto allows you to include code to run in the document
* Click on `+C` button, which stands for "add code"
* Or in the visual editor type `/` and select `R Code Chunk`

<pre><code>
## Required Packages

```{r}
library(dplyr)
library(ggplot2)
library(gt)
library(readr)
```
</code></pre>

* Can run this code by clicking the green arrow
* Load the data and look at it

<pre><code>
## Data

```{r}
data <- read_csv("https://ndownloader.figshare.com/files/2292172")
data
```
</code></pre>

* If we run the code with the green arrow we'll get a nicely formatted table
* If we click the Render button the output will be included in the html web page

* You can run code inside your text, too:

```
The data includes `r length(unique(data$species_id))` species.
```

### Analysis Example

<pre><code>
## Analysis

Get the time-series of counts for all species.
          
```{r}
time_series <-
  data |>
  group_by(species_id, year) |>
  summarize(count = n()) |>
  filter(sum(count) > 200)
time_series
```
</code></pre>

### Including Graphs

* Graphs will be included as figures in the document

<pre><code>
## Plot the time-series.

```{r}
ggplot(time_series, aes(x = year, y = count)) +
  geom_line() +
  facet_wrap(vars(species_id), scales = "free_y")
```
</code></pre>

### Chunk options

* Each block of code is called a "chunk"
* Chunks have lots of useful options
* Can add them at the start of the chunk using `#| `, the option name, `:`, the option value
* `#| echo: false` let's you show the results of the code chunk without showing the code.
* ADD: `#| echo: false` to plot chunk
* `#| message: false` will remove messages returned by R
* ADD: `#| message: false` to package, data, and analysis chunks
* RENDER

* There are also chunk options to include figure legends and alt text
* ADD TO FIGURE CHUNK:

```
#| fig-cap: "Figure 1. Time-series of rodent population dynamics at Portal."
#| fig-alt: "Time-seris of 12 rodent species showing a range of dynamics from increases to decreases to variable, but not directionally changing, response"
```

### Tables

* We can also make nicely formated tables using the `gt()` function
* Let's say we need to know who many total individuals of each species were included in the analysis

<pre><code>
```{r}
time_series |>
  group_by(species_id) |>
  summarize(total_count = sum(count)) |>
  gt() |>
  cols_label(
      species_id = "Species",
      total_count = "Total Population"
      )
```
</code></pre>

* You can add a label and then cite the table/figure in the text

```r
#| label: tbl-total-count
#| tbl-cap: "Total population counts for each species in the study"
```

* You can then reference the table in the text using `@tbl-total-count`

```r
The population dynamics at the site varies by species (@tbl-total-count).
```

### Citations


* `Insert` -> `Citation` -> `From DOI` -> `10.1101/332783` -> `+` -> `Insert`
* Creates a `bibliography.bib` file with the citations
* This is called a bibtex file
* Can now cite papers using [@ernest2018]
* It will appear as an in-text citation and in a References section at the bottom of the document

### Other Output Formats

* Slides
* Websites
