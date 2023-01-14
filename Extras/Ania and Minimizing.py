import sys

n, k = map(int, input().strip().split())
S = list(input())
chrs = 0

if len(S) == 1:

    if k != 0:
        S = '0'
        print(S)
        sys.exit(0)

if k == n and S[0] == '1' and k != 1:
    k = k - 1
for i in range(n):
    if chrs >= k:
        break
    if S[i] == '1' and i == 0:
        continue
    elif S[i] == '0':
        continue
    else:
        if S[i] != '1' and i == 0:
            S[i] = '1'
            chrs += 1

        else:
            S[i] = '0'
            chrs += 1
print("".join(S))
