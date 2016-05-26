---
layout: exercise
title: Help
subtitle: Adding and Modifying Exercises
---

### Adding New Exercises

Each exercise is stored as a [markdown file](http://daringfireball.net/projects/markdown/basics) (`.MD`) in the `exercises/` directory. 
Each `exercise.md` needs to start with standard content that [Jekyll](http://jekyllrb.com/) uses to 
automate rendering of the website. The starting content, or 'Front Matter', is entered 
using something called YAML and provides information used to organize and 
automate the website by `topic`, `title`, and `language`. The standard 
`exercise.md` front matter looks like:

```
---
layout: exercise
topic: Topic group of exercise
title: Name of exercise
language: [R, Python, SQL]
---
```

- Open a new text file. Determine the `topic` and `title` of your new exercise 
and name the file with the format `topic-title-language.md` in the   
`exercises/` directory. For example the file named `Making-choices-choice-operators-R.md` will have front matter like: 

```
---
layout: exercise
topic: Making Choices
title: Choice Operators
language: R
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
located and what the file name is. So if you created a new exercise in the `exercises/` folder called `my-awesome-exercise.md` it would be located

   - locally at: `http://localhost:4000/exercises/my-awesome-exercise`

   - after pushing to GitHub at:
`https://yourusername.github.io/semester-biology/exercises/my-awesome-exercise`

- Add `output/` files for corresponding exercises in the `output/` directory with names that match the corresponding exercise with numerals following a `-` for multiple output files. For instance, the set of output files for 
   - `Making-choices-choice-operators-R.md` would be 
   - `Making-choices-choice-operators-R-1.png` and `Making-choices-choice-operatorts-R-2.txt`.

- Be sure to [contribute]({{ site.baseurl l}}/docs/contributing.md) your new exercise to the [Data Carpentry Repository](https://github.com/datacarpentry/semester-biology)


### Modifying Existing Exercises

Modifying content in an exercise is easy.

- Modify the content in the exercise.

- Add, commit, and push the new file to GitHub to get the content added to the website. These steps are further described in [Course Customization Help]({{ site.baseurl }}/docs/course-customization).

Modifying the front matter of an exercise is a bit more challenging. Changing the front matter requires additional steps to maintain proper rendering of the website. 

- Modify the `topic`, `title` and/or `language` components of the front matter. 

- Rename the `exercise.md` file to match the revised front matter using the `topic-title-language.md` general format.

- Rename companion `solutions/` files to match the new `topic-title-language.md` general format.

- Fix links to the revised exercise file in other exercises. These links usually appear as reference for follow-up exercises.

- Revise `title` in `assignments/` `exercises:` list. 

If you have made a bug fix, exercise variation or have otherwise improved an exercise, be sure to [contribute]({{ site.baseurl l}}/docs/contributing.md) your exercise revision to the [Data Carpentry Repository](https://github.com/datacarpentry/semester-biology).