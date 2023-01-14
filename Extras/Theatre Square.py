n, m, a = map(int, input().strip().split())

x = int(m / a)
y = int(n / a)
if m % a != 0:
    x += 1
if n % a != 0:
    y += 1

print(x * y)
