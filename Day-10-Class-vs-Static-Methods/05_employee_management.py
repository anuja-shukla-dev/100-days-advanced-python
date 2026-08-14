class Employee:
    company = "TechCorp"
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count+=1

    def display(self):
        print("="*20)
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.company}")


    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    @staticmethod
    def is_valid_salary(salary):
        if salary > 0:
            return True
        else:
            return False

emp1 = Employee("Rahul", 4000)
emp2 = Employee("Rohit",5000)
emp3 = Employee("Harry",600)

emp1.display()
emp2.display()
emp3.display()

print(f"Employee count: {Employee.get_employee_count()}")

Employee.company = "Microsoft"
emp1.display()
emp2.display()
emp3.display()

print(f"Salary Valid: {Employee.is_valid_salary(1)}")
print(f"Salary Valid: {Employee.is_valid_salary(-10)}")