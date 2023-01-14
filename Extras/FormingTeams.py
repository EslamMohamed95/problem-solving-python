n, m = map(int, input().strip().split())
graph = [[]*2] * n
vis = [False] * n
cycle = None
ans = 0
cnt = 0


def dfs(cur_node, parent_node, nodes_cnt):
    if vis[cur_node]:
        return 'CYCLE'
    vis[cur_node] = True

    for child_node in graph[cur_node]:
        if child_node != parent_node:
            nodes_cnt += 1
            if dfs(child_node, cur_node, nodes_cnt) == 'CYCLE':
                return 'CYCLE'

    return 'PATH'


for i in range(m):
    x, y = map(int, input().strip().split())
    x -= 1
    y -= 1
    graph[x].append(x)
    graph[y].append(y)

toRemove = 0
for i in range(n):
    if not vis[i]:
        solve = dfs(i, -1, cnt)
        if solve == 'CYCLE':  # if odd cycle remove 1
            toRemove += (cnt % 2 == 1)

# teams must be same size if total odd remove 1
if (n - toRemove) % 2 == 1:
    toRemove += 1

print(toRemove)
