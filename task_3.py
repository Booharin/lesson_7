class MyCage:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return MyCage(self.cells + other.cells)


c_1 = MyCage(4)
print(c_1.cells)

c_2 = MyCage(7)
print(c_2.cells)

c_3 = c_1 + c_2
print(c_3.cells)