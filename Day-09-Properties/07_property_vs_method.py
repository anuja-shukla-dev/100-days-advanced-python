class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    # method
    def area(self):
        return f"Area of rectangle: {self._length * self._width}"

    # property
    @property
    def area(self):
        return f"Area of rectangle: {self._length * self._width}"

rec = Rectangle(2,4)
# print(rec.area())       # printing area using method
print(rec.area)         # printing area using property