# Day 11 - Closures

## Overview

Today I learned about Closures in Python. A closure is a function that remembers and can access variables from its enclosing scope even after the enclosing function has finished executing.

## Topics Covered

- Nested functions
- Closures
- Enclosing scope
- nonlocal keyword
- Maintaining state using closures
- Function factories
- __closure__
- cell_contents
- Practical use of closures
- Closure behavior and variable references

## Basic Closure

def outer(x):
    def inner():
        return x

    return inner

func = outer(10)
print(func())

The inner function remembers the variable x from the enclosing scope.

## Using nonlocal

Closures can maintain and modify state using the nonlocal keyword.

def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

## Function Factory

A closure can be used to create customized functions.

def multiplier(n):
    def multiply(x):
        return n * x

    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))

Output:
20
30

## Closure Inspection

Python provides __closure__ to inspect the variables captured by a closure.

def outer(x):
    def inner():
        return x

    return inner

func = outer(10)

print(func.__closure__)
print(func.__closure__[0].cell_contents)

cell_contents can be used to access the value stored inside the closure cell.

## Practice Problems

1. Basic Power Closure
2. Counter Closure
3. Multiplier Closure
4. Greeting Closure
5. Closure Inspection
6. Running Total Closure
7. Password Checker Closure

## Important Learning

A closure remembers the variable from its enclosing scope, not necessarily a snapshot of its value when the inner function was created.

Example:

def outer():
    x = 10

    def inner():
        return x

    x = 20
    return inner

func = outer()
print(func())

Output:
20

The inner function returns 20 because it refers to the enclosing variable x.

## Key Takeaway

A closure is a function that remembers and can access variables from its enclosing scope even after the enclosing function has finished execution.

## Day 11 Files

01_basic_closure.py
02_counter_closure.py
03_multiplier_closure.py
04_greeting_closure.py
05_closure_inspection.py
06_running_total_closure.py
07_password_checker_closure.py
README.md
