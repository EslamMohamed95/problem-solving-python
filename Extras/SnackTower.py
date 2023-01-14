snacks_count = int(input())
snacks = list(map(int, input().strip().split()))
tower = [False] * (snacks_count + 1)
queue = [0] * snacks_count
s = snacks_count
for i in range(snacks_count):
    tower[snacks[i]] = True
    while tower[s]:
        print(s, end=" ")
        s -= 1
    print()
