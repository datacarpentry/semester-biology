---
layout: page
title: Syllabus
catalog: WIS 6934
credits: 3
semester: Fall 2020
professor: Dr. Ethan White (he/him)
office: Zoom
email: ethanwhite@ufl.edu
phone: 
schedule: ['Tuesdays, 3-3:50 pm ET', 'Fridays, 11:45-1:40 pm ET']
location: Zoom
office_hours: "Wednesday & Thursday 2-3 pm ET"
office_hours_location: Zoom
TA: Andrew Marx
TA_email: andrewjmarx@ufl.edu
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

Or by appointment. *Note: my schedule gets very busy during the semester so
please try to schedule appointments as far in advance as possible. In general it
will be very difficult to set up appointments less than 24 hours in advance.*


### Teaching Assistant

{{ page.TA }}

Email: [{{ page.TA_email }}](mailto:{{ page.TA_email }})


### Website

The syllabus and other relevant class information and resources will be posted
at [{{ site.url}}]({{ site.baseurl }}/).
Changes to the schedule will be posted to this site so please try to check it
periodically for updates.


### Course Communications

Email: [{{ page.email }}](mailto:{{ page.email }})


### Required Texts

There is no required text book for this class.

All needed material is openly available on the course website. If you are
interested in additional reading on the topics we are covering I highly
recommend [R for Data Science](https://r4ds.had.co.nz/), which is freely
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


### Teaching Philosophy

This class is taught using a flipped, learner-centered, approach, because
learning to program and work with data requires actively working on
computers. Flipped classes work well for all kinds of content, but I think they
work particularly well for computer oriented classes. If you're interested in
knowing more take a look at this great
[flipped classroom info-graphic](https://assignmentbro.com/wp-content/uploads/2021/02/flipped-classroom-infographics-scaled.jpg).


### Instructional Methods

As a flipped classroom, students are provided with either reading or video
material that they are expected to view/read prior to class. Classes will
involve brief refreshers on new concepts followed by working on exercises in
class that cover that concept. While students are working on exercises the
instructor will actively engage with students to help them understand material
they find confusing, explain misunderstandings and help identify mistakes that
are preventing students from completing the exercises, and discuss novel
applications and alternative approaches to the data analysis challenges students
are attempting to solve. For more challenging topics class may start with 20-30
minute demonstrations on the concepts followed by time to work on exercises.


## Course Policies

### Special Policies for 2020

It has been a long, exhausting, year and it will continue to be so for many of us.
My goal is to help you learn as much as you can, while recognizing that most people have more limitations and less energy than usual.

The course is being taught online for the first time due to the pandemic.
To provide maximum flexibility the course material can be engaged with in three ways:

1. Fully synchronous: Attend class during the scheduled class periods. Follow each lesson, which combine video lectures and exercises, during the class periods and ask for help as you run into questions. This is the closest approximation to how the course normally runs in-person.
2. Synchronous Q&A: Follow each lesson before class, watching the videos and doing the exercises you can. Stop if you get confused. Come to class during the class periods and ask for help on challenges you encountered.
3. Asynchronous: Follow the lessons online and ask for help via Piazza. This is the least ideal approach because the course is generally based around the benefits of direct student-instructor interaction to work through misunderstandings, but we'll do our best to make it work for you.

The course always has flexible deadline policies (see below) and will continue to do so to support students learning under these difficult circumstances.
There is an automatic (no request needed) 48 hour extension on all assignments for those who need it.
If you need more time just let me know.
You never need to disclose personal information to me to get an extension. Just let me know how long you need.

### Class Recording

Our class sessions may be audio visually recorded for students in the class to refer back and for enrolled students who are unable to attend live. Students who participate with their camera engaged or utilize a profile image are agreeing to have their video or image recorded.  If you are unwilling to consent to have your profile or video image recorded, be sure to keep your camera off and do not use a profile image. Likewise, students who un-mute during class and participate orally are agreeing to have their voices recorded.  If you are not willing to consent to have your voice recorded during class, you will need to keep your mute button activated and communicate exclusively using the "chat" feature, which allows students to type questions and comments live. The chat will not be recorded or shared. As in all courses, unauthorized recording and unauthorized sharing of recorded materials is prohibited.

### Attendance Policy

Attendance will not be taken or factor into the grades for this class. However,
experience suggests that students who regularly miss class often struggle to learn the
material.


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
Assignments should be submitted via either RStudio Cloud (for R assignments) or Canvas (for other assignments).

### Course Technology

Students are required to provide their own laptops and to install free and open
source software on those laptops (see [Setup]({{ site.baseurl }}/computer-setup)
for installation instructions). Support will be provided by the instructor in
the installation of required software. If you don't have access to a laptop
please contact the instructor and they will do their best to provide you with
one.


### Materials and Supplies Fees

There are no materials and supplies fees for this course.


## UF Policies


### University Policy on Accommodating Students with Disabilities

The Disability Resource Center coordinates the needed accommodations of students
with disabilities. This includes registering disabilities, recommending academic
accommodations within the classroom, accessing special adaptive computer
equipment, providing interpretation services and mediating faculty-student
disability related issues.Students requesting classroom accommodation must first
register with the Dean of Students Office. The Dean of Students Office will
provide documentation to the student who must then provide this documentation to
the Instructor when requesting accommodation0001 Reid Hall, 352-392-8565,
www.dso.ufl.edu/drc/

My policy: If you are in my class I want to help you learn and will happily work
with you to make the learning environment equitable for you and others.


### Online Course Evaluation Process

Students are expected to provide professional and respectful feedback on the quality of instruction in this course by completing course evaluations online via GatorEvals. Guidance on how to give feedback in a professional and respectful manner is available at https://gatorevals.aa.ufl.edu/students/. Students will be notified when the evaluation period opens, and can complete evaluations through the email they receive from GatorEvals, in their Canvas course menu under GatorEvals, or via https://ufl.bluera.com/ufl/. Summaries of course evaluation results are available to students at https://gatorevals.aa.ufl.edu/public-results/.


### University Policy on Academic Misconduct

Academic honesty and integrity are fundamental values of the University
community. Students should be sure that they understand the UF Student Honor
Code at http://www.dso.ufl.edu/students.php.


### Netiquette and Communication Courtesy

All members of the class are expected to follow rules of common
courtesy in all email messages, threaded discussions and chats.


### Academic Honesty

As a student at the University of Florida, you have committed yourself to uphold
the Honor Code, which includes the following pledge:“We, the members of the
University of Florida community, pledge to hold ourselves and our peers to the
highest standards of honesty and integrity.”You are expected to exhibit behavior
consistent with this commitment to the UF academic community, and on all work
submitted for credit at the University of Florida, the following pledge is
either required or implied: "On my honor, I have neither given nor received
unauthorized aid in doing this assignment."

It is assumed that you will complete all work independently in each course
unless the instructor provides explicit permission for you to collaborate on
course tasks (e.g. assignments, papers, quizzes, exams). Furthermore, as part of
your obligation to uphold the Honor Code, you should report any condition that
facilitates academic misconduct to appropriate personnel. It is your individual
responsibility to know and comply with all university policies and procedures
regarding academic integrity and the Student Honor Code.Violations of the Honor
Code at the University of Florida will not be tolerated. Violations will be
reported to the Dean of Students Office for consideration of disciplinary
action. For more information regarding the Student Honor Code, please see:
http://www.dso.ufl.edu/sccr/process/student-conduct-honor-code


### Software Use

All faculty, staff and students of the university are required and expected to
obey the laws and legal agreements governing software use. Failure to do so can
lead to monetary damages and/or criminal penalties for the individual violator.
Because such violations are also against university policies and rules,
disciplinary action will be taken as appropriate.


### Student Privacy

There are federal laws protecting your privacy with regards to grades earned in
courses and on individual assignments.  For more information, please see:
http://registrar.ufl.edu/catalog0910/policies/regulationferpa.html


## Grading Policies

Grading for this course is based on 13 equally weighted assignments.

Exercises in assignments will be graded as follows:

* Produces the correct answer using the requested approach: 100%
* Generally uses the right approach, but a minor mistake results in an incorrect
    answer: 90%
* Attempts to solve the problem and makes some progress using the core concept:
    50%
* Answer demonstrates a lack of understanding of the core concept: 0%


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

[https://catalog.ufl.edu/UGRD/academic-regulations/grades-grading-policies/](https://catalog.ufl.edu/UGRD/academic-regulations/grades-grading-policies/)


## Campus Helping Resources

Students experiencing crises or personal problems that interfere with
their general well-being are encouraged to utilize the university’s counseling
resources. The Counseling& Wellness Center provides confidential counseling
services at no cost for currently enrolled students. Resources are available on
campus for students having personal problems or lacking clear career or academic
goals, which interfere with their academic performance.

### Health and Wellness 

U Matter, We Care: If you or a friend is in distress, please contact umatter@ufl.edu or 352 392-1575 so that a team member can reach out to the student. 

Counseling and Wellness Center: http://www.counseling.ufl.edu/cwc, 392-1575. 

Sexual Assault Recovery Services (SARS): Student Health Care Center, 392-1161. 

University Police Department: 392-1111 (or 9-1-1 for emergencies), or http://www.police.ufl.edu/. 

### Academic Resources

E-learning technical support: 352-392-4357 (select option 2) or e-mail to Learning-support@ufl.edu. https://lss.at.ufl.edu/help.shtml.

Career Connections Center: Reitz Union, 392-1601.  Career assistance and counseling. https://career.ufl.edu/.

Library Support: http://cms.uflib.ufl.edu/ask. Various ways to receive assistance with respect to using the libraries or finding resources.

Teaching Center: Broward Hall, 392-2010 or 392-6420. General study skills and tutoring. https://teachingcenter.ufl.edu/.

Writing Studio: 302 Tigert Hall, 846-1138. Help brainstorming, formatting, and writing papers. https://writing.ufl.edu/writing-studio/.

### Student Complaints

Student Complaints Campus: https://www.dso.ufl.edu/documents/UF_Complaints_policy.pdf.

On-Line Students Complaints: http://www.distance.ufl.edu/student-complaint-process.

## Course Schedule

The details course schedule is available on the course website at:
[{{ site.url }}/schedule]({{ site.baseurl }}/schedule).
