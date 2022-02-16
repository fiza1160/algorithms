from collections import deque
from typing import Dict, Set


def dfs(start_vertex: str, graph: Dict[str, Set[str]], used: Set[str]):
    """
    Depth-first search
    If start_vertex not in graph it raises ValueError

    >>> used = set()
    >>> graph = {'A':{'B'} ,'B':{'A', 'C', 'D'} ,'C':{'B', 'D', 'E'} ,'D':{'B', 'C', 'E'} ,'E':{'C', 'D'} }
    >>> dfs('C', graph, used)
    >>> used == {'A', 'B', 'C', 'D', 'E'}
    True
    >>> used = set()
    >>> dfs('C', {'A': set()}, used)
    Traceback (most recent call last):
        ...
    ValueError: vertex C not in graph
    """
    used.add(start_vertex)
    if start_vertex not in graph:
        raise ValueError(f'vertex {start_vertex} not in graph')

    for neighbour in graph[start_vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)


def counting_connected_components(graph: Dict[str, Set[str]]) -> int:
    """
    Returns the number of connected components in the graph.
    Uses a Depth-first search.

    >>> counting_connected_components({'A': {'B', 'C'}, 'B': {'C'},'C': {'A'},'D': {'E'},'E': {},'F': {},})
    3
    >>> counting_connected_components({})
    0
    """

    res = 0
    used = set()
    for vertex in graph:
        if vertex not in used:
            res += 1
            dfs(vertex, graph, used)

    return res


def bfs(start_vertex: str, graph: Dict[str, Set[str]]) -> Dict[str, int]:
    """
    Returns the dictionary with distances from the starting vertex.
    Uses a Breadth-first search.
    If start_vertex not in graph it raises ValueError
    >>> g = {'A':{'B','C','D'},'B':{'A','C','E'},'C':{'A','B','F'},'D':{'A'},'E':{'B','G'},'F':{'C','G'},'G':{'F','E'}}
    >>> bfs('A', g) == {'A':0,'B':1,'C':1,'D':1,'E':2,'F':2,'G':3}
    True
    >>> bfs('G', g) == {'A':3,'B':2,'C':2,'D':4,'E':1,'F':1,'G':0}
    True
    >>> bfs('C', {'A': set()})
    Traceback (most recent call last):
        ...
    ValueError: vertex C not in graph
    """
    if start_vertex not in graph:
        raise ValueError(f'vertex {start_vertex} not in graph')

    res = {start_vertex: 0}
    queue = deque([start_vertex])

    while queue:
        cur_vertex = queue.popleft()
        for neighbor in graph[cur_vertex]:
            if neighbor not in res:
                queue.append(neighbor)
                res[neighbor] = res[cur_vertex] + 1

    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
