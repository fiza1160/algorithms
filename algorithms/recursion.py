from typing import List, Union, Any, Dict


def recursive_factorial(n: int) -> int:
    """
    Calculates the factorial of a natural number.
    If the number is less than 0, it raise a ValueError.

    >>> recursive_factorial(0)
    1
    >>> recursive_factorial(1)
    1
    >>> recursive_factorial(6)
    720
    >>> recursive_factorial(-2)
    Traceback (most recent call last):
        ...
    ValueError: n must be more or equal than 0
    """
    if n < 0:
        raise ValueError('n must be more or equal than 0')

    if n == 0:
        return 1
    return n * recursive_factorial(n - 1)


def recursive_fibonacci(n: int) -> int:
    """
    Returns n-th Fibonacci number
    n must be more than 0, otherwise it raise a ValueError.
    >>> recursive_fibonacci(0)
    0
    >>> recursive_fibonacci(1)
    1
    >>> recursive_fibonacci(2)
    1
    >>> recursive_fibonacci(10)
    55
    >>> recursive_fibonacci(-2)
    Traceback (most recent call last):
        ...
    ValueError: n must be more or equal than 0
    """
    if n < 0:
        raise ValueError('n must be more or equal than 0')

    if n == 0:
        return 0
    elif n == 1:
        return 1

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def recursive_fibonacci_cache(
        n: int
) -> int:
    """
    Returns n-th Fibonacci number
    n must be more than 0, otherwise it raise a ValueError.
    >>> recursive_fibonacci_cache(0)
    0
    >>> recursive_fibonacci_cache(1)
    1
    >>> recursive_fibonacci_cache(2)
    1
    >>> recursive_fibonacci_cache(10)
    55
    >>> recursive_fibonacci_cache(-2)
    Traceback (most recent call last):
        ...
    ValueError: n must be more or equal than 0
    """
    cache = {}

    def _fib(_n):
        if _n < 0:
            raise ValueError('n must be more or equal than 0')

        if _n == 0:
            return 0
        elif _n == 1:
            return 1

        if _n not in cache:
            if _n - 1 not in cache:
                cache[_n - 1] = _fib(_n - 1)

            if _n - 2 not in cache:
                cache[_n - 2] = _fib(_n - 2)

            cache[_n] = cache[_n - 1] + cache[_n - 2]

        return cache[_n]

    return _fib(n)


