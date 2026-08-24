def greet(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper
    return decorator

@greet(3)
def greet(message):
    print(f"{message}")

greet("Hello")