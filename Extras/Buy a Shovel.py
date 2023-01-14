money = list(map(int, input().strip().split()))[:2]
k = 117#money[0]
r = 3 #money[1]
shovels = 1
while (shovels * k) % 10 !=0:
    if (shovels * k) % 10 -r == 0:
        break
    else:
        shovels+=1

print(shovels)

