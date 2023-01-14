n, k = map(int, input().strip().split())

pairs = [list(map(int, input().split())) for i in range(n)]
covered = 0
for p in pairs:
    if p[0] == p[1]:
        covered += 1
    else:
        covered += (p[1] - p[0] + 1)

print(k - covered % k if covered % k != 0 else covered % k)
