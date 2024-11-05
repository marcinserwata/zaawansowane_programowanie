import Zad3.property as prop

class House(prop.Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House: {self.area}, {self.rooms}, {self.price}, {self.address}, {self.plot}"
