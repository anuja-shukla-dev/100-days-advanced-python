# Day 10 - Class vs Static Methods

## Overview

Today I learned about class methods and static methods in Python, their syntax, use cases, and how they differ from instance methods.

## Topics Covered

- Instance methods
- Class methods
- Static methods
- `@classmethod` decorator
- `@staticmethod` decorator
- `cls` parameter
- `self` parameter
- Difference between instance, class, and static methods
- Alternative constructors
- Class-level data management
- Practical use of different method types

## Method Types in Python

### Instance Method

An instance method works with the data and behavior of a particular object.

It takes `self` as its first parameter.

Example:

def display(self):
    print(self.name)

### Class Method

A class method works with class-level data and takes `cls` as its first parameter.

It is created using the `@classmethod` decorator.

Example:

@classmethod
def display_class_data(cls):
    print(cls.value)

### Static Method

A static method does not depend on instance or class data.

It is created using the `@staticmethod` decorator.

Example:

@staticmethod
def add(a, b):
    return a + b

## Class Method

Class methods can access and modify class-level attributes.

Example:

class Student:
    college = "CSJMU"

    @classmethod
    def change_college(cls, name):
        cls.college = name

## Static Method

Static methods are used when a method is logically related to a class but does not need access to instance or class attributes.

Example:

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

## Alternative Constructor

A class method can be used as an alternative constructor.

Example:

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls, data):
        name, marks = data.split("-")
        return cls(name, int(marks))

student = Student.from_string("Anuja-90")

## Difference Between Method Types

Instance Method:
- Uses `self`
- Works with instance data
- Called using an object

Class Method:
- Uses `cls`
- Works with class-level data
- Can be used as an alternative constructor

Static Method:
- Uses neither `self` nor `cls`
- Does not depend on instance or class state
- Used for utility operations related to the class

## Practice Programs

1. Class Method
2. Static Method
3. All Method Types
4. Alternative Constructor
5. Employee Management System
6. Bank Account
7. Student System

## Day 10 Files

01_class_method.py
02_static_method.py
03_all_method_types.py
04_alternative_constructor.py
05_employee_management.py
06_bank_account.py
07_student_system.py
README.md

## Key Takeaway

Instance methods work with object-specific data, class methods work with class-level data, and static methods provide utility functionality that does not require access to either instance or class data.
