# Student Grade Tracker

students = {
"Alice": 88,
"Bob": 92,
"Charlie": 79
}

print("Student Grades:")

for name, grade in students.item():
print(name, grade)

total = 0

for grade in students.values():
total =+ grade

average = total / len(student)

print("Average Grade:", average)
code used
error 1
students.item()
problem: Dictionaries use .items() not .item()
fix: students.items()
total =+ grade
problem: assigns a positive value isntead of adding to the running total.
fix;
total += grade
error 3
len(student)
problem: the dictionary is named students, not student
Fix:
len(students)
