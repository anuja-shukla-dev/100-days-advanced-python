import time

class Timer():
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, tb):
        end = time.time()
        time_taken = end - self.start

        print(time_taken)

with Timer():
    print("Welcome")
    time.sleep(5)