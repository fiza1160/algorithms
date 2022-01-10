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
            if res[k] < res[k - 1]:
                res[k], res[k - 1] = res[k - 1], res[k]

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
        for k in range(pos + 1, len(res)):
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


def quicksort(items: List[int]) -> List[int]:
    """Tony Hoare's algorithm.
    Returns a new list with sorted items.
    For an empty list it returns an empty list.

    >>> quicksort([1,8,3,5])
    [1, 3, 5, 8]
    >>> quicksort([6,4,9,3,2])
    [2, 3, 4, 6, 9]
    >>> quicksort([2,2,2,-3])
    [-3, 2, 2, 2]
    >>> quicksort([1])
    [1]
    >>> quicksort([])
    []
    """
    if not items:
        return []

    if len(items) == 1:
        return items
    else:
        anchor = items[0]
        lower_values = []
        higher_values = []
        equal_values = []
        for elem in items:
            if elem < anchor:
                lower_values.append(elem)
            elif elem > anchor:
                higher_values.append(elem)
            else:  # elem == anchor
                equal_values.append(elem)
        return quicksort(lower_values) + equal_values + quicksort(higher_values)


def merge_sort(items: List[int]) -> List[int]:
    """Returns a new list with sorted items.
    For an empty list it returns an empty list.

    >>> merge_sort([1,8,3,5])
    [1, 3, 5, 8]
    >>> merge_sort([6,4,9,3,2])
    [2, 3, 4, 6, 9]
    >>> merge_sort([2,2,2,-3])
    [-3, 2, 2, 2]
    >>> merge_sort([1])
    [1]
    >>> merge_sort([])
    []
    """
    if not items:
        return []

    if len(items) == 1:
        return items
    else:
        middle = len(items)//2
        first_sorted_part = merge_sort(items[:middle])
        second_sorted_part = merge_sort(items[middle:])

        res = []
        ind_1 = ind_2 = 0
        while len(res) < len(items):
            if ind_1 < len(first_sorted_part) and ind_2 < len(second_sorted_part):
                if first_sorted_part[ind_1] < second_sorted_part[ind_2]:
                    res.append(first_sorted_part[ind_1])
                    ind_1 += 1
                else:
                    res.append(second_sorted_part[ind_2])
                    ind_2 += 1

            if ind_1 == len(first_sorted_part):
                res += second_sorted_part[ind_2:]
            if ind_2 == len(second_sorted_part):
                res += first_sorted_part[ind_1:]

        return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
