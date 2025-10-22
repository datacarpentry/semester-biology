---
layout: page
title: Syllabus
catalog: ALS 6501
credits: 3
semester: Fall 2025
professor: Dr. Ethan White (he/him)
office: Room 1 Building 150
email: ethanwhite@ufl.edu
phone: 352-294-2081
schedule: ['Tuesdays, 12:50-1:40 pm ET', 'Wednesdays, 10:40-12:35 pm ET']
location: "Newins-Ziegler Hall (NZH) 222"
office_hours: "Fridays, 10-11 am"
office_hours_location: "Building 150 (and Zoom - [link](https://ufl.zoom.us/j/95159104000?pwd=MDjrM5MYJNbehlc6lEHkWPkPjwS6UC.1))" 
TA: Alex Blochel
TA_email: alexanderblochel@ufl.edu
---

## Course

{{ site.title }}

{{ page.catalog }}, {{ page.credits }} Credits, {{ page.semester }}

### Instructor

{{ page.professor }}

Office: {{ page.office }}

Email:
[{{ page.email }}](mailto:{{ page.email }})

Phone: {{ page.phone }}


### Location

{{location}}


### Times

{% for class in page.schedule %}
  {{ class }}
{% endfor %}


### Office Hours

Times: {{ page.office_hours }}

Location: {{ page.office_hours_location }}

Or by appointment - please message both {{ page.professor }} and {{ page.TA }} in Canvas


### Teaching Assistant

{{ page.TA }}

Email: [{{ page.TA_email }}](mailto:{{ page.TA_email }})


### Website

The syllabus and other relevant class information and resources will be posted
on Canvas and at [{{ site.url}}]({{ site.baseurl }}/).
Changes to the schedule will be posted to both and announced on Canvas.


### Course Communications

Canvas: Messages in canvas are the preferred method for course communication

Email: [{{ page.email }}](mailto:{{ page.email }})


### Required Texts

There is no required text book for this class.

