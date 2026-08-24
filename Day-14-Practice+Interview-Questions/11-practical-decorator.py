def check_positive(func):
    def wrapper(*args, **kwargs):
        if args[0] > 0:
            result = func(*args, **kwargs)
            return result
        else:
            return "Number should be positive"

    return wrapper

@check_positive
def sqaure(n):
    return n*n

n = int(input("Enter n: "))
print(sqaure(n))