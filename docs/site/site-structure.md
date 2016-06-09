---
layout: exercise
topic: Help
title: Site Structure
---
```
.
├── _config.yml               # Modify Setup values -> \{\{ site.vars \}\}
├── _includes                 # HTML formatting blocks
|   ├── assignment.html       #   Builds exercise list for assignments
|   ├── assignments.html      #   Builds assignment schedule table
|   ├── head.html             #   Starting material for all pages
|   ├── reading.html          #   Adds reading material to assignments
|   └── sidebar.html          #   Builds navigation panel
├── _layouts                  # HTML page formatting
|   ├── exercise.html         #
|   ├── lecture.html          #
|   ├── page.html             # 
|   └── ...                   #
├── _site                     # Jekyll builds HTML for all site pages
├── about                     # 
├── assignments
|   ├── language-short-description.md
|   └── ...
├── code
├── data
├── docs
├── exercises
|   ├── Topic-title-language.md
|   └── ...
├── lectures
|   ├── language-short-description.md
|   └── ...
├── materials
|   ├── language-short-description.md
|   └── ...
├── nav
├── public
|   ├── css
|   └── favicon.ico
├── readings
|   ├── Language-short-description.md
|   └── ...
├── solutions
|   ├── Topic-title-language-1.txt
|   ├── Topic-title-language-2.jpg
|   └── ...
├── 404.html
├── index.html
├── LICENSE.md
├── README.md
├── schedule.md
├── START-for-self-guided-students.md
├── syllabus.md
└── ...

```