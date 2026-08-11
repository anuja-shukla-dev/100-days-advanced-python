class Temperature:
    def __init__(self, temp):
        self.temp = temp

    def __neg__(self):
        return -self.temp

temp = Temperature(21)
print(-temp)