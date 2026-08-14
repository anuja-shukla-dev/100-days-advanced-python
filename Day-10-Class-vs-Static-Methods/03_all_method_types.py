class Student:
    school = "ABC School"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"School: {self.school}")

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    @staticmethod
    def is_pass(marks):
        if marks>=40:
            return True
        else:
            return False

student = Student("Rahul", 99)
student.display()
Student.school = "XYZ School"
student.display()
print("Pass",Student.is_pass(99))
