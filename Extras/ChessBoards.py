n = -1
while n != 0:

    n, m, c = list(map(int, input().strip().split()))[:3]
    if n == 0:
        break
    if c == 0:
        print(int((n - 7) * (m - 7) / 2))
    else:
        print(int(((n - 7) * (m - 7) + 1) / 2))
