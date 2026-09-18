class Demo():
    def __enter__(self):
        print("Entering the context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving the context")

with Demo():
    print("Inside the context")