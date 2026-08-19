def add_prefix(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix}")
            return func(*args, **kwargs)

        return wrapper
    return decorator

@add_prefix("INFO")
def message():
    return "Program executed successfully"

print(message())