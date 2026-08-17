def before_after(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@before_after
def welcome():
    print("Welcome to advanced python!")

welcome()