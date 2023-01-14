import math

n, m = map(int, input().strip().split())


def isPrime(N):
    if N <= 1:
        return False
    if N <= 3:
        return True

    if N % 2 == 0 or N % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(N) + 1), 6):
        if N % i == 0 or N % (i + 2) == 0:
            return False

    return True


def nextPrime(N):
    if N <= 1:
        return 2
    prime = N
    found = False
    while not found:
        prime = prime + 1

        if isPrime(prime):
            found = True

    return prime


if nextPrime(n) == m:
    print('YES')
else:
    print('NO')
