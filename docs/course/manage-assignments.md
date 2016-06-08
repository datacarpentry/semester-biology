---
layout: exercise
title: Help
subtitle: Adding and Modifying Assignments
---

- Create or modify a [markdown file](http://daringfireball.net/projects/markdown/basics) from the `assignments/` directory.
 
- Use the [assignments template]({{ site.baseurl }}/docs/assignments-template) [[Raw](https://raw.githubusercontent.com/datacarpentry/semester-biology/gh-pages/docs/assignments-template.md)] to be sure the file content is read correctly 
by [Jekyll](http://jekyllrb.com/). Items that we expect you to input are `title:`, `language:`, `exercises:`, the 'Learning Objectives' list. 
[[ EXTRA INFO: Each markdown file needs to start with some information and 
standard content that is stored in a way Jekyll uses to automate rendering of 
the website. The starting content, or 'Front Matter', is entered using something 
called YAML and provides information that Jekyll uses to organize and automate 
the website, like the title of the page, what language it applies to, and a list 
of accompanying files. The body mainly includes the 'Learning Objectives' 
content and two [Liquid](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers) tags that are used by Jekyll that MUST be included AS IS. ]]

- Add, commit, and push the new file to GitHub to get the content added to the website. These steps are further described in [Course Customization Help]({{ site.baseurl }}/docs/course-customization).

- Access the assignment file on the web at the url based on where the file is 
located and what the file name is. So if you created a new assignment in the 
`assignments/` folder called `my_awesome_assignment.md` it would be located

   - locally at: `http://localhost:4000/assignments/my_awesome_assignment`

   - after pushing to GitHub at: 
`https://yourusername.github.io/semester-biology/assignments/my_awesome_assignment`