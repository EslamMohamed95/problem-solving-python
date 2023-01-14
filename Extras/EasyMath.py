count = int(input())

for i in range(count):
    n, m, a, d = list(map(int, input().strip().split()))[:4]
    nc = 0
    for j in range(n,m+1):
        if j%a and j%(a + d) and j%(a + 2*d) and j%(a + 3*d) and j%(a + 4*d)!=0:
            nc += 1
    print(nc)


