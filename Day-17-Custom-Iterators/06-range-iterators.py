class RangeIterators:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            value = self.start
            self.start += self.step
            return value
        else:
            raise StopIteration

range_iter = RangeIterators(2, 10, 2)

for x in range_iter:
    print(x)