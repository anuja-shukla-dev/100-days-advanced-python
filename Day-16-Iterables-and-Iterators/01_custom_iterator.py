class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= 1:
            value = self.start
            self.start -= 1
            return value

        else:
            raise StopIteration

counter = CountDown(5)

for num in counter:
    print(num)