class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __add__(self, other):
        return self.price + other.price

book1 = Book("Python Programming", 210)
book2 = Book("Let's C++", 300)

print(book1 + book2)