def counter():
    count = 0
    def c():
        nonlocal count
        count += 1
        return count
    return c

c = counter()

print(c())
print(c())
print(c())