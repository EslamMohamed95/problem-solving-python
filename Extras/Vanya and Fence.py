inp = list(map(int, input().strip().split()))[:2]
ppl = list(map(int, input().strip().split()))[:inp[0]]
width_total = 0

for i in ppl:
    if i <= inp[1]:
        width_total += 1
    else:
        width_total += 2

print(width_total)