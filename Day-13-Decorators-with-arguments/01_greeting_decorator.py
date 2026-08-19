def greet_user(greeting):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(greeting)
            func(*args, **kwargs)

        return wrapper
    return decorator


@greet_user("Good morning")
def welcome(name):
    print(f"Welcome {name}")


welcome("Anuja Shukla")
        
