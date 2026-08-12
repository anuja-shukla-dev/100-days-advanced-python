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
- Using properties for encapsulation

## 🔑 Key Understanding

A property allows a method to be accessed like an attribute while still
giving control over how the attribute is read, modified, or deleted.

### Basic Property

```python
@property
def value(self):
    return self._value