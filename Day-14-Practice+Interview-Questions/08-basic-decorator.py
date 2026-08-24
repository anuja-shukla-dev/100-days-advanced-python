def logger(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")

    return wrapper

@logger
def greet():
    print("Hey programmer!")

greet()