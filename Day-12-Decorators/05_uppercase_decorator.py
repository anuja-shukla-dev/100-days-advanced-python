def uppercase_decorator(func):
    def wrapper():
        message = func()
        print(message.upper())

    return wrapper


@uppercase_decorator
def greet():
    return "hello, anuja"


greet()