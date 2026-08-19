def log_function(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level}] Function started")
            result = func(*args, **kwargs)
            print(f"[{level}] Function ended")
            return result

        return wrapper
    return decorator

@log_function("INFO")
def calculate(a, b):
    return a + b

print("Result:",calculate(10,20))