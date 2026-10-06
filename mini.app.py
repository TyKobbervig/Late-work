# Student Grade Tracker

# Dictionary to store student names and grades
students = {
    "Alice": 88,
    "Bob": 92,
    "Charlie": 79,
    "Diana": 95
}

# Retrieve and display a specific value
print("Bob's grade:", students["Bob"])

print("\nAll Student Grades:")
# Iterate through the dictionary
for name, grade in students.items():
    print(f"{name}: {grade}")

# Calculate the class average
total = 0
for grade in students.values():
    total += grade

average = total / len(students)

print(f"\nClass Average: {average:.2f}")

# Add a new student
students["Ethan"] = 85

print("\nUpdated Student List:")
for name, grade in students.items():
    print(f"{name}: {grade}")