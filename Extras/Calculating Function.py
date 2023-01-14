n = int(input())


def func(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int((n - 1) / 2 - n)


print(func(n))
