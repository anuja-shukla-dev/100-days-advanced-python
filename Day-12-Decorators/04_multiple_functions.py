def simple_decorator(func):
    def wrapper():
        print("Decorator executed")
        func()

    return wrapper

@simple_decorator
def login():
    print("User logged in")

@simple_decorator
def logout():
    print("User logged out")

@simple_decorator
def dashboard():
    print("Dashboard opened")

login()
logout()
dashboard()