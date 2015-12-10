---
layout: page
title: Help
subtitle: Add, Modify, and Manage Assignments
---

## Add or modify a new assignment

- Create or modify a [markdown file](http://daringfireball.net/projects/markdown/basics) from the `assignments/` directory. 
- Use the following standard assignments page template to be sure the file content is read correctly by [Jekyll](http://jekyllrb.com/). Items that we expect you to input are noted in _italics_. [[ EXTRA INFO: Each markdown file needs to start with some information and standard content that is stored in a way Jekyll uses to automate rendering of the website. The starting content, or 'Front Matter', is entered using something called YAML and provides information that Jekyll uses to organize the website, like the title of the page, what language it applies to, and a list of accompanying files. The body mainly includes the 'Learning Objectives' content and two [Liquid](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers) tags that are used by 
Jekyll that MUST be included AS IS. ]]

```
---
layout: page
title: _Name-of-assignment_
subtitle: _Assignment-topic-or-short-description_
language: _R-Python-or-SQL_
exercises: ['_List_', '_of_', '_exercise_', '_titles_']
---

####Learning Objectives

> Following this assignment students should be able to:

> - _objective 1_
> - _objective 2_
> - _objective 3_

{% include reading.html %}

{% include assignment.html %}
```

- Add, commit, and push the new file to GitHub to get the content added to the website. These steps are further described in [Course Customization Help]({{ site.baseurl }}/documents/course-customization).


## Accessing an assignment file on the web

The page should be available at a url based on where the file is located
and what the file name is. So if you created a new assignment in the `assignments/` folder called `my_awesome_assignment.md` it would be located

locally at: `http://localhost:4000/assignments/my_awesome_assignment`

after pushing to GitHub at:
`https://yourusername.github.io/semester-biology/assignments/my_awesome_assignment`