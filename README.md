# Introducing Agroecology - Extension Training Materials

This is a [forkable](https://help.github.com/articles/fork-a-repo/) set of teaching materials for teaching practitioners the basics of agroecology through
the introduction of foundational concepts and interactive learning activities.

The initial materials are presented primarily for a 1.5 day in-service training
sponsored by UF/IFAS Extension, though the materials should also be organized
for self-guided learning. 

[Helpful information](http://trec-agroecology.github.io/introducing-agroecology/docs/) 
is available regarding the structure and function of the course and website
materials for customized development and delivery of the course. We recognize 
the original development of this website format by @ethanwhite, @brymz, and others.


## Where is everything

Core teaching materials are stored in `exercises/`, `lectures/`, and 
`materials/`.

Class specific materials are stored in the `syllabus`, `schedule` and `assignments/`.

Most of the other folders and files support creating the course website using
[Jekyll](http://jekyllrb.com/).


## Using Jekyll to build your own course website

### Simple setup

The website is setup to be easy to run automatically through GitHub:

1. [Fork](https://github.com/TREC-Agroecology/introducing-agroecology#fork-destination-box)
   or [import](https://import.github.com/) the repository to 
   `https://github.com/yourusername/introducing-agroecology`.
2. Update `# Setup` information in `_config.yml` in the main directory for
   proper site rendering.
   * You must `push` this change to your repository to build and browse your 
     forked version.
   * In a few minutes you should be able to see the site at:
     `https://yourusername.github.io/introducing-agroecology/`
3. Edit any of the markdown (.md) files
4. Commit and push the changes
   * The changes should now be reflected on the website
5. If you want to use a custom domain name instead of `github.io`, follow
   [GitHub's instructions for setting up a custom domain](https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages/).

If you have any problems please
[let us know](https://github.com/TREC-Agroecology/introducing-agroecology/issues/new)
and we'll be happy to help.

### Previewing changes locally

If you want to view your changes locally, before pushing them to the live
website, you'll need to setup Jekyll locally. GitHub provides a [good
introduction on how to do this](https://help.github.com/articles/using-jekyll-with-pages/).

If you have Jekyll properly installed, you can then run

`bundle exec jekyll serve --baseurl ''`

from the command line and navigate to http://localhost:4000/ in your browser to
preview the current state of the website.


## Creating new pages

If you want to add new exercises, lecture notes, etc. you do this by creating a
[markdown file](http://daringfireball.net/projects/markdown/basics) in the
appropriate directory. Each markdown file needs to start with some information
that tells Jekyll what the page is. This is done using something called YAML,
and the standard YAML for a new exercise would look like this:

```
---
layout: exercise
topic: Topic group of exercise
title: Name of exercise
language: [R, Python, SQL]
---
```

This is placed at the very beginning of the markdown file and provides
information on what kind of content it is (e.g., exercise, page, etc.),
the title of the page, and what language it applies to.

The page should then be available at a url based on where the file is located
and what the file name is. So if you created a new exercise in the `exercises/`
folder called `my_awesome_exercise.md` it would be located at:

Locally: `http://localhost:4000/exercises/my_awesome_exercise`

After pushing to GitHub:
`https://yourusername.github.io/introducing-agroecology/exercises/my_awesome_exercise`


## Acknowledgements

Development of this material is funded by [UF/IFAS Extension](http://sfyl.ifas.ufl.edu/)
through IST #31557, “What is Agroecology and how is it relevant to your 
Extension program?” and Hatch Project FLA-TRC-005661.
