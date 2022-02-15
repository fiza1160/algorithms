from typing import List


class Heap:
    """
    >>> heap = Heap()
    >>> heap.values
    []
    >>> heap.size
    0
    >>> heap.extract_min()

    >>> heap.insert(5)
    >>> heap.insert(2)
    >>> heap.insert(3)
    >>> heap.insert(6)
    >>> heap.insert(7)
    >>> heap.insert(1)
    >>> heap.values
    [1, 5, 2, 6, 7, 3]
    >>> heap.size
    6
    >>> heap.extract_min()
    1
    >>> heap.values
    [2, 5, 3, 6, 7]
    >>> heap.size
    5
    """

    def __init__(self):
        self.values = []
        self.size = 0

    def _sift_up(self, ind: int):
        while ind != 0 and self.values[(ind - 1) // 2] > self.values[ind]:
            self.values[(ind - 1) // 2], self.values[ind] = self.values[ind], self.values[(ind - 1) // 2]
            ind = (ind - 1) // 2

    def _sift_down(self, ind: int):
        first_child_ind = ind * 2 + 1
        second_child_ind = ind * 2 + 2

        while first_child_ind < self.size:
            if (second_child_ind < self.size
                    and self.values[second_child_ind] < self.values[ind]
                    and self.values[second_child_ind] < self.values[first_child_ind]):
                self.values[second_child_ind], self.values[ind] = self.values[ind], self.values[second_child_ind]
                ind = second_child_ind
            elif self.values[first_child_ind] < self.values[ind]:
                self.values[first_child_ind], self.values[ind] = self.values[ind], self.values[first_child_ind]
                ind = first_child_ind
            else:
                break

    def insert(self, x: int):
        self.values.append(x)
        self.size += 1
        self._sift_up(self.size - 1)

    def extract_min(self):
        if self.size:
            tmp = self.values[0]
            self.values[0] = self.values[-1]
            self.values.pop()
            self.size -= 1
            self._sift_down(0)

            return tmp


def heap_sort(array: List[int]) -> List[int]:
    """
    Returns a new list with sorted items.
    For an empty list it returns an empty list.

    >>> heap_sort([5,8,-6,3,2,1,0])
    [-6, 0, 1, 2, 3, 5, 8]
    >>> heap_sort([])
    []
    >>> heap_sort([1,1,1,1])
    [1, 1, 1, 1]
    """
    heap = Heap()
    for elem in array:
        heap.insert(elem)

    res = []
    while heap.size:
        res.append(heap.extract_min())

    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
