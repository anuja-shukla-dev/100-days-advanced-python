class Calculator:
    @staticmethod
    def is_even(number):
        if number %2 == 0:
            return True
        else:
            return False

n = int(input("Enter a number: "))
print(Calculator.is_even(n))
