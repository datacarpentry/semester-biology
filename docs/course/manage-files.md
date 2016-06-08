---
layout: exercise
topic: Help
title: Manage Course Files
---

### File Locations and Formats

Core teaching materials are stored in the relevant folders including
`lectures/`, `materials/`, and `readings/`.

Class specific materials are stored in `assignments/`, `exercises/` and `solutions/`. Additional files are stored in `data/` and `code/`.

Most of the other folders and files support creating the course website using
[Jekyll](http://jekyllrb.com/).

Many of the file names and [front matter](https://jekyllrb.com/docs/frontmatter/) content values are coordinated across course materials. File names and front matter must be revised carefully according to the [site structure]({{ site.baseurl }}/docs/site/site-structure) and [file templates]({{ site.baseurl }}/docs/).

### Manage Files

- Create or modify a [Markdown file](http://daringfireball.net/projects/markdown/basics) from the `assignments/` directory.
 
- Use the appropriate [template]({{ site.baseurl }}/docs) to be sure the file content is formatted correctly for [Jekyll](http://jekyllrb.com/) rendering. Each file needs to start with standard [front matter](https://jekyllrb.com/docs/frontmatter/) content that [Jekyll](http://jekyllrb.com/) uses to automate rendering of the website. Use the [style guide]({{ site.baseurl }}/docs/course/style-guide) for formatting page content following the [front matter](https://jekyllrb.com/docs/frontmatter/).

- Add, commit, and push the new or modified file to GitHub to get the content added to the website. These steps are further described in [Course Customization Help]({{ site.baseurl }}/docs/course-customization).

### View Rendered Site Pages

- Access the assignment file on the web at the url based on where the file is 
located and what the file name is. So if you created a new assignment in the 
`assignments/` folder called `my_awesome_assignment.md` it would be located

   - locally at: `http://localhost:4000/assignments/my_awesome_assignment`

   - after pushing to GitHub at: 
`https://yourusername.github.io/semester-biology/assignments/my_awesome_assignment`