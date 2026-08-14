def power(n):
    def square(x):
        return n**x
    return square

square = power(2)
print(square(5))