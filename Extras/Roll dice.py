dices = list(map(int, input().strip().split()))[:2]
Y = dices[0]
W = dices[1]
maxRoll = Y if Y > W else W
counts = 0
for i in range(maxRoll,7):
    counts+=1
if counts == 1:
    print("1/6")
elif counts == 2:
    print("1/3")
elif counts == 3:
    print("1/2")
elif counts == 4:
    print("2/3")
elif counts == 5:
    print("5/6")
elif counts == 6:
    print("1/1")
