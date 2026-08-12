class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return f"Area: {3.14 * self._radius * self._radius}"

circle = Circle(4)
print(circle.area)