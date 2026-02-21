
class Array:
    def __init__(self, size):
        self.values = list(range(1, size + 1))

    def operate(self, pos, op):
        if op == "swap" or op == "shift":
            i, j = pos
            self.values[i], self.values[j] = self.values[j], self.values[i]
            