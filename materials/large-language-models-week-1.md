---
layout: page
element: notes
title: Large Language Models
language: R
---

### Initial Discussion

* Who's heard about ChatGPT?
* Claude?
* Gemini?
* Who uses one of these at least once a week?
* What about AI Coding Assistants - like Claude Code, Codex, GitHub Copilot?
* Who uses one of these regularly?
* What do you think about them?

### Introduction

* These are all large language models
* Predict the new token (or word) based on preceeding words
* They work by being trained on the entire internet
* Since there is lots of code written by software developers on the internet they are good at generating code
* And since there are lots of lessons on how to learn to code on the internet they can also be good at generating text that explains code

* There are a variety of meaningful ethical concerns about using LLMs
* Environmental, Intellectual Property, and Labor are the big 3
* Writing code with them when lacking the background to evaluate that code can also be dangerous
* The worst code in science is code that is wrong, but runs, and models are good at producing this kind of code

* But they can be useful
* Starting in late 2025 frontier models became very good 
* My lab uses these tools to support our software engineering

### Using LLMs for learning

* Growing evidence that LLM usage can have significant negative effects on learning
* We learn through a combination of repetition and struggling with material
* If we take that away we don't learn
* So, both in class and more broadly if we need to think about when this use is helpful vs harmful on a personal level

* LLMs can be useful for learning and you are allowed to use them for this purpose
* Using them to directly answer the exercises won't help you learn, because humans need practice to learn
* That's why we have exercises
* Using LLMs to solve exercises has been compared to [taking a forklift to the gym to lift weights](https://havn.blog/2025/03/01/on-the-need-for-friction.html)
* The goal of lifting weights is to get stronger, so having the forklift move the weights for you doesn't help
* In this class practicing the concepts and the specific implementation goes hand in hand
* To put that somewhat more enjoyably here's quick short from Hero of Coding with Strangers

<iframe width="674" height="1198" src="https://www.youtube.com/embed/OhaGNTiMXmU" title="Sora AI is Like Batman&#39;s Utility Belt" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

* There is also a growing body of scholarship backing this idea
* I'm here to teach and you're (hopefully) all here to learn, so I ask that you listen to Hero and not use LLMs to directly answer the exercises

* So what are useful ways to use them?
* You can prompt them to explain things you don't understand 
* If we're in class I definitely recommend asking me or the TA, but if it's midnight and you're stuck then they are certainly useful
* You can also use them to help debug your code, which we'll talk about more once we start coding
* But trying to fix bugs yourself is also important to learning, so start by working the problem yourself and only ask a model for help at the point where you would ask a one of us for help during class

### Using LLMs at UF

* Due to security and privacy risks and Florida and federal law the only approved way to use LLMs at UF is through NaviGator
* It also has the nice benefit of being free
* The chat-based interface is available at:
* *Go to* https://chat.ai.it.ufl.edu
* *Sign in*
* Through this system you have access to a bunch of different models
* Hover over them to see what they are approved for
* For this class any of these models is fine
* For research, it depending on your work you might be restricted to a subset of them
* I tend to use Claude, but any of the newer Claude, Gemini, or OpenAI/GPT models will be sufficient for anything we're doing

### Demo

* Copy-paste Repeating Things 2 Challenge
* Result is likely in Python
* Is this what we want?
* *Ask to rewrite in R (using loops and conditionals)*
* *Run the resulting code*
* What do you think went wrong here?
* Answer may be wrong due to misunderstanding data structure
* *Download files*
* *Open in text editor*
* *Does this match our idea of tidy data?*
* Some federal data providers include metadata at the top of the csv
* There are ways to handle this, but only if you know what the data looks like, which the LLM doesn't
* We could tell model to look at data by using web search
* But we'd run into something called a context limit because the data file is too large
* So show it the top of the file
* *Copy first 40 lines and have model update code*
* *Rerun*
* Result may still be wrong and model may assume space delimited due to copy-paste

### What does this demo show us?

* Chat-only interfaces can be limited
* Real AI coding assistant like Claude Code or Codex running locally will easily solve this problem
* We'll talk about them later in the semester

* Without enough context the LLM may do things we don't want
* Use Python or packages in R we aren't familiar with
* Just give us the answer when we want help learning

### Learning to leverage LLMs

* Last year the models still weren't that great
* So we have a shorter version of this discussion at the start of class
* And then didn't explore AI until briefly at the end of the semester
* But since then there has been a step change in these models for writing code

* Do you want to spend a short amount of time each week talking about how to effectively use AI for supporting your coding? 
* *Respond contingent on answer, notes below focused on if the answer is Yes*

* So, this year we're going try to engage with this a little bit each week
* Doing so will be optional
* I'm still figuring out what this looks like
* In fact everyone who teaches coding is figuring what this looks like

* Generally we're going to stick to focusing on concepts first
* Understanding the basic idea of how computational approaches work remains central to coding and working as a scientist
* We're going to learn how to implement things ourselves in R
* This helps us learn how to think computationally
* And LLM output for science is typically code and you'll be responsible for the output of that code
* Which means you need to understand it
* What I'm going to try to add (briefly) at the end of each week is some introduction to how to engage with LLMs for coding effectively

* This is going to very much be an experiment
* So feedback on what is working or not working for you will be very helpful
