l, r = map(int, input().strip().split())

if l % 2 != 0:
    l += 1

if abs(l - r) < 2:
    print(-1)
else:
    print(l, " ", l + 1, " ", l + 2)
