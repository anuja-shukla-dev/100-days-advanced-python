def calculator_log(func):
    def wrapper():
        print("Starting calculation...")
        func()

    return wrapper

@calculator_log
def add():
    print("Addition completed")
    print()

@calculator_log
def subtract():
    print("Subtraction completed")
    print()

@calculator_log
def multiply():
    print("Multiplication completed")
    print()

add()
subtract()
multiply()