event_count = int(input())
events = list(map(int, input().strip().split()))[:event_count]
recruits = 0
untreated_crimes = 0

for e in events:
    if e == -1:
        if recruits > 0:
            recruits -= 1
        else:
            untreated_crimes += 1
    else:
        recruits += e
print(untreated_crimes)
