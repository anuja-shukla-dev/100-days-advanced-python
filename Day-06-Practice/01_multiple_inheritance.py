class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print(f"Name: {self.name}")


class Student(Person):
    def __init__(self, name, roll_no):
        Person.__init__(self, name)
        self.roll_no = roll_no

    def display_student(self):
        print(f"Roll no: {self.roll_no}")


class College(Person):
    def __init__(self, name, college_name):
        Person.__init__(self, name)
        self.college_name = college_name

    def display_college(self):
        print(f"College name: {self.college_name}")


class CollegeStudent(Student, College):
    def __init__(self, name, roll_no, college_name):
        Student.__init__(self, name, roll_no)
        self.college_name = college_name


stu = CollegeStudent("Rahul Shukla", 51, "CSJMU")

stu.display_person()
stu.display_student()
stu.display_college()