def depth_first_iterative(g, start):
    stack = [start]
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbor in g[current]:
            stack.append(neighbor)


def depth_first_recursive(g, current):
    print(current)
    for neighbor in graph[current]:
        depth_first_recursive(graph, neighbor)


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}
depth_first_iterative(graph, "a")
depth_first_recursive(graph, "a")
