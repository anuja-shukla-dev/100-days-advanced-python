class Numbers:
    def __init__(self, limit):
        self.start = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.limit:
            value = self.start
            self.start += 1
            return value

        else:
            raise StopIteration

num = Numbers(10)

for n in num:
    print(n,end=" ")