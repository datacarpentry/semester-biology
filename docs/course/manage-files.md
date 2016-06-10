---
layout: exercise
topic: Help
title: Manage Course Files
---

### File Locations and Formats

Core teaching materials are stored in the relevant folders including
`lectures/`, `materials/`, and `readings/`.

Class specific materials are stored in `assignments/`, `exercises/` and `solutions/`. Additional files are stored in `code/` and `data/`.

Most of the other folders and files support creating the course website using
[Jekyll](http://jekyllrb.com/).

Many of the file names and [front matter](https://jekyllrb.com/docs/frontmatter/) content values are coordinated across course materials. File names and front matter must be revised carefully according to the [course structure]({{ site.baseurl }}/docs/site/course-structure) and [file templates]({{ site.baseurl }}/docs/).

### Manage Files

- Create or modify a [Markdown file](http://daringfireball.net/projects/markdown/basics) in the `assignments/` directory.
 
- Use the appropriate [template]({{ site.baseurl }}/docs) to be sure the file content is formatted correctly for [Jekyll](http://jekyllrb.com/) rendering. Each file needs to start with standard [front matter](https://jekyllrb.com/docs/frontmatter/) content that Jekyll uses to automate rendering of the website. Use the [style guide]({{ site.baseurl }}/docs/course/style-guide) for formatting page content following the [front matter](https://jekyllrb.com/docs/frontmatter/).

- [Add, commit, and push](https://help.github.com/articles/create-a-repo/#commit-your-first-change) the new or modified file to GitHub to get the content added to the website.

### Preview changes locally using Jekyll

If you want to view your changes locally, before pushing them to the live
website, you'll need to setup [Jekyll](http://jekyllrb.com/) locally. GitHub 
provides a [good introduction on how to do this](https://help.github.com/articles/using-jekyll-as-a-static-site-generator-with-github-pages/).

If you have Jekyll properly installed, you can then run

`bundle exec jekyll serve`

from the command line and navigate to `http://localhost:4000/` in your browser 
to preview the current state of the website. Access a specific file on the web at the url based on where the file is located and what the file name is. 
So if you made changes to this file `manage-files.md` from the `docs/course/` folder, you could view them

   - locally at: `http://localhost:4000{{ site.baseurl }}/docs/course/manage-files`

   - after pushing to GitHub at: 
`https://yourusername.github.io{{ site.baseurl }}/docs/course/manage-files`