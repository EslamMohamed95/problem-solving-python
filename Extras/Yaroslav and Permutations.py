import sys

n = int(input())
arr = list(map(int, input().strip().split()))[:n]
Cs = []*len(set(arr))
for i in range(n):
    C = 0
    for j in range(n):
        if arr[i] == arr[j]:
            C += 1
    Cs.append(C)
if n >= 2*max(Cs) - 1:
    print('YES')
else:
    print('NO')
