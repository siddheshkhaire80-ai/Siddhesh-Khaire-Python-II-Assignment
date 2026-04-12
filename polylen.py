# Parent class

class Person:

    def __init__(self, name, age):

        self.name = name

        self.age = age



    def display_person(self):

        print(f"Name: {self.name}")

        print(f"Age: {self.age}")





# Child class

class Student(Person):

    def __init__(self, name, age, marks):

        # Call the constructor of the parent class

        super().__init__(name, age)

        self.marks = marks



    def display_student(self):

        # Access parent class method

        self.display_person()

        print(f"Marks: {self.marks}")





# Creating an object of Student class

student1 = Student("Alice", 20, 85)



# Displaying student details

student1.display_student()