All needed material is openly available on the course website. If you are
interested in additional reading on the topics we are covering I highly
recommend [R for Data Science](https://r4ds.hadley.nz/), which is freely
available on the web.


### Course Description

An introduction to data management, manipulation, and analysis, with an emphasis
on biological problems. Class consists of short introductions to new concepts
followed by hands on computing exercises using R and SQLite, but the concepts
apply to programming languages and databases more generally. No background in
computing is required.


### Prerequisite Knowledge and Skills

Knowledge of basic biology to provide context for exercises.


### Purpose of Course

In this course you will learn all of the fundamental aspects of computer
programming that are necessary for conducting biological research. By the end of
the course you will be able to use these tools to import data into R, perform
analysis on that data, and export the results to graphs, text files, and
databases. By learning how to get the computer to do your work for you, you will
be able to do more science faster.


### Course Objectives and Goals

Students completing this course will be able to:

* Create well structured data
* Extract information from data
* Write computer programs in R
* Automate data analysis
* Apply these tools to address biological questions
* Apply general data management and analysis concepts to other programming
  languages and database management systems


### How this course relates to the Student Learning Outcomes in Wildlife Ecology and Conservation

This course contributes to the 'Quantitative Skills' and 'Conducting and
Analyzing Independent/Original Research' Student Learning Outcomes specified in
the
[Ph.D. and MS in Wildlife Ecology and Conservation Academic Assessment Plans](https://fora.aa.ufl.edu/docs/1//16Apr13//CALS_WIE_PHD_GAAP_2012-2013_final.pdf),
by providing students the skills and knowledge they need to manage and analyze
the data used in research.


### Instructional Methods

Classes will involve brief introductions to new concepts followed by working on exercises in
class that cover that concept. While students are working on exercises the
instructor will actively engage with students to help them understand material
they find confusing, explain misunderstandings and help identify mistakes that
are preventing students from completing the exercises, and discuss novel
applications and alternative approaches to the data analysis challenges students
are attempting to solve.

### Gender-Neutral and Family Restrooms

There are two gender-neutral restrooms available in the building where the course is taught:
* 1st floor in Room 124
* 3rd floor in Room 304

There are also two gender-neutral restrooms available in the building where the instructor's office is located.

For more information on gender-neutral and family restrooms see:

- [UF Campus Map](https://campusmap.ufl.edu/#/) (click the menu in top left corner, select `Wellness`, and select either `Inclusive, Unisex Restrooms` or `Inclusive, Family Restrooms`)
- [Gender-Neutral Restrooms at UF Map](https://www.google.com/maps/d/u/0/edit?mid=1q6SbWhwmYRCz1KHqyeUHjhyGguI&ll=29.644933459100784%2C-82.36141954894258&z=14)

## Course Policies

### Attendance Policy

Attendance will not be taken or factor into the grades for this class. However,
experience suggests that students who regularly miss class often struggle to learn the material.


### Quiz/Exam Policy

There are no quizzes or exams in this course.


### Make-up policy

Life happens and therefore there is an automatic grace period of 48 hours for
the submission of late assignments with no need to request an extension.
However, it is highly recommended that you submit assignments on time when
possible because assignments build on one another and it can be hard to catch up
if you fall behind. Reasonable requests for longer extensions will also be granted.
Assignments turned in after the 48 hour grace period without an extension will be
be graded with a 20% penalty.


### Assignment policy

Assignments are due Monday night by 11:59 pm Eastern Time.
This timing allows you to be finished with one week's material before starting the next week's material.
Assignments should be submitted as links to via Canvas.

### Course Technology

Students are required to provide their own laptops and to install free and open
source software on those laptops. Support will be provided by the instructor in
the installation of required software. If you don't have access to a laptop
please contact the instructor and they will do their best to provide you with
one.


### Materials and Supplies Fees

There are no materials and supplies fees for this course.


## UF Policies

Information on UF academic policies, academic resources, and compus health and wellness resources is available on the [Academic Policies & Resources webpage](https://go.ufl.edu/syllabuspolicies).

## Grading Policies

The goal of grading in this class is to encourage practice, which is crucial to learning computing skills.
Given that goal grading is based on weekly (equally weighted) assignments, with the focus of each assignment on practicing new material learned each week and reinforcing information learned earlier in the semester.

Because the goal is practice, exercises in assignments will be graded as follows:

* Code runs, uses the requested approach, and produces approximately the correct answer: 100%
* Attempts to solve the problem and makes some progress using the core concept, but does not produce approximately the correct answer or demonstrate basic comfort with the core concept: 50%
* Not submitted or no meaningful effort demonstrated: 0%

Students also enter the class with different levels of experience.
The goal of assignments to is help students grow as computational scientists whether they are complete novices or have some limited background in coding.
Therefore, on many assignments there are optional *Challenge* exercises that are both more difficult and require integrating all of the weeks material.
Students who are already familiar with the basics may choose to submit *Challenge* exercises in place of regular exercises if they wish.
One *Challenge* exercise counts for two regular exercises.
Alternatively *Challenge* exercises can be completed in addition to all regular exercises for up to 10 pts of extra credit.
Please indicate at the top of your assignment if you are substituting *Challenge* exercises.

### Grading scale

- **A 93-100**
- **A- 90-92.9**
- **B+ 87-89.9**
- **B 83-86.9**
- **B- 80-82.9**
- **C+ 77-79.9**
- **C 73-76.9**
- **C- 70-72.9**
- **D+ 67-69.9**
- **D 60-66.9**
- **E <60**


### UF grading policies for assigning grade points

UF policies related to grades are available on the [Grades and Grading Policies webpage](https://catalog.ufl.edu/UGRD/academic-regulations/grades-grading-policies/).

## Course Schedule

The detailed course schedule is available on Canvas and on the course website at:
[{{ site.url }}/schedule]({{ site.baseurl }}/schedule).
