# GENERATE EXPRESSION THAT GENERATES SQUARES FROM 1 TO 10

squares = (x * x for x in range(1, 11))

for i in squares:
    print(i)

# GENERATE EXPRESSION THAT GENERATES EVEN NUMBERS FROM1 TO 20

even_numbers = (x for x in range(1, 21) if x % 2 == 0)

for i in even_numbers:
    print(i)

# GENERATE EXPRESSION TO FIND LENGTH OF WORDS IN ITERABLE
words = ["Python", "Generator", "Iterator", "Function"]

length = (len(x) for x in words)

for i in length:
    print(i)