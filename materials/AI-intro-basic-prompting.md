---
layout: page
element: notes
title: AI - Introduction and Basic Prompting
language: R
time: 1
---

## Understand the concepts

- Working effectively with AI requires that you understanding the concepts
- But it reduces the need for remembering specific syntax
- E.g., It's crucial to understand the idea of filtering the data, what it does, and how `and` and `or` work
- But it matters less if you quickly remember that you create an `or` condition using the `|`

## Be able to read the code

- As scientists we are responsible for making sure our code reflects the analysis we think we are doing
- The code we produce is our reproducible documenation of what we've done
- We should be able to look at the code to determine if this is true
- We'll talk about other ways of checking that it is true later in the semester

## Should I use AI for this?

- Ask the meta question - given my goals how useful is using AI for this task?
- Do I want to learn this or not?
- Is the process of implementing part of my thinking (e.g. writing)?
- Is it critical that this is right/that I understand the details or not?
- Would I enjoy doing this more myself?
- Does my brain need a break from executive function?
- Is it quicker, easier, cheaper to do it directly?

## Providing context

- Models need "context"
- Details of what you want done, how you want it done, and information needed to do it
- The most basic form of context is the "prompt"
- The thing that you ask the model to do
- Good prompts provide details
- For programming include language and any specific tools you want to use or not use
- Since we want to be able to understand the code that is generated tell the model to use the things you're familiar with
- R, dplyr

- Initial prompt (w/o data info):

> Using R and dplyr produce code that will take my data table, select the species, date, and weight columns, filter for weights >50 g, and remove any rows with null weights, add a new column showing weight in kg, and sort the data by weight in descending order.

- Did we cover how this filter statement works?
- No, we learned `drop_na()`, why didn't the model use it?
- Didn't specify we are also using tidyr
- Add that context now (or just include it from the start)

> Use drop_na from tidyr instead of !is.na

> Use base R pipes

- The model also needs information about the data you are working with
- Data format as context
- Can attach files
- But often data files are very large and can fill up the context window
- Often more useful to provide the top few rows of the data file
- Either as an attached file or by pasting into the prompt
- *Copy the prompt, add tidyr & base R pipes if needed*
- *Open surveys.csv in RStudio and copy-past the first few lines*

- Modified prompt (w/data info):

> Using R and dplyr and tidyr produce code that will take my data table, select the species, date, and weight columns, filter for weights >50 g, and remove any rows with null weights, add a new column showing weight in kg, and sort the data by weight in descending order.

> The data is stored in a csv file named surveys.csv and the top few rows of that file are:

> record_id,month,day,year,plot_id,species_id,sex,hindfoot_length,weight
> 1,7,16,1977,2,NL,M,32,
> 2,7,16,1977,3,NL,M,33,
> 3,7,16,1977,2,DM,F,37,
> 4,7,16,1977,7,DM,M,36,
