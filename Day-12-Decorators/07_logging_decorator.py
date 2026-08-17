def log_function(func):
    def wrapper():
        print("Function is being executed...")
        func()

    return wrapper

@log_function
def calculate():
    print("Calculation completed")

calculate()