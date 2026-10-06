class Student:
    def __init__(self, name, grade):
        self.name = name  # attribute
        self.grade = grade  # attribute

    def display_info(self):  # method
        print(f"{self.name} has a grade of {self.grade}")


# Instantiate an object
student1 = Student("Alice", 88)

# Call a method
student1.display_info()

# the class is Student
# Attributes self.name and self.grade
# the method is display_info()
# Instantiate an Object student1 = Student("Alice", 88)
# calling the method
student1.display_info()


# small modification
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"{self.name} has a grade of {self.grade}")

    def is_passing(self):
        if self.grade >= 60:
            print("Passing")
        else:
            print("Failing")


student1 = Student("Alice", 88)

student1.display_info()
student1.is_passing()
