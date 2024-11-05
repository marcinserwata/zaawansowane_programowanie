import Zad3.property as prop

class Flat(prop.Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: {self.area}, {self.rooms}, {self.price}, {self.address}, {self.floor}"
