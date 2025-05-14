class Algorithms:
    def __init__(self, array: list[int]):
        self.array = array  # cópia será passada de fora
        self.swappedIndexes: list[tuple[int, int]] = []

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self._swap(j, j + 1)
                    swapped = True
            if not swapped:
                break

    def _swap(self, i: int, j: int):
        # Add the swap to the list of swapped indexes
        self.swappedIndexes.append((i, j))
        # Perform the swap
        self.array[i], self.array[j] = self.array[j], self.array[i]
