class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("*"*30)
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

    @classmethod
    def from_string(cls, data):
        name, marks = data.split("-")
        return cls(name, int(marks))

student1 = Student("Anuja Shukla", 99)
student1.display()

student2 = Student.from_string("Rahul-98")
student2.display()

