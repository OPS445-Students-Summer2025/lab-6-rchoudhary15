from student import Student

student1 = Student('John', 13454900)  # int number will be converted to string
student1.displayStudent()

student2 = Student('Jessica', '023384103')
student2.displayStudent()

student1.addGrade('uli101', 4.0)
student1.addGrade('ops245', 3.5)
student1.addGrade('ops445', 3.0)

student2.addGrade('ipc144', 4.0)
student2.addGrade('cpp244', 4.0)

student1.displayGPA()
student2.displayGPA()

student1.displayPassedCourses()
student2.displayPassedCourses()

# Demonstrate zero GPA scenario
student3 = Student('Jen', '034686901')
student3.displayGPA()
student3.displayPassedCourses()

# Show name update and string handling
print(student1.name)
student1.name = 'Jack'
print(student1.name)
print(len(student1.name))
