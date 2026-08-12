class Temperature:
    def __init__(self, celcius):
        self.celcius = celcius

    @property
    def celcius(self):
        return f"Temp in celcius: {self._celcius}°C"

    @celcius.setter
    def celcius(self, new_temp):
        if new_temp < -273.15:
            raise ValueError("Temperature cannot be below than absolute zero")

        self._celcius = new_temp

    @property
    def fahrenheit(self):
        return f"Temp in fahrenheit: {self._celcius * 9/5 + 32}"


cel = float(input("Enter temperature in celcius: "))
temp = Temperature(cel)
print(temp.celcius)
print(temp.fahrenheit)
temp.celcius = 21
print(temp.fahrenheit)


    
