from contextlib import contextmanager

@contextmanager
def demo():
    print("Entering")
    yield 
    print("Leaving")

with demo():
    print("Inside")