games = int(input())
history_inp = input()
history = list(history_inp)
cA , cD = 0,0
for g in history:
    if g == 'A':
        cA +=1
    elif g == 'D':
        cD +=1


if cA > cD :
    print("Anton")
elif cA < cD:
    print("Danik")
else:
    print("Friendship")