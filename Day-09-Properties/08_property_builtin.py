class Product:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price

    price = property(get_price, set_price)


product = Product(500)

print(product.price)

product.price = 750

print(product.price)