import math

a,b,d = list(map(int, input().strip().split()))[:3]
sizes = list(map(int, input().strip().split()))[:a]
waste =0
count = 0
for o in sizes:
    if o<=b:
        waste+=o
        if waste > d:
            waste = 0
            count += 1

print(count)

