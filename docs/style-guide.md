---
layout: page
title: Help
subtitle: Style Guide
---

### Page Layout

- Do not leave extra whitespace, unless required to properly format the markdown rendering. Include one blank line following the YAML front matter.

- Wrap lines at 80 characters, but don't break urls or markdown rendering.


### General Syntax 

- Use leading `#` for headers (`# Heading 1`). Most headers in the website content will be `###` or `####`.

- Use `-` for unordered lists. Only use ordered lists if instructions, items, or tasks are sequential in execution.

- Encase any hint, note, or () statement with \* to italicize text (*like this*).


### Including Code Chunks

- Use ` to denote code and objects according to their structure:
   - `packages`, `objects` and `lists`
   - `functions()`
   - `directories/`
   - `data-and-output-files.txt`
   - `"characters"`

- Code chunks that take up a whole line should be placed in a code block using ```.

- Use appropriate code style guides [ [R](http://adv-r.had.co.nz/Style.html) | [Python](https://www.python.org/dev/peps/pep-0008/) ] and [best practices](http://swcarpentry.github.io/r-novice-inflammation/06-best-practices-R.html).

- The code chunks have a shorter effective page width than the 80 characters 
afforded normal text. Reduce the length of code blocks to improve readability 
for students (*~60 characters*).