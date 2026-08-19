# Day 13 - Decorators with Arguments

## Topics Covered

- Understanding decorators with arguments
- Three-level decorator structure
- Passing arguments to decorators
- Using `*args` and `**kwargs` inside wrappers
- Returning values from decorated functions
- Repeating function execution using decorators
- Adding prefixes/logging using decorators
- Role-based access using decorators
- Validating function arguments
- Retrying failed function execution using decorators
- Using `try` and `except` inside decorators

## Practice Programs

1. `01_greeting_decorator.py`
   - Created a decorator that accepts a greeting as an argument.

2. `02_repeat_decorator.py`
   - Created a decorator that executes a function multiple times.

3. `03_prefix_decorator.py`
   - Created a decorator that adds a prefix before function execution.

4. `04_permission_decorator.py`
   - Created a role-based permission decorator.

5. `05_logging_decorator.py`
   - Created a decorator that logs function execution before and after the function runs.

6. `06_validate_arguments.py`
   - Created a decorator to validate positive numerical arguments.

7. `07_retry_decorator.py`
   - Created a retry decorator that attempts a failed function multiple times.

## Key Concept

A decorator with arguments generally follows this structure:

    def decorator_with_arguments(value):
        def decorator(func):
            def wrapper(*args, **kwargs):
                # decorator logic
                return func(*args, **kwargs)

            return wrapper
        return decorator

## Important Learning

- A normal decorator takes the function directly.
- A decorator with arguments requires an additional outer function.
- `*args` stores positional arguments as a tuple.
- `**kwargs` stores keyword arguments as a dictionary.
- `return func(*args, **kwargs)` preserves the return value of the original function.
- Code placed before `func()` runs before the decorated function.
- Code placed after `func()` runs after the decorated function.
- A `return` inside a loop immediately stops the loop.
- In a retry decorator, successful execution should return immediately, while an exception allows the loop to continue.

