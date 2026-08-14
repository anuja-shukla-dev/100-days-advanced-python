def outer(x):
    def inner():
        return x

    return inner

func = outer(10)
print(func.__closure__)
print(func.__closure__[0].cell_contents)