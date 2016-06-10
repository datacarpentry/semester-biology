---
layout: exercise
topic: Help
title: Strip Course Content for Site Template
---

### From most up-to-date course version on [GitHub]({{ site.github.repo }})...

- Familiarize yourself with the [site]({{ site.baseurl }}/docs/site/site-structure) and [course]({{ site.baseurl }}/docs/site/course-structure) structure.
  - `_includes/`, `_layouts/`, `nav/`, and `public` contain essential site 
software for [Jekyll](https://jekyllrb.com/) to render the website from `.HTML` 
and `.MD` files. These files can be left AS IS for a 'computer programming' 
template. Template developers may toggle object names for `element:` and 
`language:` used to organize course materials.
- Follow the [course customization]({{ site.baseurl }}/docs/course/course-customization) guide to identify the files and values that need to be stripped 
of content or replaced with a descriptive placeholder. 
- For [`assignments/`, `code/`, `data/`, `exercises/`, `lectures/`, `materials/`, `readings/`]:
  - Remove all files EXCEPT `index.md` from the directory
  - Move `templates/` file to directory
  - Revise `index.md` to template
- For `solutions/`:
  - Remove all files EXCEPT `Exercises-template.txt`
- For [`README.md`, `START-for-self-guided-students.md`]:
  - Revise for general template language.

### OR, `pull` a well out-dated, but largely generated, template...

```
git checkout -b make-template gh-pages
git pull https://github.com/brymz/datacarp-semester-biology.git template
```
- [GitHub Pull Request](https://github.com/datacarpentry/semester-biology/pull/408)
