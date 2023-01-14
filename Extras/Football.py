import sys

n = int(input())
matches = []
for i in range(n):
    matches.append(input())

teams = list(set(matches))

if len(teams) < 2:
    print(teams[0])
    sys.exit(0)

if sum(1 for s in matches if teams[0] == s) > sum(1 for s in matches if teams[1] == s):
    print(teams[0])
else:
    print(teams[1])
