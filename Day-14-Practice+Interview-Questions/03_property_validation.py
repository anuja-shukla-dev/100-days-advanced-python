class Employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def salary(self):
        return f"Rs.{self._salary}"

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary should be postive")

        self._salary = new_salary


sal = int(input("Enter salary: "))
emp = Employee(sal)
print("Salary",emp.salary)
