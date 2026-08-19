def retry(attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(attempts):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print("Attempt failed")

            return f"Function failed after {attempts} attempts"
        return wrapper
    return decorator

@retry(3)
def unstable_function(a, b):
    if b > 0:
        return a / b
    else:
        raise ZeroDivisionError("Can't divide by zero")


a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(unstable_function(a, b))