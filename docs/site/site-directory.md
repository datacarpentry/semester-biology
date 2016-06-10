---
layout: exercise
topic: Help
title: Site Directory
---

Marked (`#`) files and directories are [course customization]({{ site.baseurl }}/docs/course/course-customization) targets.

```
.
├── _config.yml                # Modify Setup values -> `site.vars`
├── 404.html                   | Page not found destination
├── index.html                 # Modify course description
├── computer-setup.md          # Download and install software
├── LICENSE.md                 | CC BY and MIT
├── README.md                  | GitHub facing Site Help
├── schedule.md                # Modify assignments: list
├── START-for-...-students.md  | Self guided students guide
├── syllabus.md                # Modify course details and policy
├── ...                        | Support files for Jekyll/GitHub Pages
|                              |
├── _includes                  | HTML formatting blocks
|   ├── assignment.html        |   Builds exercise list for assignment
|   ├── assignments.html       |   Builds assignment schedule table
|   ├── head.html              |   Starting material for all pages
|   ├── reading.html           |   Adds reading material to assignment
|   └── sidebar.html           |   Builds navigation panel
├── _layouts                   | HTML page formatting
|   ├── exercise.html          |
|   ├── lecture.html           |
|   ├── page.html              | 
|   └── ...                    |
├── _site                      | Jekyll builds HTML for all site pages
|                              | Course Materials
├── about                      #   Motivation and support documents
├── assignments                |   Assignments documents
|   ├── language-descr.md      |     lower case file names
|   └── ...                    |
├── code                       |   Code files used in exercises
├── data                       |   Data files used in exercises
├── docs                       |   Course & site help docs; Templates
├── exercises                  |   Exercise documents
|   ├── Topic-title-Language.md|     UPPER first letter of file name 
|   └── ...                    |     File name formatted from YAML 
├── lectures                   |   Lecture documents
|   ├── language-descr.md      |     File name matches assignment
|   └── ...                    |
├── materials                  |   Lecture materials documents
|   ├── language-descr.md      |     Unmanaged descriptive file name 
|   └── ...                    |
├── nav                        | Site navigation pages
├── public                     |
|   ├── css                    | Style sheet for Hyde site theme
|   └── favicon.ico            | Browser tab icon file 
|                              | Course Materials (Cont.)
├── readings                   |   Reading materials
|   ├── Language-descr.md      |     File name matches assignment
|   └── ...                    |
└── solutions                  |   Solutions documents
    ├── Topic-tit...guage-1.txt|     File name matches exercise
    ├── Topic-tit...guage-2.jpg|     Number if multiple; any .ext
    └── ...                    |
```