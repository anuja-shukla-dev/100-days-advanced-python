class Employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def salary(self):
        return f"Salary: {self._salary}"

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        
        self._salary = new_salary

sal = int(input("Enter salary: "))
emp = Employee(sal)
print(emp.salary)