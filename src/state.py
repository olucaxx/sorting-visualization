
class SortingArray:
    def __init__(self, size: int):
        self.values = list(range(1, size + 1))
        self.accesses = 0
        self.comparisons = 0
        self.swaps = 0
        
    def clear_stats(self) -> None:
        self.accesses = 0
        self.comparisons = 0
        self.swaps = 0
        
    def compare(self, result: bool) -> bool:
        self.comparisons += 1
        return result
        
    def get(self, idx: int) -> int:
        self.accesses += 1
        return self.values[idx]
        
    def set(self, idx: int, value: int) -> None:
        self.accesses += 1
        self.values[idx] = value

    def swap(self, i: int, j: int) -> None:
        self.swaps += 1
        temp = self.get(i)
        self.set(i, self.get(j))
        self.set(j, temp)
            