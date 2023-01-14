stewards_count = int(input())
stewards = list(map(int, input().strip().split()))
supp = 0
minS = min(stewards)
maxS = max(stewards)
for i in stewards:
    if minS < i < maxS:
        supp += 1
print(supp)
