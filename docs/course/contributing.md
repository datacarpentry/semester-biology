---
layout: exercise
topic: Help
title: Providing Feedback and Contributing New Material
---

### Providing feedback and getting help
{% if site.github.repo == 'https://github.com/datacarpentry/semester-biology' %}
- [Open a new issue]({{ site.github.repo }}/issues/new) at the `{{ site.github.repo | remove: 'https://github.com/' }}` repository on [GitHub](http://github.com) (*You'll have to be logged into GitHub*).
- Provide a clear description of your question, comment, or proposed change in 
the `Title` section and use the `Leave a comment` section for further detail or discussion. 
- Select `Submit new issue` and the repository maintainers will be notified of your feedback. Thanks!

OR

- You can also email us at [{{ site.email }}](mailto:{{ site.email }}). (*Though we prefer organizing comments and issues on GitHub, we want to hear from you and we want it to be easy.*)

{% else %}
#### Have an issue about the course material?
- [Open a new issue]({{ site.github.repo }}/issues/new) at the `{{ site.github.repo | remove: 'https://github.com/' }}` repository on [GitHub](http://github.com) (*You'll have to be logged into GitHub*).
- Provide a clear description of your question, comment, or proposed change in 
the `Title` section and use the `Leave a comment` section for further detail or discussion. 
- Select `Submit new issue` and the repository maintainers will be notified of your feedback. Thanks!

OR

- You can email us at [{{ site.email }}](mailto:{{ site.email }}). (*Though we prefer organizing comments and issues on GitHub, we want to hear from you and we want it to be easy.*)

#### Have an issue with the course website?
- [Open a new issue](https://github.com/datacarpentry/semester-biology/issues/new) at the `datacarpentry/semester-biology` main repository on [GitHub](http://github.com) (*You'll have to be logged into GitHub*).
- Provide a clear description of your question, comment, or proposed change in 
the `Title` section and use the `Leave a comment` section for further detail or discussion. 
- Select `Submit new issue` and the repository maintainers will be notified of your feedback. Thanks!

OR

- You can email us at [datacarpentrysemester@weecology.org](mailto:datacarpentrysemester@weecology.org). (*Though we prefer organizing comments and issues on GitHub, we want to hear from you and we want it to be easy.*)
{% endif %}

### Contributing New Material

We use standard [GitHub flow](https://guides.github.com/introduction/flow/):
fork the repository, add or change material, and submit a pull request.

- From a local GitHub repository 
   1. [Fork and clone](https://help.github.com/articles/fork-a-repo/) the  
[`datacarpentry/semester-biology` repository on GitHub](https://github.com/datacarpentry/semester-biology).
   2. Create a branch from `gh-pages` for your changes. Give your branch a 
      meaningful name, such as `fix-typos-in-select-query` or `add-groupby`.
   4. Make your changes, [commit them, and push them to your repository on  GitHub](https://help.github.com/articles/create-a-repo/#commit-your-first-change).
   5.  Send a [pull request](https://help.github.com/articles/using-pull-requests/) to the `gh-pages` branch of the main repository.

- From GitHub.com
   1. Click on the `Fork` button at the top right corner of the [`datacarpentry/semester-biology` repository on GitHub](https://github.com/datacarpentry/semester-biology).
   2. Navigate to your forked repository at `https://yourusername.github.io/semester-biology/`
   3. Navigate to the file or directory you want to change (*like [`contributing.md`](https://github.com/datacarpentry/semester-biology/blob/gh-pages/docs/contributing.md)*) and click on the <i class="fa fa-pencil"></i> button to edit. 
   4. Make changes to the file.
   5. Commit the changes using the form at the bottom of the `edit` page. If you are working on your own forked version of the course, you can choose 'Commit directly to the `gh-pages` branch'. The other option ('Create a **new branch**') is used for a work flow with [Pull Requests](https://help.github.com/articles/using-pull-requests), which is our preferred way of receiving collaborative contributions.

- If it is easier for you to send your changes to us some other way, please 
email us at [datacarpentrysemester@weecology.org](mailto:datacarpentrysemester@weecology.org). Given a choice between you creating content or wrestling with Git, we'd rather have you doing the former.


### Philosophy

Data Carpentry for Biologists is an open source project, and we welcome 
contributions of all kinds: new and improved lessons, bug reports, and small 
fixes to existing material are all useful. Course materials are managed on 
GitHub to facilitate collaboration on developing this kind of material for 
university courses. The central component of a [flipped computing course]({{ site.baseurl }}/docs/course/course-delivery) is the 
exercises, so one of the primary forms of contribution we expect will be adding 
exercises to the existing set. Individual instructors can then select from a 
rich pool of exercises the set that best fit the topics, languages, and 
scientific domains they want to cover in the course.

There are lots of great resources for being introduced to the individual
concepts being taught in courses like this. Our philosophy is to use and improve
these external resources when available instead of creating new versions of the
same content. In particularly we actively use
[Data Carpentry](http://datacarpentry.org/lessons) and
[Software Carpentry](http://software-carpentry.org/lessons) workshop
materials. However, in cases where the necessary material doesn't exist
elsewhere it can certainly be added to `materials/`.

By contributing, you are agreeing that your work is [licensed using a combination of CC-BY and MIT licenses]({{ site.baseurl }}/LICENSE) and may be openly used, modified, and distributed by others.


