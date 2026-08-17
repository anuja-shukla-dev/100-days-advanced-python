# 🐍 Day 12 — Decorators

## 📌 Overview

Day 12 of the 100 Days of Advanced Python series focuses on Decorators.

A decorator is a function that takes another function, adds or modifies its behavior, and returns the modified function without directly changing the original function's source code.

---

## 🎯 Learning Objectives

By completing Day 12, I learned:

- What decorators are
- Why decorators are used
- How functions can be passed as arguments
- How a decorator receives a function
- How wrapper functions work
- How to use the @decorator syntax
- How to execute code before and after a function
- How to reuse one decorator with multiple functions
- How decorators can modify function behavior
- How the decorator and wrapper work together

---

## 🧠 What is a Decorator?

A decorator is a function that extends or modifies the behavior of another function without modifying its original source code.

Basic structure:

    def decorator(func):
        def wrapper():
            # Additional behavior
            func()
            # Additional behavior

        return wrapper

---

## 🔹 Using the @ Syntax

A decorator can be applied using @:

    @decorator
    def greet():
        print("Hello!")

The above syntax is equivalent to:

    def greet():
        print("Hello!")

    greet = decorator(greet)

---

## 🔹 Wrapper Function

A wrapper is an inner function used by the decorator.

Example:

    def decorator(func):

        def wrapper():
            print("Before function")
            func()
            print("After function")

        return wrapper

Here:

- decorator() receives the original function.
- wrapper() adds extra behavior.
- func() calls the original function.
- wrapper is returned by the decorator.

---

## 🔄 Decorator Execution Flow

    Original Function
           ↓
    Decorator receives Function
           ↓
    Wrapper Function is Created
           ↓
    Decorator returns Wrapper
           ↓
    @decorator replaces Original Function
           ↓
    Calling Function
           ↓
    Wrapper Executes
           ↓
    Original Function Executes

---

## 📂 Practice Programs

### 01 — Basic Decorator

File: 01_basic_decorator.py

Created a basic decorator and learned how it executes additional code before calling a function.

### 02 — Before and After

File: 02_before_after.py

Created a decorator that executes code both before and after the original function.

### 03 — Function Reference

File: 03_function_reference.py

Practiced passing a function as an argument to another function.

### 04 — Multiple Functions

File: 04_multiple_functions.py

Applied the same decorator to multiple functions and understood decorator reusability.

### 05 — Uppercase Decorator

File: 05_uppercase_decorator.py

Created a decorator that modifies the returned string and converts it into uppercase.

### 06 — Message Decorator

File: 06_message_decorator.py

Created a decorator that displays messages before and after function execution.

### 07 — Logging Decorator

File: 07_logging_decorator.py

Created a simple logging decorator that displays a message whenever a function executes.

### 08 — Calculator Decorator

File: 08_calculator_decorator.py

Used the same decorator with multiple calculator-related functions.

### 09 — Nested Wrapper

File: 09_nested_wrapper.py

Practiced the relationship between the decorator function, wrapper function, and original function.

### 10 — Decorator Challenge

File: 10_decorator_challenge.py

Created a security-check decorator that adds additional security behavior before executing a function.

---

## 🏆 Day 12 Completion

- Topic: Decorators
- Practice Programs: 10/10
- Status: Completed ✅
- Series: 100 Days of Advanced Python

---

## 💭 Final Takeaway

Decorators allow us to add or modify the behavior of functions without changing their original implementation.
