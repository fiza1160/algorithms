from typing import Set


def fibonacci(n: int) -> int:
    """
    Returns n-th Fibonacci number
    n must be more than 0, otherwise it raise a ValueError.
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(10)
    55
    >>> fibonacci(-2)
    Traceback (most recent call last):
        ...
    ValueError: n must be more or equal than 0
    """
    if n < 0:
        raise ValueError('n must be more or equal than 0')
    elif n == 0:
        return 0

    fib = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


def count_trajectories(n: int) -> int:
    """
    The Grasshopper is in position 1.
    The Grasshopper may jump to +1, +2 or +3.
    How many possible trajectories does the grasshopper have to get to position n?
    If n<=1, consider that the Grasshopper has 0 possible trajectory.

    >>> count_trajectories(0)
    0
    >>> count_trajectories(1)
    0
    >>> count_trajectories(2)
    1
    >>> count_trajectories(3)
    2
    >>> count_trajectories(4)
    3
    >>> count_trajectories(7)
    20
    >>> count_trajectories(-3)
    0
    """
    if n <= 1:
        return 0

    trajectories = [0, 0, 1, 2, 3] + [0] * (n - 4)

    for i in range(5, n + 1):
        trajectories[i] = trajectories[i - 1] + trajectories[i - 2] + trajectories[i - 3]

    return trajectories[n]


def count_trajectories_with_forbidden_cells(n: int, forbidden_cells: Set[int]) -> int:
    """
    The Grasshopper is in position 1.
    The Grasshopper may jump to +1, +2 or +3.
    The function receives a set of numbers of cells that cannot be jumped.
    How many possible trajectories does the grasshopper have to get to position n?
    If n<=1, consider that the Grasshopper has 0 possible trajectory.
    If 1 is forbidden, consider that the Grasshopper has 0 possible trajectory.

    >>> count_trajectories_with_forbidden_cells(0, set())
    0
    >>> count_trajectories_with_forbidden_cells(1, set())
    0
    >>> count_trajectories_with_forbidden_cells(2, set())
    1
    >>> count_trajectories_with_forbidden_cells(3, set())
    2
    >>> count_trajectories_with_forbidden_cells(4, set())
    3
    >>> count_trajectories_with_forbidden_cells(4, {2})
    2
    >>> count_trajectories_with_forbidden_cells(4, {3})
    2
    >>> count_trajectories_with_forbidden_cells(4, {4})
    0
    >>> count_trajectories_with_forbidden_cells(9, {2,6,7})
    3
    >>> count_trajectories_with_forbidden_cells(12, {3,6,7,10})
    9
    >>> count_trajectories_with_forbidden_cells(8, {5})
    13
    >>> count_trajectories_with_forbidden_cells(8, {1})
    0
    >>> count_trajectories_with_forbidden_cells(-3, set())
    0
    """
    if n <= 1 or 1 in forbidden_cells:
        return 0

    trajectories = [0] * 5
    for i in range(2, 5):
        if i not in forbidden_cells:
            for k in range(i-1, 0, -1):
                if k not in forbidden_cells:
                    trajectories[i] = trajectories[k]+1
                    break

    trajectories += [0] * (n - 4)

    for i in range(5, n + 1):
        if i not in forbidden_cells:
            trajectories[i] = trajectories[i - 1] + trajectories[i - 2] + trajectories[i - 3]

    return trajectories[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
