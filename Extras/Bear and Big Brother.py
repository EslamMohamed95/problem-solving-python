inp = list(map(int, input().strip().split()))[:2]
L = inp[0]
B = inp[1]
yrs = 0
while L <= B :
        L*=3
        B*=2
        yrs +=1
print(yrs)