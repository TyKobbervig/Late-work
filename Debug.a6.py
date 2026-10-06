# Student Grade Tracker

students = {"Alice": 88, "Bob": 92, "Charlie": 79}

print("Student Grades:")

for name, grade in students.item():
    print(name, grade)

total = 0

for grade in students.values():
    total = +grade

average = total / len(student)

print("Average Grade:", average)
