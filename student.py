#!/usr/bin/env python3
# Author ID: rchoudhary15

class Student:

    def __init__(self, name, number):
        self.name = str(name)
        self.number = str(number)
        self.courses = {}

    def displayStudent(self):
        print('Student Name: ' + self.name)
        print('Student Number: ' + self.number)

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        if len(self.courses) == 0:
            print(f"GPA of student {self.name} is 0.0 (no courses added yet)")
            return
        total = sum(self.courses.values())
        gpa = total / len(self.courses)
        print('GPA of student ' + self.name + ' is ' + str(round(gpa, 2)))

    #  New method to list all passed courses (assuming passing grade is ≥ 2.0)
    def displayPassedCourses(self):
        passed = [course for course, grade in self.courses.items() if grade >= 2.0]
        print(f"{self.name} has passed: {', '.join(passed) if passed else 'No courses passed'}")
