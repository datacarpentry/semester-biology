---
layout: exercise
topic: Help
title: Style Guide
---

### File Content

- All web content files are written in [Markdown](http://daringfireball.net/projects/markdown/basics) and start with [YAML front matter](https://jekyllrb.com/docs/frontmatter/). Any `.MD` file in the course can be modified for content using plain text in [Markdown](http://daringfireball.net/projects/markdown/basics), HTML, or [Liquid](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers). 
- File names and front matter must be revised carefully according to the [course structure]({{ site.baseurl }}/docs/site/course-structure) and [file templates]({{ site.baseurl }}/docs/). 
- [Add and modify files]({{ site.baseurl }}/docs/course/manage-files) from your local machine or online using [GitHub]({{ site.github.repo }}).

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

- Use appropriate code style guides [ [R](http://adv-r.had.co.nz/Style.html) \| [Python](https://www.python.org/dev/peps/pep-0008/) ] and [best practices](http://swcarpentry.github.io/r-novice-inflammation/06-best-practices-R.html).

- The code chunks have a shorter effective page width than the 80 characters 
afforded normal text. Reduce the length of code blocks to improve readability 
for students (*~60 characters*).