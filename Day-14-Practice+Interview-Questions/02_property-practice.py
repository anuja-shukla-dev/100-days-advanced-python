class Student:
    def __init__(self, marks):
        self.marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, new_marks):
        if new_marks < 0 or new_marks > 100:
            raise ValueError("Marks should be between 0-100")

        self._marks = new_marks

mark = int(input("Enter marks: "))
student = Student(mark)
print("Marks",student.marks)