stone_count = int(input())
stones = input()
stones = list(stones)
rmv_count = 0

for i in range(len(stones)-1):
    if stones[i] == stones[i+1]:
        # stones.pop(stones.index(stones[i]))
        rmv_count+=1
print(rmv_count)