---
layout: page
title: Help
subtitle: Customizing the Course for Your Needs
---

### Simple setup

The website is setup to be easy to run automatically through GitHub:

1. [Fork]({{ site.baseurl }}/documents/fork-the-course) 
   or [import](https://import.github.com/) the repository
   * In a few minutes you should be able to see the site at:
     `https://yourusername.github.io/semester-biology/`
2. Edit any of the markdown (.md) files
3. Commit and push the changes
   * The changes should now be reflected on the website
4. If you want to use a custom domain name instead of `github.io`, follow
   [GitHub's instructions for setting up a custom domain](https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages/).

If you have any problems please
[let us know](https://github.com/datacarpentry/semester-biology/issues/new) and
we'll be happy to help.

### Preview changes locally using Jekyll

If you want to view your changes locally, before pushing them to the live
website, you'll need to setup [Jekyll](http://jekyllrb.com/) locally. GitHub provides a [good
introduction on how to do this](https://help.github.com/articles/using-jekyll-with-pages/).

If you have Jekyll properly installed, you can then run

`jekyll serve --baseurl ''`

from the command line and navigate to `http://localhost:4000/` in your browser 
to preview the current state of the website.