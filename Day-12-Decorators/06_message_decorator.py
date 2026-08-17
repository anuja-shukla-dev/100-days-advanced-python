def show_message(func):
    def wrapper():
        print("--- Function Started ---")
        func()
        print("--- Function Finished ---")

    return wrapper

@show_message
def study():
    print("Studying advanced python")

study()