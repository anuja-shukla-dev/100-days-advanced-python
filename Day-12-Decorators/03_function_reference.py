def greet():
    print("Welcome, programmer")


def decorator(func):
    def wrapper():
        print("Hey!!")
        func()

    return wrapper

decorated_function = decorator(greet)
decorated_function()