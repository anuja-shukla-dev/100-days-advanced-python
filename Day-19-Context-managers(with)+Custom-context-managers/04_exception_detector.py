class Demo():
    def __enter__(self):
        print("Hello")

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            print("No exception occurred")
        else:
            print("Exception occurred",exc)


# with Demo():
#     print("Everything is fine")

with Demo():
    raise ValueError("Something went wrong")