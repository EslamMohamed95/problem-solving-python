stones = list(input())
instruction = list(input())
pos = 0
for i in range(len(instruction)):
    if stones[pos] == instruction[i]:
        pos+=1

print(pos+1)