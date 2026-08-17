def decorator(func):
    def wrapper():
        print("Decorator is executing")
        func()
    return wrapper

@decorator
def greet():
    print("Hello, python!")

greet()