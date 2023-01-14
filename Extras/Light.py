import math

mydata = []
inp = -1
while inp != 0:
    inp = int(input())
    if inp != 0:
        mydata.append(inp)
for b in mydata:
    p = int(math.sqrt(b))
    print('yes' if p * p == b else 'no')
