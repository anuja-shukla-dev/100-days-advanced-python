class Student:
    school_name = "ABC School"
    student_count = 0

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.student_count+=1

    def display(self):
        print("*"*30)
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"School: {self.school_name}")

    def calculate_grade(self):
        if self.marks >= 90:
            return "Grade A"
        elif 75<=self.marks<=89:
            return "Grade B"
        elif 60<=self.marks<=74:
            return "Grade C"
        elif 40<=self.marks<=59:
            return "Grade D"
        else:
            return "Grade F"

    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school

    @classmethod
    def get_student_count(cls):
        return cls.student_count

    @staticmethod
    def is_valid_marks(marks):
        if 0 <= marks <= 100:
            return True
        else:
            return False

    @staticmethod
    def percentage_to_grade(percentage):
        if percentage >= 90:
            return "Grade A"
        elif 75<= percentage <=89:
            return "Grade B"
        elif 60<= percentage <=74:
            return "Grade C"
        elif 40<= percentage <=59:
            return "Grade D"
        else:
            return "Grade F"

student1 = Student("Rohit",90)
student2 = Student("Rohit",67)
student3 = Student("Rohit",41)

student1.display()
print(student1.calculate_grade())
student2.display()
print(student2.calculate_grade())
student3.display()
print(student3.calculate_grade())

Student.school_name = "XYZ School"
student1.display()
student2.display()
student3.display()

print("Student count:",Student.get_student_count())

print("Valid marks:",Student.is_valid_marks(102))
print(Student.percentage_to_grade(78))