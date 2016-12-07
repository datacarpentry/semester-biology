---
layout: exercise
topic: Help
title: Customizing the Course for Your Needs
---

The website is setup to be easy to run automatically through [GitHub](http://github.com):

- [Fork]({{ site.baseurl }}/docs/course/forking-the-course) 
   or [import](https://import.github.com/) the repository to 
   `https://github.com/yourusername/semester-biology`.
   - You may change the `Repository name` (`semester-biology`) from the 
     `Settings` tab.
   
- Update `# Setup` information in `_config.yml` in the main directory for proper
  site rendering.
  - You must `push` this change to your repository to build and browse your 
    forked version.
  - In a few minutes you should be able to see a copy of the site at:
    `https://yourusername.github.io/semester-biology/`
  - If you want to use a custom domain name instead of `github.io`, follow
    [GitHub's instructions for setting up a custom domain](https://help.github.com/articles/using-a-custom-domain-with-github-pages/).
  - If you choose to keep the "Data Carpentry" name in your `title:`, please
    [contact us via email ({{ site.email }})](mailto:{{ site.email }}) 
    to confirm permission.

- [Add or Edit]({{ site.baseurl }}/docs/course/manage-files) any of the course content files. In particular, you will be interested to update:
  - course description in `index.md` in the main directory
  - course details and policy in `syllabus.md` in the main directory
  - `assignments:` list in the `schedule.md` front matter
  - motivation and support documents in `about/`
  - software download and install in `computer-setup.md`

- If you have any problems please [let us know]({{ site.github.repo}}/issues/new) and we'll be happy to help.

Check out some examples of customized courses:

- [Introduction to Ecology](https://atredennick.github.io/ecology_class/) by [Andrew Tredennick](https://atredennick.github.io/)
- [Introduction to Scientific Computing](https://palderman.github.io/IntroSciComp/) by [Phillip Alderman](http://pss.okstate.edu/pass-drctry/faculty/alderman/alderman)

   *Please, let us know if you have developed a customized version of the course
   so we can list it here.*