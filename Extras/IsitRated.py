import sys

rounds = int(input())

inputs = [list(map(int, input().split())) for i in range(rounds)]

before, after = zip(*inputs)
rating = 0

for i in range(rounds):
    if before[i] != after[i]:
        print('rated')
        sys.exit(0)
    if i < rounds-1 and before[i] < before[i + 1]:
        rating = -1

if rating == -1:
    print('unrated')
else:
    print('maybe')
