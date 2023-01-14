from collections import deque

global graph


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


def has_path(graph, src, dst):
    queue = deque([src])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


def shortest_path(graph, nodeA, nodeB):
    visited = {nodeA}
    queue = deque([(nodeA, 0)])

    while queue:
        node, distance = queue.popleft()
        if node == nodeB:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))


def distanceToGateway(graph, gateways):
    queue = deque([])
    distance_to_gateway = []
    vis = set()

    for p in graph:
        distance_to_gateway.insert(p, 10000000000)
    for g in gateways:
        distance_to_gateway[g] = 0
        queue.append(g)

    while queue:
        source = queue.popleft()
        for node in graph:
            if has_path(graph, source, node) and (node not in vis):
                vis.add(node)
                node_dist = shortest_path(graph, node, source)
                if node_dist < distance_to_gateway[node]:
                    distance_to_gateway[node] = node_dist
                    queue.append(node)

    return distance_to_gateway


def countGateways(graph, gateways):
    connected_gateways = [0] * len(graph)
    visited = set([])
    critical_nodes = []
    for node in graph:
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in gateways:
                    connected_gateways[node] += 1
            if connected_gateways[node] >= 2:
                critical_nodes.append(node)
    return connected_gateways, critical_nodes


def cutLink(u, v):  # remove a link and print
    graph[v].remove(u)
    graph[u].remove(v)


def edges_to_sever(source, graph):
    # dist_closest_gw = distanceToGateway(graph, gateways)
    connected_gateways, critical_nodes = countGateways(graph, gateways)

    if connected_gateways[source] == 1:
        for neighbor in graph[source]:
            if neighbor in gateways and has_path(graph, source, neighbor):
                return source, neighbor
            elif not has_path(graph, source, neighbor):
                for g in critical_nodes:
                    if len(graph[g]) >= 3:
                        for neighbor in graph[g]:
                            if neighbor in gateways:
                                return g, neighbor
                    elif len(graph[g]) >= 2:
                        for neighbor in graph[g]:
                            if neighbor in gateways:
                                return g, neighbor
                    else:
                        return graph[gateways[0]][0], gateways[0]
    else:
        if len(critical_nodes) > 0:
            for g in critical_nodes:
                if len(graph[g]) >= 3:
                    for neighbor in graph[g]:
                        if neighbor in gateways:
                            return g, neighbor
                elif len(graph[g]) >= 2:
                    for neighbor in graph[g]:
                        if neighbor in gateways:
                            return g, neighbor
        else:
            for i in range(len(gateways)):
                if len(graph[gateways[i]]) > 0:
                    return graph[gateways[i]][0], gateways[i]


# --------------------- Main Program to Run --------------------- #

n, l, e = [int(i) for i in input().split()]
edges = []
gateways = []
visited = set()
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    edges.append((n1, n2))
graph = build_graph(edges)

for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways.append(ei)

while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    node, adjacent = edges_to_sever(si, graph)
    cutLink(node, adjacent)
    print(node, adjacent)
