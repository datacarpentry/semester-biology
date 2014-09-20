#!/usr/bin/python

import numpy as np

names = np.loadtxt("student_names.csv", delimiter=',', dtype=str)

def create_grade_file(template_filename, name):
    lastname = name.split()[-1].lower()
    grade_filename = "grade_%s.txt" % lastname
    with open(template_filename, 'r') as template, open(grade_filename, 'w') as grade_file:
        for line in template:
            if "Name:" in line:
                grade_file.write("Name: %s\n" % name)
            else:
                grade_file.write(line)

if __name__ == "__main__":
    template = "grading_page.txt"
    for name in names:
        create_grade_file(template, name)
