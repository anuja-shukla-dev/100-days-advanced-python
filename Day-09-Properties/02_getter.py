class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return f"{self._name}"
    
    @property
    def age(self):
        return f"{self._age}"

person = Person("Rahul", 21)
print(person.name)
print(person.age)