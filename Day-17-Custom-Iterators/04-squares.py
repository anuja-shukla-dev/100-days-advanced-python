class Squares:
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

sq = Squares(5)

for x in sq:
    print(x,end=" ")