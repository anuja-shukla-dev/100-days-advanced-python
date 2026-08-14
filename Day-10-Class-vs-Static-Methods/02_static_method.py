class MathUtils:

    @staticmethod
    def square(n):
        return n*n

    @staticmethod
    def cube(n):
        return n*n*n

    @staticmethod
    def is_even(n):
        if n%2 == 0:
            return True
        else:
            return False

    @staticmethod
    def is_prime(n):
        count = 0
        for i in range(1, n+1):
            if n%i == 0:
                count+=1
        if count == 2:
            return True
        else:
            return False

print("Sqaure",MathUtils.square(2))
print("Cube",MathUtils.cube(4))
print("Even",MathUtils.is_even(5))
print("Prime",MathUtils.is_prime(2))