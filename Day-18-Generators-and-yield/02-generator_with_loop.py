# GENERATE NUMBERS FROM 1 TO N
def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

n = int(input("Enter n: "))
gen = generate_numbers(n)
for x in gen:
    print(x)

# GENERATE ODD NUMBERS FROM 1 TO N
def odd_numbers(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            yield i

n = int(input("Enter n: "))
gen = odd_numbers(n)
for x in gen:
    print(x)

# GENERATE MULTIPLES OF GIVEN NUMBER
def multiples(number, count):
    for i in range(1, count + 1):
        yield i * number

num = int(input("Enter number: "))
count = int(input("Enter count: "))
mul = multiples(num, count)
for x in mul:
    print(x)