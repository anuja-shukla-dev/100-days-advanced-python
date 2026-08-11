class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name} | Marks: {self.marks}"

    def __eq__(self, other):
        return self.marks == other.marks

stu1 = Student("Rahul",99)
stu2 = Student("Geeta", 91)
print(stu1 == stu2)