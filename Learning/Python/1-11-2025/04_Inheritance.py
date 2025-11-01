# Inheritance
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class StudentGender(Student):
    def __init__(self, name, age , gender):
        super().__init__(name, age) # with the help of super we can access the data of the class from where we are taking the values like name, age.
        self.gender = gender

# The StudentGender is the class which is been inheriting the data from the previous class Student, where we have already mentioned about student name and age,


student1 = StudentGender("Stud_name", "Stud_age", "Stud_gender")

print(student1.name, student1.gender)