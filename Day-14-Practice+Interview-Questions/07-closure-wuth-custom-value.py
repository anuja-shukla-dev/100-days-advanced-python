def power(n):
    def inner(x):
        return x**n

    return inner

square = power(2)
cube = power(3)

print(square(5))
print(cube(3))