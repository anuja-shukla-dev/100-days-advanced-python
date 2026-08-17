def decorator(func):
    def wrapper():
        print("Wrapper started")
        func()
        print("Wrapper ended")
    return wrapper

@decorator
def python():
    print("Learning python")

python()