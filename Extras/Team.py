probs = int(input())
inp = [list(map(int,input().split())) for i in range(probs)]
ans = 0
for p in range(probs):
        if inp[p][0] and inp[p][1] and inp[p][2]:
            ans +=1
        elif (inp[p][1] and inp[p][2] ) or (inp[p][0] and inp[p][1]) or (inp[p][0] and inp[p][2]):
            ans +=1
print(ans)
