class Demo():
    def __enter__(self):
        print("Hello")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exception type:",exc_type)
        print("Exception value:",exc_value)
        print("Traceback:",traceback)


# with Demo():
#     print("No error")

with Demo():
    raise ValueError("Something went wrong")