coins_count = int(input())
coins = list(map(int, input().strip().split()))[:coins_count]
coins.sort(reverse=True)
coins_taken_count = 1
coins_taken_sum = coins[0]
remaining_sum = sum(coins[1:])

for i in range(1,coins_count):

    if coins_taken_sum <= remaining_sum:
        coins_taken_count += 1
        coins_taken_sum += coins[i]
        remaining_sum = sum(coins[i + 1:])
    else:
        break
print(coins_taken_count)
