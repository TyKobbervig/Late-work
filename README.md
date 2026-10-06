---
## Instructor comments:

- You submitted code for A6 and A7 as markdown files rather than .py files. (I created copies and converted them to .py files for testing/observation/grading.)
- Suggest you "add" a Readme.md for each of the assignments.
- Consider including a brief summary of what each assignment demonstrates or any particular challenges you faced.
---

- **For Debug.a6**

- The actual code had several issues:
  1. your code used for name, grade in students.item() instead of students.items().
  2. And you are try to using "2 indexes" on a dictionary without using .items().
  3. Also this line: average = total / len(student)
     should be: average = total / len(students)
  4. Also, `total =+ grade` should be `total += grade`.

In summary, the main issues were with dictionary methods and proper accumulation of the total grade.

**For A7**

- Not bad! You demonstrated a grasp of the concepts.

**For A8 - Save and Load**

- Your submission for A8 was well-structured and demonstrated a clear understanding of the concepts.

**For A9**

- Your submission for A9 was well-structured and demonstrated a clear understanding of the concepts here as well.

**For A10**

- I was actually looking for a coding example, but your submission still demonstrated an understanding of the concepts.
- An observation of your preferred structure for coding assignments would have been helpful for understanding your approach.
