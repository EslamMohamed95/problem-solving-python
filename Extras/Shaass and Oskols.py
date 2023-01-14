wires_count = int(input())
wires = list(map(int, input().strip().split()))[:wires_count]
shooting_count = int(input())
shooting = [list(map(int, input().split())) for i in range(shooting_count)]

for s in shooting:
    if len(wires) < 2:
        wires = [0]

    elif s[0] == 1:
        wires[(s[0] - 1) + 1] += (wires[(s[0] - 1)] - s[1])
        wires[(s[0] - 1)] = 0
    elif s[0] == len(wires):
        wires[(s[0] - 1) - 1] += (s[1] - 1)
        wires[(s[0] - 1)] = 0
    else:
        wires[(s[0] - 1) - 1] += (s[1] - 1)
        wires[(s[0] - 1) + 1] += (wires[(s[0] - 1)] - s[1])
        wires[(s[0] - 1)] = 0

for w in wires:
    print(w)
