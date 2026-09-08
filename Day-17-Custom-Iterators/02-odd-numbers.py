class OddNumbers:
    def __init__(self, limit):
        self.start = 1
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

odd = OddNumbers(10)
for x in odd:
    print(x,end=" ")