---
layout: page
element: notes
title: Knitr
language: R
---

> Download [`knitr-examp.Rmd`]({{ site.baseurl }}/materials/knitr-examp.Rmd).

### Literate programming

* Combine text, code, figures, tables, etc.
* Write papers without having to remember to swap figures
* Automatically generate reports


### Getting started

* File -> New File -> R Markdown
    * Enter a title and author(s).
    * Choose 'Default Output Format' as `HTML`.
* Generates a basic stub of a `.Rmd` document. 
* Press `Knit to HTML` to create an `HTML` from it
    * 1st time may ask you to install some packages
    * `install.packages("rmarkdown")` in console for permanence
* Runs the code in the code chunks and prints their output along with the
  markdown formatted text
* Can also create `PDF` & Word versions of our files
    * `PDF` Requires `pandoc` and `TeX` installation
    * Use the `Knit` dropdown or change `output: pdf_document` 


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

### R chunks 

        ```{r}
        ```

* Code that you write inside them gets executed, then the results are shown
below.
* Chunks have lots of useful options
  * Options are described at http://yihui.name/knitr/options/
  * Options will be listed in RStudio if you press tab inside
    the `{r}` brackets at the top of the chunk
    
* You can run code inside your text too:
    * `r cos(pi)` turns into `-1` when you press the "knit" button.

### Example

> Demo
>
> * [`knitr-examp.Rmd`]({{ site.baseurl }}/materials/knitr-examp.Rmd) in RStudio
> or, 
> * [direct link](https://raw.githubusercontent.com/datacarpentry/semester-biology/gh-pages/materials/knitr-examp.Rmd).

* Talking points
    * front matter
    * chunks
    * chunk options
        * `message=FALSE` to first and last chunk
        * `echo=FALSE` to last chunk
    * `library(scales)` & `scale_x_continuous(breaks=pretty_breaks(n=2))`

