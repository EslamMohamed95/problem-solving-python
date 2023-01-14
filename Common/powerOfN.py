n = int(input())
if n == 0:
    print(1)
elif n > 0:
    units = [8, 4, 2, 6]
    n = (n - 1) % 4
    print(units[n])
