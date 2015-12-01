---
layout: page
title: Help
subtitle: Providing Feedback and Contributing New Material
---

# Contributing New Material

Data Carpentry is an open source project, and we welcome contributions of all
kinds: new and improved lessons, bug reports, and small fixes to existing
material are all useful.

By contributing, you are agreeing that Data Carpentry may redistribute your work
under [these licenses](LICENSE.md).


**Table of Contents**

*   [Working With GitHub](#working-with-github)
*   [Locations and Formats](#locations-and-formats)
*   [FAQ](#faq)


## Working With GitHub

1.  Fork the `datacarpentry/sql-ecology` repository on GitHub.

2.  Clone that repository to your own machine.

3.  Create a branch from `gh-pages` for your changes.
    Give your branch a meaningful name,
    such as `fix-typos-in-select-query`
    or `add-groupby`.

4.  Make your changes, commit them, and push them to your repository on GitHub.

5.  Send a pull request to the `gh-pages` branch of the repository

If it is easier for you to send them to us some other way,
please mail us at
[board@datacarpentry.org](mailto:board@datacarpentry.org).
Given a choice between you creating content or wrestling with Git,
we'd rather have you doing the former.


## Locations and Formats

Every lesson has its own repository, with individual files for each topic. We
use two digits followed by a one-word topic key to ensure files appear in the
right order when listed.

Lessons should be written in Markdown.

## Datasets

We don't store data for lessons inside the lesson repositories. For completed
lessons the data should be publicly available in a data repository appropriate
to the data type. For lesson development the data may be provided in any way
that is convenient including posting to a website, on
[figshare](http://figshare.com/), a public dropbox link, a
[GitHub gist](https://gist.github.com), or even included in the PR. Once the PR
is ready to merge the data should be placed in the
[official data repository](http://figshare.com/articles/Portal_Project_Teaching_Database/1314459)
and all links to the data updated.

## Formatting of the material

To ensure a consistent formatting of the lessons, we recommend the following
guidelines:
* No trailing white space
* Wrap lines at 80 characters (unless it breaks URLs)
* Use unclosed `#` symbols for headers, e.g. `# Heading 1`

## FAQ

*   *Where can I get help?*
    <br/>
    Open an issue or email the Discuss list at [dc-discuss@lists.idyll.org](mailto:dc-discuss@lists.idyll.org)
