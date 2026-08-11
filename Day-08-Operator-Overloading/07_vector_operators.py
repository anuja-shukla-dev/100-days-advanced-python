class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __add__(self, other):
        return (self.x + other.x , self.y + other.y)
    
    def __sub__(self, other):
        return (self.x - other.x , self.y - other.y)
    
    def __mul__(self, other):
        return (self.x * other , self.y * other)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

vector1 = Vector(9,2)
vector2 = Vector(6,1)

print(vector1 + vector2)
print(vector1 - vector2)
print(vector1 * 3)
print(vector1 == vector2)