import sys

n, t = map(int, input().strip().split())
i = 10**(n-1)
if t == 10 and n < 2:
    print(-1)
    sys.exit(0)

while True:
    if len(list(str(i))) == n and i % t == 0:
        print(i)
        sys.exit(0)
    i += 1
