# Day 9 — Properties in Python

## 📌 Topic
Properties in Python

## 📚 Concepts Covered
- `@property` decorator
- Getters
- Setters using `@property_name.setter`
- Deleters using `@property_name.deleter`
- Read-only properties
- Property-based validation
- Properties vs normal methods
- `property()` built-in function
- Internal attributes using `_attribute`
- Properties and encapsulation

## 🔑 Key Understanding

A property allows a method to be accessed like an attribute while still giving control over how the attribute is read, modified, or deleted.

### Basic Property

```python
@property
def value(self):
    return self._value
```

### Setter

```python
@value.setter
def value(self, new_value):
    self._value = new_value
```

### Deleter

```python
@value.deleter
def value(self):
    del self._value
```

### Built-in `property()`

```python
value = property(get_value, set_value)
```

## 🧠 Important Distinction

- `self.value` → accesses the property and triggers its logic.
- `self._value` → stores/accesses the actual internal value.

Using `self.value = value` inside `__init__` allows the setter to perform validation during object creation.

## 💻 Practice Problems

1. Basic property — Student
2. Getter — Person
3. Getter + Setter — Student marks
4. Deleter — User username
5. Read-only property — Circle area
6. Property validation — Employee salary
7. Property vs method — Rectangle area
8. Built-in `property()` — Product price
9. Temperature with validation and Fahrenheit conversion
10. Interview problem — Rectangle with dynamic read-only area

## 🎯 Key Takeaway

Properties provide a clean attribute-like interface while allowing validation, controlled access, and encapsulation behind the scenes.