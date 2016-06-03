# Prof. Hyde: course website template

This is a [forkable](https://help.github.com/articles/fork-a-repo/) template for a website of teaching materials for a 
university style and/or self-guided course. 

[Helpful information](http://www.datacarpentry.org/semester-biology/docs/) 
is available regarding the structure and function of the course template and website materials, as well as customization and potential delivery of the course.

The course template is designed to work primarily with a flipped classroom, 
where students read and view instructional materials before coming to class and 
then spending the bulk of class time working on exercises with the teacher 
answering questions and demoing the concepts.

We encourage collaborative development of the template and the original general programming course ([[original course website](http://www.datacarpentry.org/semester-biology/) | [original course on git](https://github.com/datacarpentry/semester-biology)].  
We welcome contributions to all aspects of the course/site and are especially 
seeking exercises and assignments for a range of disciplines.

## How is the template organized?

Core teaching materials are stored in `exercises/`, `lectures/`, and 
`materials/`.

Class specific materials are stored in the `syllabus`, `schedule` and `assignments/`.

Most of the other folders and files support creating the course website using
[Jekyll](http://jekyllrb.com/).


## How to contribute

We use standard [GitHub flow](https://guides.github.com/introduction/flow/), so
fork the repository, add or change material, and submit a pull request.

The goal of making this template forkable is to facilitate collaboration on
developing this kind of material for university courses. The central component
of a flipped computing course is the exercises, so one of the primary forms of
contribution will be adding exercises to the pool of exercises. Individual
instructors can then select from a rich pool of exercises the ones that fit the
topics, languages, and scientific domains that best fit the material they want
to cover in their course.


## Using Jekyll to build your own course website

### Simple setup

The website is setup to be easy to run automatically through GitHub:

1. [Fork](https://github.com/datacarpentry/semester-biology#fork-destination-box)
   or [import](https://import.github.com/) the repository
   * In a few minutes you should be able to see the site at:
     `https://yourusername.github.io/semester-biology/`
2. Edit any of the markdown (.md) files
3. Commit and push the changes
   * The changes should now be reflected on the website
4. If you want to use a custom domain name instead of `github.io`, follow
   [GitHub's instructions for setting up a custom domain](https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages/).

If you have any problems please
[let us know](https://github.com/datacarpentry/semester-biology/issues/new) and
we'll be happy to help.

### Previewing changes locally

If you want to view your changes locally, before pushing them to the live
website, you'll need to setup Jekyll locally. GitHub provides a [good
introduction on how to do this](https://help.github.com/articles/using-jekyll-with-pages/).

If you have Jekyll properly installed, you can then run

`bundle exec jekyll serve --baseurl ''`

from the command line and navigate to http://localhost:4000/ in your browser to
preview the current state of the website.


## Creating new pages

To add new exercises, lecture notes, and other course materials, simply create a
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
`https://yourusername.github.io/semester-biology/exercises/my_awesome_exercise`

Example course material markdown files are included in their appropriate directory.


## Acknowledgements

Development of this template is funded by [the Gordon and Betty Moore
Foundation's Data-Driven Discovery
Initiative](http://www.moore.org/programs/science/data-driven-discovery) through
[Grant GBMF4563](http://www.moore.org/grants/list/GBMF4563) to Ethan White and
the [National Science Foundation](http://nsf.gov/) as part of a [CAREER award to
Ethan White](http://nsf.gov/awardsearch/showAward.do?AwardNumber=0953694).
