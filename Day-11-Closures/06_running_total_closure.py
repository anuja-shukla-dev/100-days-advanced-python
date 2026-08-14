def total():
    n = 0
    def t(x):
        nonlocal n
        n+=x
        return n
    return t

t = total()
print(t(5))
print(t(4))
print(t(10))
