---
layout: page
element: notes
title: AI Assistance and Assistants for Coding
language: R
time: 1
---

> Have students install Positron before class

### Problems with LLMs

- There are a variety of meaningful ethical concerns about using LLMs
- The use a lot of energy to train and run and therefore put a lot of CO2 in the atmosphere
- They use millions of peoples work without credit or payment, arguably in violation of copyright and licenses
- Writing code with them when lacking the background to evaluate that code can also be dangerous
  - They are good at giving you an answer, even if it's the wrong one & code that is wrong but runs is the scariest kind of code in science
  - Bad code can accidentally destroy your work
  - Malicious hackers are finding ways to get models to generate code that lead to compromised computers
- Cost
  - Start out with generous free plans
  - Most companies already increasing prices (and still losing money)
  - Expect costs to continue to rise
- Privacy/confidentiality
- Reduced learning making it difficult to go from beginner to expert
- But they can be useful tools and we'll spend today exploring how

### What are you doing now?

- First - How are you using LLMs for coding now?

### Chat

- UF provides access to a number of different model's chat systems for free
- UF Navigator
- Navigate to: https://chat.ai.it.ufl.edu/
- Sign in

- So, many of you have already used chat interfaces
- "How do you drop NA's from a table in R"
- Copy the resulting code into RStudio
- Give it a quick read for anything bad
- Run it

#### Improving output from LLMs

- Provide details (value of knowing things)
- Ask model to write code not return results
- Provide model with context
  - Better prompts
  - Attaching files
  - Including relevant urls
- If the resulting code doesn't run, tell model what happened and ask for fixes
- This set of practices is so common they are now integrated into many IDEs

### Assistants

- "AI Coding Assistants" provide a combination of chat, autocomplete, and local code execution

#### Activating the assistant in Positron

- Click on ⚙️
- Choose `Settings`
- Type "Assistant"
- Scroll down and select `Enable`
- Restart Positron
- `Welcome` -> `New Folder` -> `R Project`

#### Integrated Chat

- Click on the 🤖 (bottom of sidebar)
- `Add a Chat Provider` -> `GitHub Copilot` -> `Sign in`
- On `Authorize your device` page paste code -> `Continue`
- `Authorize GitHub Copilot Plugin` -> `Close`
- Return to Positron
- _Type_ "How do I remove rows with na using dplyr"
- _Show at top of code block_
- From the top of code blocks you can
  - Run code in the console
  - Move code to the editor either in the current file or a new one
  - Copy it
- Can then keep or undo changes
- More useful if we give it context

```R
library(dplyr)
library(readr)

surveys <- read_csv("https://ndownloader.figshare.com/files/2292172")
```

- Save file
- *Show that file is in the context in chat*
- "Add a dplyr pipeline that removes rows with NA in the weight column from the surveys table"
- We could copy this code over, or we can change the settings for the assistant to let it edit our files
- Switch from "Ask" to "Edit"
- Rerun query
- Read and accept the edits

#### Inline assistant

- In the text editor `Ctrl-i`
 - "Only keep the year, month, day, and weight columns"
 - Accept changes

#### Autocomplete

- Hit enter after the last line
- Look at the autocomplete
- Interpret output
- We typically don't want an LLM guessing at what analysis we want
- Start it with a comment

```R
# calculate the average weight and number of individuals in each year in each month
```

#### Debugging

- *Let autocomplete do as much of this as possible*

```R
# Write a dplyr pipeline that returns only species starting with the letter "D" and
# where weights are greater than 46 then calculate the average weight of each species
```

- Run the pipeline and debug. If the model doesn't error introduce an error
- Highlight code and select `Review`
- There will soon be Fix and Explain options that pop up in the error message itself to further simplify this process

#### Vibe coding & Agent-based approaches

- Who's heard of vibe coding before?
- Instead of writing code yourself with assitance from an LLM just have the LLM write a full first draft
- Provide feedback to the LLM to make improvements to the code
- Anyone have experience with this yet?

- Change to `Agent` model
- This will allow the model to actually run code for you
- By default it will write the code, show it to you, and ask you if you want to run it
- Be careful, I relatively recently asked a model to perform a git operation I didn't remember how to do and the resulting code would have deleted by work from the last hour

- "Using R create species distribution models for Great Egrets, White Ibis, and Roseatte Spoonbills. Use these models to make predictions for the distribution of those species in 26 years. Create a website displaying the current model predictions and the future predictions."
- Explore the code, emphasize need to read it
- "Download the relevant data from gbif, update the code to use that data, and check that it works"
