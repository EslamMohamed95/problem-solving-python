from collections import deque


def has_path(graph, src, dst):
    queue = deque([src])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

has_path(graph, 'f', 'k')  # True

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

has_path(graph, 'f', 'j')  # False

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

has_path(graph, 'i', 'h')  # True
