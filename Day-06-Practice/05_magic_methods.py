class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"Title: {self.title} | Price: {self.price}"

    def __add__(self, other):
        return self.price + other.price

    def __eq__(self, other):
        return self.price == other.price

book1 = Book("Attitude is everything", 299)
book2 = Book("The Secret", 300)

print(book1)
print(book2)
print(book1 + book2)
print(book1 == book2)