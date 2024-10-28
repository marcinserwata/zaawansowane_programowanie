class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property: {self.area}, {self.rooms}, {self.price}, {self.address}"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House: {self.area}, {self.rooms}, {self.price}, {self.address}, {self.plot}"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: {self.area}, {self.rooms}, {self.price}, {self.address}, {self.floor}"

house1 = House(100, 5, 1000000, "Marszalkowska", 500)
flat1 = Flat(50, 2, 500000, "Krakowska", 2)

print(house1)
print(flat1)