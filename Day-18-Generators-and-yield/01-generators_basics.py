# GENERATE NUMBERS FROM 1 TO 10
def generate_numbers():
    for i in range(1, 11):
        yield i


gen = generate_numbers()
for x in gen:
    print(x)

# GENERATE EVEN NUMBERS FROM 1 TO 20
def even_numbers():
    for i in range(1, 21):
        if i % 2 == 0:
            yield i

even = even_numbers()
for x in even:
    print(x)


# GENERATE SQUARES FROM 1 TO 10
def squares():
    for i in range(1, 11):
        yield i * i

sq = squares()
for x in sq:
    print(x)









