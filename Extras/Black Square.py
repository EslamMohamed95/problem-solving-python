strips_cal = list(map(int, input().strip().split()))[:4]
strips_idx = input()
strips_idx = [int(x) for x in list(strips_idx)]
calories = 0

for i in strips_idx:
    calories += strips_cal[i - 1]

print(calories)
