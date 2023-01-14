from collections import deque


def shortest_path(edges, nodeA, nodeB):
    graph = build_graph(edges)
    visited = set([nodeA])
    queue = deque([(nodeA, 0)])

    while queue:
        node, distance = queue.popleft()
        if node == nodeB:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    return -1


def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)
    return graph

edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [2, 3],
]

print(shortest_path(edges, 0, 3))  # -> 3
