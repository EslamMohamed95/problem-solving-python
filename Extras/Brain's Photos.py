import sys

n, m = map(int, input().strip().split())
picture = [list(map(str, input().split())) for i in range(n)]
result = ''

for i in range(n):
    for j in range(m):
        if picture[i][j] == 'W' or picture[i][j] == 'B' or picture[i][j] == 'G' :
            result = '#Black&White'
        else:
            result = '#Color'
            print(result)
            sys.exit(0)
print(result)
