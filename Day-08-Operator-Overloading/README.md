# Day 8 - Operator Overloading in Python

## 📌 Topics Covered

* Introduction to Operator Overloading
* Special (Dunder) Methods
* Arithmetic Operators
* Comparison Operators
* Unary Operators
* String Representation of Objects

---

## 📚 Concepts Learned

### 1. Arithmetic Operator Overloading

Implemented custom behavior for:

* `__add__()` → `+`
* `__sub__()` → `-`
* `__mul__()` → `*`

Examples:

* Adding Book prices
* Adding Point objects
* Vector operations

---

### 2. Comparison Operator Overloading

Implemented:

* `__gt__()` → `>`
* `__eq__()` → `==`

Examples:

* Comparing student marks
* Comparing bank account balances
* Comparing vectors

---

### 3. Unary Operator Overloading

Implemented:

* `__neg__()` → Unary `-`

Example:

* Negative Temperature object

---

### 4. String Representation

Implemented:

* `__str__()`

Examples:

* Product details
* Student information
* Bank account information

---

## 📂 Files

* `01_book_addition.py`
* `02_point_addition.py`
* `03_student_comparison.py`
* `04_student_equality.py`
* `05_temperature_negation.py`
* `06_product_string.py`
* `07_vector_operators.py`
* `08_bank_account_operators.py`

---

## 🧠 Key Learning

Python operators are internally translated into special methods.

Examples:

```python
a + b    -> a.__add__(b)
a - b    -> a.__sub__(b)
a * b    -> a.__mul__(b)
a == b   -> a.__eq__(b)
a > b    -> a.__gt__(b)
-a       -> a.__neg__()
print(a) -> a.__str__()
```

Operator overloading allows custom classes to behave like built-in Python objects, making code more readable and intuitive.

---

## 🚀 Outcome

Completed practical implementation of:

* Arithmetic operators
* Comparison operators
* Unary operators
* Object representation

Strengthened understanding of how Python handles operators internally through dunder methods.
