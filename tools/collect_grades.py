"""Collects grades from grading sheets

Searching through existing grading sheets by student name and create a table of
grades for each assignment.

"""

import glob
import os
import pandas as pd

assignments = ['HW1', 'HW2', 'HW3', 'HW4', 'HW5', 'HW6', 'HW7']

def get_student(path):
    filename = os.path.basename(path)
    filename, extension = os.path.splitext(filename)
    student = filename.split('_')[-1]
    return student

grades = []
for assignment in assignments:
    assignment_grades = {}
    grade_files = glob.glob('./HW1/grade_*.txt')
    for grade_file in grade_files:
        student = get_student(grade_file)
        with open(grade_file, 'r') as current_file:
            for line in current_file:
                if line.startswith('Grade:'):
                    grade = line.strip().split()[-1]
                    break
        assignment_grades[student] = grade
    grades.append(assignment_grades)

grades = pd.DataFrame(grades)
