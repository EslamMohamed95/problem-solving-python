def has_path(graph, src, dst):
    if src == dst:
        return True
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst):
            return True
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
