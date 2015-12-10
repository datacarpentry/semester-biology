---
layout: page
title: Help
subtitle: Add, Modify, and Manage Exercises
---

## Add or modify a new exercise

- Create or modify a [markdown file](http://daringfireball.net/projects/markdown/basics) from the `exercises/` directory. Name the file according to its title, followed by the programming language, with `-` in the spaces.
- Use the following standard exercises page template to be sure the file is read correctly by [Jekyll](http://jekyllrb.com/). Items that we expect you to input are noted in _italics_. [[ EXTRA INFO: Each markdown file needs to start with some information and standard content that is stored in a way Jekyll uses to automate rendering of the website. The starting content, or 'Front Matter', is entered using something called YAML and provides information that Jekyll uses to organize and automate the website, like the title of the page, what language it applies to, and a list of accompanying files. ]]

```
---
layout: exercise
title: Combining Basics
subtitle: Shrub Volume Pt 5
language: R
---

_page content_
```

- To ensure a consistent formatting of the lessons, we recommend the following
guidelines:
   * No trailing white space
   * Wrap lines at 80 characters (unless it breaks URLs)
   * Use unclosed `#` symbols for headers, e.g. `# Heading 1`
   * Use ordered lists only when introducing sequential tasks
   * Please, see the website [Style Guide]({{ site.baseurl }}/documents/course-customization) for more details

- Add, commit, and push the new file to GitHub to get the content added to the website. These steps are further described in [Course Customization Help]({{ site.baseurl }}/documents/course-customization).


## Accessing an exercise file on the web

The page should be available at a url based on where the file is located
and what the file name is. So if you created a new exercise in the `exercises/` folder called `my_awesome_exercise.md` it would be located

locally at: `http://localhost:4000/exercises/my_awesome_exercise`

after pushing to GitHub at:
`https://yourusername.github.io/semester-biology/exercises/my_awesome_exercise`
