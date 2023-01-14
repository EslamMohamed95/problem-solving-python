n, k = list(map(int, input().strip().split()))

if k <= (n + 1) / 2:

    print(2 * k - 1)
else:

    k -= int(((n + 1) / 2))
    print(2 * k)
