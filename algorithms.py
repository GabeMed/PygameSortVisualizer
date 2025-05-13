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
                    # grava o par …
                    self.swappedIndexes.append((j, j + 1))
                    # … e já faz a troca de verdade
                    self.array[j], self.array[j + 1] = (
                        self.array[j + 1],
                        self.array[j],
                    )
                    swapped = True
            if not swapped:  # early-exit correto agora
                break
