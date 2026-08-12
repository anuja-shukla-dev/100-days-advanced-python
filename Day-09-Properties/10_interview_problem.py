class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def length(self):
        return f"Length: {self._length}"
    
    @property
    def width(self):
        return f"Width: {self._width}"

    @length.setter
    def length(self, new_length):
        if new_length < 0:
            raise ValueError("Length cannot be negative")
        self._length = new_length
        
    @width.setter
    def width(self, new_width):
        if new_width < 0:
            raise ValueError("Width cannot be negative")
        self._width = new_width

    @property
    def area(self):
        return f"Area of rectangle: {self._length * self._width}"

len = int(input("Enter length: "))
wid = int(input("Enter width: "))
rec = Rectangle(len, wid)
print(rec.length)
print(rec.width)
print(rec.area)

rec.length = 10
print(rec.area)
