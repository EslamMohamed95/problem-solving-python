num = list(input())

for i in range(len(num) - 1, -1, -1):
    if i == 0 and num[i] == str(9):
        continue
    if int(num[i]) > 9 - int(num[i]):
        num[i] = str(9 - int(num[i]))

num = "".join(num)
print(num)
