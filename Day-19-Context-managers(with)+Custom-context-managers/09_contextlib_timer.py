from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print("Time taken",end - start)

with timer():
    time.sleep(3)