def recursive_max(sequence: List[int]) -> Union[int, None]:
    """
    Finds the maximal element in the sequence.
    For an empty sequence returns None.
    >>> recursive_max([-2,5,1,12,-8,3])
    12
    >>> recursive_max([1,2,2,2,2])
    2
    >>> recursive_max([1])
    1
    >>> recursive_max([])
    """
    if not sequence:
        return None

    if len(sequence) == 1:
        return sequence[0]
    else:
        left_max = recursive_max(sequence[:len(sequence) // 2])
        right_max = recursive_max(sequence[len(sequence) // 2:])
        return left_max if left_max > right_max else right_max


def recursive_binary_search(
        sequence: List[int],
        elem: int,
        start: Union[None, int] = None,
        stop: Union[None, int] = None
) -> int:
    """
    Searches for an element in the sequence.
    If the element is in the sequence, it returns the index of the element.
    If there are several identical elements in the sequence, it returns the index of the first one.
    If no element is found - returns -1.
    >>> recursive_binary_search([-3, -2, 1, 4, 7, 9, 12], 1)
    2
    >>> recursive_binary_search([-3, -2, 1, 4, 7, 9, 12], 90)
    -1
    >>> recursive_binary_search([2,2,2,2], 2)
    0
    >>> recursive_binary_search([1,2,2,2], 2)
    1
    >>> recursive_binary_search([1,1,2,2], 2)
    2
    >>> recursive_binary_search([1,1,1,2], 2)
    3
    >>> recursive_binary_search([1], 1)
    0
    >>> recursive_binary_search([], 8)
    -1
    """
    start = start or 0
    stop = stop or len(sequence) - 1

    if (not sequence
            or start > stop):  # element not found
        return -1

    middle = (start + stop) // 2
    if sequence[middle] == elem:
        for ind in range(middle, 0, -1):
            prev_elem = sequence[ind - 1]
            if prev_elem != elem:
                return ind
        return 0  # So the sequence starts with the element

    elif sequence[middle] > elem:
        return recursive_binary_search(sequence, elem, start=start, stop=middle - 1)
    else:  # sequence[middle] < elem
        return recursive_binary_search(sequence, elem, start=middle + 1, stop=stop)


def euclidean_algorithm(a: int, b: int) -> int:
    """
    Finds the greatest common divisor of two natural numbers.
    If n or k is less than or equal to 0, it raise ValueError.
    >>> euclidean_algorithm(6,9)
    3
    >>> euclidean_algorithm(8, 20)
    4
    >>> euclidean_algorithm(19, 17)
    1
    >>> euclidean_algorithm(20, -2)
    Traceback (most recent call last):
        ...
    ValueError: a and b must be more than 0
    >>> euclidean_algorithm(-3, 8)
    Traceback (most recent call last):
        ...
    ValueError: a and b must be more than 0
    """
    if a <= 0 or b <= 0:
        raise ValueError('a and b must be more than 0')

    if a == b:
        return a
    elif a > b:
        return euclidean_algorithm(a - b, b)
    else:  # a<b
        return euclidean_algorithm(a, b - a)


def tower_of_hanoi(
        n: int = 1,
        from_rod: str = 'A',
        to_rod: str = 'B',
        through_road: str = 'C'
) -> str:
    """
    Solving the Hanoi Towers puzzle.
    Returns a string with the sequence of disc changes from rod to rod in the format 'disk_number from_rod->to_rod'
    If n < 0 it raises ValueError
    If n == 0, it returns empty string
    >>> tower_of_hanoi()
    '1 A->B '
    >>> tower_of_hanoi(2)
    '1 A->C 2 A->B 1 C->B '
    >>> tower_of_hanoi(3)
    '1 A->B 2 A->C 1 B->C 3 A->B 1 C->A 2 C->B 1 A->B '
    >>> tower_of_hanoi(0)
    ''
    >>> tower_of_hanoi(-2)
    Traceback (most recent call last):
        ...
    ValueError: n must be more than 0
    """
    if n == 0:
        return ''
    elif n < 0:
        raise ValueError('n must be more than 0')

    if n == 1:
        return f'1 {from_rod}->{to_rod} '
    return (tower_of_hanoi(n - 1, from_rod=from_rod, to_rod=through_road, through_road=to_rod) +
            f'{n} {from_rod}->{to_rod} ' +
            tower_of_hanoi(n - 1, from_rod=through_road, to_rod=to_rod, through_road=from_rod))


def all_permutations(sequence: List[Any]) -> List[Any]:
    """
    Returns a list of all permutations of sequence elements.
    The length of the sequence must be less than or equal to 10 (since the algorithm is factorial).
    If the length of the sequence is greater than 10, it raise a ValueError.
    For an empty sequence it returns an empty list.
    >>> all_permutations([1,2,3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> all_permutations([1])
    [[1]]
    >>> all_permutations([])
    []
    >>> all_permutations([0,1,2,3,4,5,6,7,8,9,10])
    Traceback (most recent call last):
        ...
    ValueError: len(sequence) must be less than or equal to 10
    """
    if not sequence:
        return []
    elif len(sequence) > 10:
        raise ValueError('len(sequence) must be less than or equal to 10')

    if len(sequence) == 1:
        return [sequence]
    else:
        res = []
        for ind, elem in enumerate(sequence):
            permutations = all_permutations(sequence[:ind] + sequence[ind + 1:])
            for permutation in permutations:
                res.append([elem] + permutation)
        return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
