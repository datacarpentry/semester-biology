---
layout: page
element: notes
title: Large Language Models
language: R
---

### Introduction

* Large language models are a form of machine learning, or AI, that can be used for generating text in response to written prompts
* Who's heard about ChatGPT and other similar models?
* One of the kinds of text these models can generate is code

* The very simplistic version of how these models work is that they look at a string of words and figure out what word is most likely to come next
* They learn the most likely next word by looking at millions of examples from the internet
* In other words they are an advanced form of autocomplete or a parrot

* Since there is lots of code written by software developers on the internet they are pretty good at generating code
* And since there are lots of lessons on how to learn to code on the internet they can also be good generating text that explains code

### Examples

* *Open ChatGPT*
* Let's prompt ChatGPT to solve something like we've been working on
* *Enter the following prompt*

> How do you calculate the sum of the vector numbers <- c(2.1, 2.7, 2.7, 3.2, 2.9, NA, 3.9, 2.1, 4.5, 2.6) in R?

* *ChatGPT will produce a code answer with a variable holding the sum*
* This looks like the right answer and it even saw the NA, handled it appropriately, and explained that
* Let's prompt ChatGPT for the result of this code

> What is the value of <variable_name>?

* *Copy the code into R and run it*
* *The result returned is currently wrong, but that could change*
* In this case the LLM is wrong
* It can't run code and it doesn't know how to do math, it just knows that when the word "sum" is used for a string of numbers that looks like roughly like this one that there tends to be a number that looks roughly like 24.7 that follows it
* So, LLMs can be powerful, but also wrong 

### Right answer wrong approach

* Because LLM aren't specifically designed for this course they may show you ways to do things that we aren't learning

* *Start a new Chat*
* *Type the following prompt*

> In the R programming language use code to print the sum of the following vector.
>
> numbers <- c(2.1, 2.7, 2.7, 3.2, 2.9, NA, 3.9, 2.1, 4.5, 2.6, 2.9, 3.1)

* Because of the small differences in the phrasing of the question (and the stochasticity of LLMs) we get a different answer
* It still works, but it's more complicated, and it's not the approach that we're learning

### Using LLMs for learning

* There are a variety of meaningful ethical concerns about using LLMs
    * The use a lot of energy to train and run and therefore put a lot of CO2 in the atmosphere
    * They use millions of peoples work without credit or payment, arguably in violation of copyright and licenses
    * And since they parrot what's on the internet they often lot of bias and bigotry
* That said, LLMs can be useful for learning and you are welcome to use them for this in this course
* Using them to directly answer the exercises won't help you learn, because humans need practice to learn
* That's the only reason we have exercises
* So what are useful ways to use them?
* You can prompt them to explain things you don't understand and they will parrot relevant advice from material on the web
* This can be easier, especially for folks learning to code, than trying to search for a specific site that has the answer
* You can also use them to help debug your code, which we'll talk about more when we talk about debugging

### Using LLMs for work

* Once you've finished the course you can use them to automate things you already know how to do
* But LLMs are parrots so you know enough so that you can check and make sure that the model produced a valid result
