class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return f"{self._name}"

student = Student("Anuja Shukla")
print(student.name)