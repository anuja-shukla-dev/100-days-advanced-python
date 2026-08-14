class Employee:
    company = "TechCorp"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.company}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

emp1 = Employee("Rahul", 10000)
emp2 = Employee("Rohit", 12000)
emp1.display()
emp2.display()
Employee.company = "Apple"
emp1.display()
emp2.display()