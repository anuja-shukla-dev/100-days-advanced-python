class EvenNumbers:
    def __init__(self, limit):
        self.start = 2
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.limit:
            value = self.start
            self.start += 2
            return value
        else:
            raise StopIteration


num = EvenNumbers(10)

for n in num:
    print(n)