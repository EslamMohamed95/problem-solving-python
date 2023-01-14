import sys

size = int(input())
paper = [input() for i in range(size)]

digs = []
others = []

if paper[0][0] == paper[0][1]:
    print('NO')
    sys.exit(0)

for i in range(size):
    for j in range(size):
        if i == j or i == size - 1 - j:
            digs.append(paper[i][j])
        else:
            others.append(paper[i][j])
digs = set(digs)
others = set(others)
if (digs != others) and (len(digs) == 1) and (len(others) == 1):
    print('YES')
else:
    print('NO')
