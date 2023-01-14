matches = int(input())
teams = [list(map(int, input().split())) for i in range(matches)]
home = []
guest = []
count = 0
for i in range(matches):
        home.append(teams[i][0])
        guest.append(teams[i][1])

for i in range(matches):
    for j in range(matches):
        if home [i] == guest[j]:
            count += 1

print(count)