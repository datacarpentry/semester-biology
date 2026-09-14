---
layout: page
element: notes
title: AI - Context via Files and Websites
language: R
time: 1
---

## Importance of context

- Review last time
- Provided context through prompts

## Other ways to provide context

- Can give models access to files or websites
- *Demo*

## Too much context

- But it's possible to have too much context
- *Demo adding big file*
- This happens because models have limited "attention"
- There are both maximum limits on the number of tokens
- But even before you reach them you can enter the "dumb zone"
- Also usage priced based on the number of tokens
- So don't want to pay for 200,000 tokens when 200 will do
- Provide files that are just the first few rows of a data file
- Generate this in R using `head(df) |> write_csv(df, "df.csv")`
