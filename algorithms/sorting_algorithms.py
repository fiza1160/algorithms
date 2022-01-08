from typing import List


def insertion_sort(items: List[int]) -> List[int]:
    """Returns a new list with sorted items.
    For an empty list it returns an empty list.

    >>> insertion_sort([1,8,3,5])
    [1, 3, 5, 8]
    >>> insertion_sort([6,4,9,3,2])
    [2, 3, 4, 6, 9]
    >>> insertion_sort([2,2,2,-3])
    [-3, 2, 2, 2]
    >>> insertion_sort([1])
    [1]
    >>> insertion_sort([])
    []
    """
    res = list(items)

    for n in range(1, len(res)):
        for k in range(n, 0, -1):
            if res[k] < res[k-1]:
                res[k], res[k-1] = res[k-1], res[k]

    return res


def choice_sort(items: List[int]) -> List[int]:
    """Returns a new list with sorted items.
    For an empty list it returns an empty list.

    >>> choice_sort([1,8,3,5])
    [1, 3, 5, 8]
    >>> choice_sort([6,4,9,3,2])
    [2, 3, 4, 6, 9]
    >>> choice_sort([2,2,2,-3])
    [-3, 2, 2, 2]
    >>> choice_sort([1])
    [1]
    >>> choice_sort([])
    []
    """
    res = list(items)

    for pos in range(0, len(res)):
        for k in range(pos+1, len(res)):
            if res[k] < res[pos]:
                res[k], res[pos] = res[pos], res[k]

    return res


def bubble_sort(items: List[int]) -> List[int]:
    """Returns a new list with sorted items.
    For an empty list it returns an empty list.

    >>> bubble_sort([1,8,3,5])
    [1, 3, 5, 8]
    >>> bubble_sort([6,4,9,3,2])
    [2, 3, 4, 6, 9]
    >>> bubble_sort([2,2,2,-3])
    [-3, 2, 2, 2]
    >>> bubble_sort([1])
    [1]
    >>> bubble_sort([])
    []
    """
    res = list(items)
    for bypass in range(1, len(res)):
        for k in range(0, len(res) - bypass):
            if res[k] > res[k + 1]:
                res[k], res[k + 1] = res[k + 1], res[k]

    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
