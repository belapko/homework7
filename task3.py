class Cell():
    def __init__(self, param):
        self.param = int(param)

    def __add__(self, other):
        summa = self.param + other.param
        return summa

    def __sub__(self, other):
        difference = self.param - other.param
        if difference <= 0:
            return "Клетка исчезла"
        else:
            return difference

    def __mul__(self, other):
        mult = self.param * other.param
        return mult

    def __truediv__(self, other):
        divis = self.param // other.param
        return divis

    def make_order(self, line):
        row = ''
        for i in range(int(self.param / line)):
            row += '*' * line + '\n'
        row += '*' * (self.param % line) + '\n'
        return row

cell = Cell(11)
other_cell = Cell(5)

print(cell + other_cell)
# print(cell.__add__(other_cell))

print(cell - other_cell)
# print(cell.__sub__(other_cell))

print(cell * other_cell)
# print(cell.__mul__(other_cell))

print(cell / other_cell)
# print(cell.__truediv__(other_cell))

print(cell.make_order(3))

