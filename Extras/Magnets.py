from itertools import chain

MagNo = int(input())
Magnets = [list(map(str, input().split(','))) for i in range(MagNo)]
Magnets = list(chain.from_iterable(Magnets))
groups = 1


for i in range(0,MagNo-1):
    if Magnets[i]!=Magnets[i+1]:
        groups +=1

print(groups)