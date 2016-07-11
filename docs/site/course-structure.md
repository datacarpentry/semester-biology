---
layout: exercise
topic: Help
title: Course Structure
---

### Custom Information

- `_config.yml`: Customize set up information for use as [`site.variables`](https://jekyllrb.com/docs/variables/)
- `index.html`: Course description and site navigation
- `about/`: `acknowledgements.md`, `audience.md`, and `why-.` files

### Initialization Materials

#### Self-Guided
- `START-for-self-guided-students.md`: Anyone should be able to start from here

#### Course / Workshop
- `computer-setup.md`: List preparations for prerequisite knowledge & technology 
- `syllabus.md`: Course details and policy. 

### Layout and Linkages
 
```
     START-for-self-guided-students.md      syllabus.md 
                   \____________________________/
                                  |  
                             schedule.md
                                  |
           _______________________|_____________________
          /                       |                     \
      readings/               lectures/            assignments/
```
 
- `schedule.md` generates links for a list of `assignments:` for each of the major course `element:` `reading`, `lecture`, `assignments`    
- These `element:` must share a `title:` that is inserted into the 
`assignments:` list and `language:`  
- `element:` may share a common file name, `language-short-description.md`. 
- `assignments/` MUST have a `lower` case file name. 
- `readings/` have an `UPPER` first letter of the file name, arbitrarily.

``` 
    readings/            lectures/             assignments/
---                  ---                  ---
layout: page         layout: page         layout: page
element: reading     element: lecture     element: assignment
title: Hello World   title: Hello World   title: Hello World 
language: Foo        language: Foo        language: Foo
---                  ---                  exercises: ['Ba Ram', 'Ewe']
                                          ---
```

```
    lectures/     -->     materials/
                     ---
                     layout: page
                     element: notes
                     title: Hello Foos
                     language: Foo
                     --- 
```

- `lectures/` use links to organize `materials/`. 
  - `[link text]({{ site.baseurl }}/materials/file-name)` 
  - *NB: no* `.MD` *after* `file-name`

```
                             assignments/
                    ______________|_____________
                   /                            \
               readings/                     exercises/
                                            _____|_____  
                                           /     |     \
                                     solutions/ code/ data/

```
- `assignments/` organize `exercises/` with the `exercise:` list of `exercises/` `title:`

```
---
layout: exercise
topic: Practice
title: Ba Ram
language: Foo
---
```

- `exercises/` file names share similar values to `exercises/` YAML in the form:
`Topic-title-Language.md`. 
  - From the above YAML: `Practice-ba-ram-Foo.md`
- `exercises/` file names MUST start with an `UPPER` first letter.
- `solutions`/ file names MUST match the `exercises/` file name and can use any extension. For example: `Practice-ba-ram-Foo.txt`
- Multiple `solutions/` files can be numbered following the `exercises/` file name and before the file extension with a `-`.
  - `Practice-ba-ram-Foo-1.txt`, 
  - `Practice-ba-ram-Foo-2.jpg`, ...
- `code/` and `data/` files can be linked to exercises
  - `[Code file]({{ site.baseurl }}/code/code-file.foo)`
  - `[Data file]({{ site.baseurl }}/data/data-file.csv)`
