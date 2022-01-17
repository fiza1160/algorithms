from typing import List, Union


def find_k_largest(sequence: List[int], k: int = 1) -> Union[List[int], None]:
    """Returns a sorted list of the k-largest elements in the sequence of natural numbers.
    If k is greater than the length of the sequence, returns the sorted sequence.
    For an empty sequence returns empty list.
    For k<1 returns None

    >>> find_k_largest([1,8,3,5])
    [8]
    >>> find_k_largest([1,8,3,5], 2)
    [8, 5]
    >>> find_k_largest([1,8,3,5], 6)
    [8, 5, 3, 1]
    >>> find_k_largest([1,5,5,5], 2)
    [5, 5]
    >>> find_k_largest([])
    []
    >>> find_k_largest([1,5,5,5], -1)
    """
    if k < 1:
        return None
    if not sequence:
        return []

    maximums = [-1] * k if k < len(sequence) else [-1] * len(sequence)

    for elem in sequence:
        for n in range(len(maximums)):
            if elem > maximums[n]:
                maximums[n], elem = elem, maximums[n]

    return maximums


def most_frequent_element(sequence: List[int]) -> Union[int, None]:
    """
    Returns the most frequent element in the sequence of natural numbers.
    If there are several most frequent elements, it returns the element with the smallest index.
    For an empty sequence returns None.

    >>> most_frequent_element([1,8,3,5,3,5,5])
    5
    >>> most_frequent_element([1,1,5,5,1,5])
    1
    >>> most_frequent_element([])
    """
    if not sequence:
        return None
    frequencies = {}

    for elem in sequence:
        if elem not in frequencies:
            frequencies[elem] = 0
        frequencies[elem] += 1

    most_frequent = None, -1
    for elem, freq in frequencies.items():
        if freq > most_frequent[1]:
            most_frequent = elem, freq

    return most_frequent[0]


def sorting_by_counting(sequence: List[int]) -> List[int]:
    """
    Sorting by counting for a sequence of natural numbers.
    The elements of the sequence must not be less than 0 and not more than 100,
    otherwise it raises a Value Error
    Returns a new list with sorted elements.
    For an empty sequence returns an empty list.

    >>> sorting_by_counting([1,8,3,5,3,5,5,3,7,12,10,2,6])
    [1, 2, 3, 3, 3, 5, 5, 5, 6, 7, 8, 10, 12]
    >>> sorting_by_counting([])
    []
    >>> sorting_by_counting([1,4,800])
    Traceback (most recent call last):
        ...
    ValueError: elements of the sequence must not be less than 0 and not more than 100
    >>> sorting_by_counting([1,-4,3])
    Traceback (most recent call last):
        ...
    ValueError: elements of the sequence must not be less than 0 and not more than 100
    """
    if not sequence:
        return []

    frequencies = [0] * 101  # values of the elements of the sequence can be from 0 to 100, i.e. 101 variants

    for elem in sequence:
        if elem < 0 or elem > 100:
            raise ValueError('elements of the sequence must not be less than 0 and not more than 100')
        frequencies[elem] += 1

    res = []
    for n in range(len(frequencies)):
        elem = frequencies[n]
        for k in range(elem):
            res.append(n)

    return res


def sieve_of_eratosthenes(n: int = 2) -> Union[List[int], None]:
    """
    Returns a list of prime numbers up to and including n.
    For n<2 returns None.

    >>> sieve_of_eratosthenes()
    [2]
    >>> sieve_of_eratosthenes(5)
    [2, 3, 5]
    >>> sieve_of_eratosthenes(16)
    [2, 3, 5, 7, 11, 13]
    >>> sieve_of_eratosthenes(1)
    """
    if n < 2:
        return None

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for k in range(2, n + 1):
        for i in range(k * 2, n + 1, k):
            sieve[i] = False

    res = []
    for number in range(len(sieve)):
        if sieve[number]:
            res.append(number)

    return res


def rotate_right(sequence: List[int]) -> List[int]:
    """
    Shifts the elements in the sequence to the right, so that the last element of the sequence becomes the first.

    >>> rotate_right([1,2,3,4,5])
    [5, 1, 2, 3, 4]
    >>> rotate_right([1])
    [1]
    >>> rotate_right([])
    []
    """
    if len(sequence) <= 1:
        return sequence

    tmp = sequence[-1]
    for n in range(len(sequence) - 1, 0, -1):
        sequence[n] = sequence[n - 1]
    sequence[0] = tmp

    return sequence


def rotate_left(sequence: List[int]) -> List[int]:
    """
    Shifts the elements in the sequence to the left, so that the first element of the sequence becomes the last.

    >>> rotate_left([1,2,3,4,5])
    [2, 3, 4, 5, 1]
    >>> rotate_left([1])
    [1]
    >>> rotate_left([])
    []
    """
    if len(sequence) <= 1:
        return sequence

    tmp = sequence[0]
    for n in range(len(sequence) - 1):
        sequence[n] = sequence[n + 1]
    sequence[-1] = tmp

    return sequence


def reverse_sequence(sequence: List[int]) -> List[int]:
    """
    Replaces the elements in the sequence in reverse order.

    >>> reverse_sequence([1,2,3,4,5])
    [5, 4, 3, 2, 1]
    >>> reverse_sequence([1,0,0,0])
    [0, 0, 0, 1]
    >>> reverse_sequence([1])
    [1]
    >>> reverse_sequence([])
    []
    """
    if len(sequence) <= 1:
        return sequence

    for n in range(len(sequence) // 2):
        sequence[n], sequence[len(sequence) - n - 1] = sequence[len(sequence) - n - 1], sequence[n]

    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()
