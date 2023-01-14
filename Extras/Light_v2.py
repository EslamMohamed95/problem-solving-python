mydata = []
inp = -1
while inp != 0:
    inp = int(input())
    if inp != 0:
        mydata.append(inp)
for b in mydata:
    bulbs = [[j, 0] for j in range(b)]
    for i in range(1, len(bulbs) + 1):
        for j in range(1, len(bulbs) + 1):
            if j % i == 0:
                bulbs[j - 1][1] = 1 - bulbs[j - 1][1]
    if bulbs[-1][1] == 1:
        print('yes')
    else:
        print('no')
