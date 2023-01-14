from collections import deque


def breadth_first(g, start):
    queue = deque([start])
    while len(queue) > 0:
        current = queue[0]
        print(current)
        queue.popleft()
        for neighbor in g[current]:
            queue.append(neighbor)


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

breadth_first(graph,"a")
