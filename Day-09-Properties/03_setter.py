class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return f"Marks: {self._marks}"

    @marks.setter
    def marks(self, new_marks):
        self._marks = new_marks

stu = Student(99)
print(stu.marks)
stu.marks = 90
print(stu.marks)
