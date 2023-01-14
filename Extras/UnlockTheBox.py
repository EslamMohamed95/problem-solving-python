import sys

r1, r2 = map(int, input().strip().split())
if r1 == 1 or r2 == 1:
    print(-1)
    sys.exit(0)
c1, c2 = map(int, input().strip().split())
if c1 == 1 or c2 == 1:
    print(-1)
    sys.exit(0)
d1, d2 = map(int, input().strip().split())
if d1 == 1 or d2 == 1:
    print(-1)
    sys.exit(0)
if r1 == r2 == c1 == c2 == d1 == d2:
    print(-1)
    sys.exit(0)

x, a, b, c = 0, 0, 0, 0

for i in range(1, 10):
    x = i
    a = r1 - x
    b = c1 - x
    c = d1 - x
    if x == b or x == a or x == c or a == b or c == b or c == a:
        continue
    if 1 > a or a > 9:
        continue

    if 1 > c or c > 9:
        continue
    if 1 > b or b > 9:
        continue
    if c + b != r2 or a + b != d2 or a + c != c2:
        continue
    else:
        print(x, a)
        print(b, c)
        sys.exit(0)

print(-1)
