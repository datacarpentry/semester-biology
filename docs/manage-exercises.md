---
layout: exercise
title: Help
subtitle: Adding and Modifying Exercises
---

- Create or modify a [markdown file](http://daringfireball.net/projects/markdown/basics) from the `exercises/` directory. Name the file according to its title, followed by the programming language, with `-` in the spaces (as in `Making-choices-1-R.md`).

- Use the following standard exercises YAML at the top of your exercise file to 
be sure the file is read correctly by [Jekyll](http://jekyllrb.com/). [[ EXTRA INFO: Each markdown file needs to start with some information and standard content that is stored in a way Jekyll uses to automate rendering of the website. The starting content, or 'Front Matter', is entered using something called YAML and provides information that Jekyll uses to organize and automate the website, like the title of the page, what language it applies to, and a list of accompanying files. ]]

```
---
layout: exercise
title: Name-of-exercise
subtitle: Exercise-topic-or-short-description
language: R-Python-or-SQL
---
```

- Anything markdown can go in an exercise file, but please use consistent formatting. We recommend the following guidelines:
   * No trailing white space
   * Wrap lines at 80 characters (unless it breaks URLs)
   * Use unclosed `#` symbols for headers, e.g. ```# Heading 1```
   * Use ordered lists only when introducing sequential tasks
   * For more, please see the website [Style Guide]({{ site.baseurl }}/docs/style-guide).

- Add, commit, and push the new file to GitHub to get the content added to the website. These steps are further described in [Course Customization Help]({{ site.baseurl }}/docs/course-customization).

- Access the exercise file on the web at the url based on where the file is 
located and what the file name is. So if you created a new exercise in the `exercises/` folder called `my_awesome_exercise.md` it would be located

   - locally at: `http://localhost:4000/exercises/my_awesome_exercise`

   - after pushing to GitHub at:
`https://yourusername.github.io/semester-biology/exercises/my_awesome_exercise`

- Add `output/` files for corresponding exercises in the `output/` directory with names that match the corresponding exercise with numerals following a `-` for multiple output files. For instance, the set of output files for 
   - `Making-choices-1-R.md` would be 
   - `Making-choices-1-R-1.png` and `Making-choices-1-R-2.txt`.