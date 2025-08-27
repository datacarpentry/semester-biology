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

* The very simplistic version of how these models work is that they look at a string of words and figure out what words are most likely to come next
* They learn this by looking at millions of examples from the internet

* Since there is lots of code written by software developers on the internet they are pretty good at generating code
* And since there are lots of lessons on how to learn to code on the internet they can also be good generating text that explains code

### Examples

* *Open ChatGPT*
* *Copy and paste an exercise from the assignment*
* *In most cases the result will be reasonable*

### Using LLMs

* There are a variety of meaningful ethical concerns about using LLMs
    * The use a lot of energy to train and run and therefore put a lot of CO2 in the atmosphere
    * They use millions of peoples work without credit or payment, arguably in violation of copyright and licenses
    * And since they parrot what's on the internet they often biased in all the ways content on the internet is biased
* Writing code with them when lacking the background to evaluate that code can also be dangerous
    * They are good at giving you an answer, even if it's the wrong one
    * Code that is wrong but runs is the scariest kind of code in science
* But they can be useful tools
* My lab uses these tools to support our software engineering
* So I have a reasonable amount experience using and evaluating them in complex data analysis & coding contexts
* My experience with the current models is that they can be useful tools, but are rarely complete solutions
* Useful for implementing things you already know how to do quickly - model generates an imperfect draft and you fix it
* Also useful for getting started with the specifics of how to do something new - if you already have a strong foundational understanding

### Using LLMs for learning

* LLMs can be useful for learning and you are allowed to use them for this in this course
* Using them to directly answer the exercises won't help you learn, because humans need practice to learn
* That's why we have exercises
* As a result using LLMs to solve exercises has been compared to [taking a forklift to the gym to lift weights](https://havn.blog/2025/03/01/on-the-need-for-friction.html)
* The goal of lifting weights is to get stronger, so the forklift doesn't help
* Likewise, the goal of our exercises is to learn the foundations of computing in R

* To put that somewhat more enjoyably here's quick short from Hero of Coding with Strangers
* (there is some swearing in this video, so if you're not comfortable with that you're welcome to step out for ~60 seconds)

<iframe width="674" height="1198" src="https://www.youtube.com/embed/OhaGNTiMXmU" title="Sora AI is Like Batman&#39;s Utility Belt" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

* I'm assuming that you're all here to learn, so I recommend listening to Hero and at least not using LLMs to directly answer the exercises
* We won't be policing LLM content in submissions
* But the exercises do need to be answered using the approaches we learned in class and often LLMs will use a different approach

* So what are useful ways to use them?
* You can prompt them to explain things you don't understand and they will parrot relevant advice from material on the web
* This can be easier, especially for folks learning to code, than trying to search for a specific site that has the answer
* You can also use them to help debug your code, which we'll talk about more when we talk about debugging

### Using LLMs for work

* Once you've finished the course you can use them to automate things you already know how to do
* In our experience in my lab these models typically do about 90% of each simple task correctly
* That means that the end result rarely works, but if you know how to fix what is wrong it can still be a time saver
* But you have to know enough to fix the things that don't work and to check and make sure that the code is actually doing what you want
* And sometimes they're really wrong
* The other day I asked GitHub copilot for help with a complex version control command and it gave me a command that would have unrecoverably deleted all of the work I'd done in the last hour
