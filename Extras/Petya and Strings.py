str1 = input().lower()
str2 = input().lower()

A = [ord(x) for x in str1]
B = [ord(x) for x in str2]

for i in range(len(A)):
    if A[i] < B[i]:
        print(-1)
        break
    elif A[i] > B[i]:
        print(1)
        break
    if i == len(A) - 1:
        print(0)