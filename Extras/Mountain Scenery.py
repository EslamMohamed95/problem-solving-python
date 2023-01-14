n, k = map(int, input().strip().split())
mountains = list(map(int, input().strip().split()))[:2 * n + 1]
c = 0
for i in range(len(mountains)):
    if mountains[i + 1] < mountains[i]-1 > mountains[i - 1]:
        mountains[i] = mountains[i] - 1
        c += 1
        if c == k:
            break

for m in mountains:
    print(m, end=" ")
