class SquareNumbers:
    def __init__(self, limit):
        self.start = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.limit:
            value = self.start * self.start
            self.start += 1
            return value
        else:
            raise StopIteration


sqaure = SquareNumbers(5)

for n in sqaure:
    print(n)