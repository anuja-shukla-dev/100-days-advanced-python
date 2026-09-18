# 📘 Day 19 — Context Managers (`with`) + Custom Context Managers

## 📌 Overview

Day 19 focused on **Context Managers in Python** and the `with` statement.

Context managers are used to manage resources or perform setup and cleanup operations automatically.

---

## 🎯 Topics Covered

- Context managers
- `with` statement
- `__enter__()`
- `__exit__()`
- Returning values from `__enter__()`
- Exception handling inside context managers
- `exc_type`, `exc_value`, and `traceback`
- Suppressing exceptions with `return True`
- Custom class-based context managers
- File management using context managers
- Timer context manager
- `contextlib.contextmanager`
- `yield` as the context boundary

---

## 1. 🔹 The `with` Statement

The `with` statement is used to work with context managers.

Example:

    with Demo():
        print("Inside the context")

It automatically handles entering and leaving the context.

---

## 2. 🔹 `__enter__()`

`__enter__()` runs when the `with` block starts.

Example:

    class Demo:
        def __enter__(self):
            print("Entering the context")

---

## 3. 🔹 `__exit__()`

`__exit__()` runs when the `with` block finishes.

Example:

    class Demo:
        def __enter__(self):
            print("Entering")

        def __exit__(self, exc_type, exc_value, traceback):
            print("Leaving")

---

## 4. 🔹 `as` with `__enter__()`

The value returned by `__enter__()` is assigned to the variable after `as`.

Example:

    class Demo:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            print("Goodbye")

    with Demo() as message:
        print(message)

The important idea is:

    as variable ← value returned by __enter__()

---

## 5. 🔹 Exception Information

`__exit__()` receives information about an exception if one occurs.

    def __exit__(self, exc_type, exc_value, traceback):
        ...

### `exc_type`

Contains the exception type.

Example:

    ValueError

### `exc_value`

Contains the actual exception object.

Example:

    ValueError("Something went wrong")

### `traceback`

Contains traceback information about where the exception occurred.

If no exception occurs, all three values are `None`.

---

## 6. 🔹 Detecting Exceptions

A context manager can check whether an exception occurred.

Example:

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("No exception occurred")
        else:
            print("Exception occurred")

---

## 7. 🔹 Suppressing Exceptions

Returning `True` from `__exit__()` tells Python that the exception has been handled.

Example:

    class SuppressValueError:
        def __enter__(self):
            print("Hello")

        def __exit__(self, exc_type, exc_value, traceback):
            print("Ended")
            return True

    with SuppressValueError():
        raise ValueError("Invalid value")

    print("Program continues")

Because `__exit__()` returns `True`, the exception does not propagate outside the `with` block.

---

## 8. 🔹 Custom File Manager

A custom context manager can manage a file resource.

Important concept:

    self.file → filename
    self.f    → opened file object

The opened file object must be stored on the object so that `__exit__()` can close it.

Example structure:

    class FileManager:
        def __init__(self, file):
            self.file = file

        def __enter__(self):
            self.f = open(self.file, "w")
            return self.f

        def __exit__(self, exc_type, exc_value, traceback):
            self.f.close()

This demonstrates how `self` allows information created in `__enter__()` to be accessed later in `__exit__()`.

---

## 9. 🔹 Timer Context Manager

A context manager can also measure how long a block of code takes.

Example:

    import time

    class Timer:
        def __enter__(self):
            self.start = time.time()

        def __exit__(self, exc_type, exc_value, traceback):
            end = time.time()
            print("Time taken:", end - self.start)

    with Timer():
        time.sleep(3)

The timer starts before the `with` block and calculates the elapsed time after the block finishes.

---

## 10. 🔹 `contextlib.contextmanager`

Python provides a simpler way to create context managers using:

    from contextlib import contextmanager

Example:

    @contextmanager
    def demo():
        print("Entering")
        yield
        print("Leaving")

    with demo():
        print("Inside")

The structure is:

    code before yield → enter/setup
    yield             → context boundary
    code after yield  → exit/cleanup

---

## 11. 🔹 Timer Using `contextmanager`

The same timer idea can be implemented using `@contextmanager`.

Example:

    from contextlib import contextmanager
    import time

    @contextmanager
    def timer():
        start = time.time()
        yield
        end = time.time()
        print("Time taken:", end - start)

    with timer():
        time.sleep(3)

---

## 📂 Files Created

    Day-19-Context-managers(with)+Custom-context-managers/
    │
    ├── 01_basic_context_manager.py
    ├── 02_enter_return.py
    ├── 03_exit_parameters.py
    ├── 04_exception_detector.py
    ├── 05_suppress_exception.py
    ├── 06_file_manager.py
    ├── 07_timer_context_manager.py
    ├── 08_contextlib_basic.py
    ├── 09_contextlib_timer.py
    ├── 10_temporary_message.py
    └── data.txt

---

## 🧠 Key Takeaways

- Context managers manage setup and cleanup automatically.
- The `with` statement works with context managers.
- `__enter__()` runs at the beginning of the context.
- `__exit__()` runs when the context finishes.
- `__enter__()` can return a value for use with `as`.
- `__exit__()` receives exception information.
- Returning `True` from `__exit__()` suppresses an exception.
- Context managers are useful for files, timers, database connections, locks, and other resources.
- `@contextmanager` from `contextlib` provides a simpler way to create context managers.
- With `@contextmanager`, code before `yield` represents setup and code after `yield` represents cleanup.

---

## 🚀 Day 19 Completed

Learned both **class-based custom context managers** and the **`@contextmanager` approach**, along with exception handling, resource management, and practical file/timer examples.