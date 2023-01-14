n = int(input())


def dfs(i, j):
    if i < 0 or j < 0 or i == g or j == g:
        return
    if grid[i][j] == '.' or visited[i][j]:
        return
    visited[i][j] = 1
    dfs(i - 1, j)
    dfs(i + 1, j)
    dfs(i, j - 1)
    dfs(i, j + 1)


import itertools
for c in range(n):
    g = int(input())
    grid = [list(input()) for _ in range(g)]
    print()
    visited = [[None] * g] * g
    ships = 0
    for i, j in itertools.product(range(g), range(g)):
        cell = grid[i][j]
        if not visited[i][j] and grid[i][j] == 'x':
            ships += 1
            dfs(i, j)
    print(f"Case {c + 1}: {ships}")
