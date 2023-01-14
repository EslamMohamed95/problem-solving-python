import math

n, t, k, d = list(map(int, input().strip().split()))[:4]

x = math.ceil(d / t)
n = n - (x * k)
if n > 0:
    if d % t != 0:
        print('YES')
    else:
        if n > k:
            print('YES')
        else:
            print('NO')
else:
    print('NO')
