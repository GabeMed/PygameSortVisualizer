class Algorithms:
    def __init__(self, array: list[int]):
        self.array = array  # takes the copy of the array
        self.swappedIndexes: list[tuple[int, int]] = []

    def bubble_sort(self):
        """Sort the array using the bubble sort algorithm."""
        n = len(self.array)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self._swap(j, j + 1)
                    swapped = True
            if not swapped:
                break

    def quick_sort(self):
        """Sort the array using the quicksort algorithm."""
        self._quick_sort(0, len(self.array) - 1)

    # --------------------- Internal Helpers ---------------------- #

    def _quick_sort(self, low: int, high: int):
        if low < high:
            p = self._partition(low, high)
            # sort the sub-arrays left & right of the pivot
            self._quick_sort(low, p - 1)
            self._quick_sort(p + 1, high)

    def _partition(self, low: int, high: int) -> int:
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1
                if i != j:
                    self._swap(i, j)  # record + execute swap
        # place pivot between the two partitions
        if i + 1 != high:
            self._swap(i + 1, high)  # swap pivot into place
        return i + 1

    def _swap(self, i: int, j: int):
        # Add the swap to the list of swapped indexes
        self.swappedIndexes.append((i, j))
        # Perform the swap
        self.array[i], self.array[j] = self.array[j], self.array[i]
