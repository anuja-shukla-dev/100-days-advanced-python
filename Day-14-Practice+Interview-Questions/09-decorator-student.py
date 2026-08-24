def show_arguments(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper

@show_arguments
def student(name, age):
    print(name, age)

student("Anuja", 100)