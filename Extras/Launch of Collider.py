n = int(input())
dirs = list(input())
particles = list(map(int, input().strip().split()))
ans = 100000000000
for i in range(n - 1):
    if dirs[i] == 'R' and dirs[i + 1] == 'L':
        time = int((particles[i + 1] - particles[i]) / 2)
        ans = time if time < ans else ans

if ans == 100000000000:
    print(-1)
else:
    print(ans)
