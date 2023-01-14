import sys

n, m = map(int, input().strip().split())
picture = [list(map(str, input().split())) for _ in range(n)]
result = ''

for i in range(n):
    for j in range(m):
        if picture[i][j] in ['W', 'B', 'G']:
            result = '#Black&White'
        else:
            result = '#Color'
            print(result)
            sys.exit(0)
print(result)
