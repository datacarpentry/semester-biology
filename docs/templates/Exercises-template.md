---
layout: exercise
topic: Templates
title: Exercise Template
language: Access-Python-R-SQL
---

1. Determine the `topic`, `title`, and `language` from the [front matter](https://jekyllrb.com/docs/frontmatter/) of your new or modified exercise.
2. Name the file with the format `Topic-title-Language.md` in the `exercises/` directory such as `Templates-exercise-template-Python.md`. The file must start with an `UPPER` case letter.
3. Generate or repair [course linkages]({{ site.baseurl }}/docs/site/course-structure).
  - The `title` may be listed in `assignments/`
  - An output file or set of files can be stored in `solutions/` with
    matching `Topic-title-Language` format. The file retains its file 
    extension. Multiple files are numbered such as: 
    `Templates-exercise-template-Python-1.txt`, 
    `Templates-exercise-template-Python-2.jpg`, ...
  - Reference the exercise in a follow-up link: 
    ```[Title]({{ site.baseurl }}/exercises/Topic-title-Language)```
4. Be sure to [contribute]({{ site.baseurl l}}/docs/course/contributing) your new exercise to the [Data Carpentry Repository](https://github.com/datacarpentry/semester-biology). 