class Countdown:
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

count = Countdown(10)

for n in count:
    print(n,end=" ")