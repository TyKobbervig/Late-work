import csv

# Open and read the CSV file
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    total_students = 0
    total_grades = 0

    for row in reader:
        total_students += 1
        total_grades += int(row["Grade"])

# Calculate average grade
average = total_grades / total_students

# Display report
print("Student Report")
print("--------------")
print("Total Students:", total_students)
print("Average Grade:", round(average, 2))