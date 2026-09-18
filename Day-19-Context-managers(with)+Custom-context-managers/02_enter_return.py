class Demo():
    def __enter__(self):

        return "Hello from context manager"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Goodbye")

with Demo() as message:
    print(message)