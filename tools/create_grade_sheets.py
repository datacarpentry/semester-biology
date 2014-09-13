#!/usr/bin/python
names = ['Timothy Beach', 'Leland Bennion', 'Lette Benson', 'Shanna Chugg',
         'Kenneth Kehoe', 'Kari Norman', 'Mehmet Ozturk', 'Alexandre Rego',
         'Brian Rozick', 'Eric Sodja', 'Bethany Unger', 'Zachary Valois',
         'Darrel Woodruff', 'Ryan Berry', 'Ryan Choi', 'Matthew Del Grosso',
         'Rebekah Downard', 'Camilo Fagua', 'Erica Hansen', 'Jay Hemmis',
         'Sajeena Horvath', 'Martha Jensen', 'Sara Kelly', 'Eric Lamalfa',
         'Jarod Raithel', 'Kristina Riemer', 'Rebecca Rossi', 'Rebecca Tobin',
         'Alison Webb']

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
