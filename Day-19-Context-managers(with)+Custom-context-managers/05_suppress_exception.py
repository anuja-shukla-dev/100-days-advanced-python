class SuppressValueError():
    def __enter__(self):
        print("Hello")

    def __exit__(self, exc_type, exc, tb):
        print("Ended")

        return True

with SuppressValueError():
    raise ValueError("Invalid value")

print("Program continues")                 