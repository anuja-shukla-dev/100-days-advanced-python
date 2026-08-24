class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("*"*30)
        print("Name",self.name)
        print("Age",self.age)
        print("*"*30)

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

stu = Student.from_string("Anuja-120")
stu.display()
