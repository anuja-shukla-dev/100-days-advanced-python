def validate_positive():
    def decorator(func):
        def wrapper(*args, **kwargs):
            if all(x>=0 for x in args):
                return func(*args, **kwargs)
            else:
                return "Invalid arguments"

        return wrapper
    return decorator

@validate_positive()
def multiply(a, b):
    return a * b

print(multiply(-1,3))