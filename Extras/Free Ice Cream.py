queue_count, icecream_packs = list(map(int, input().strip().split()))[:2]
queue = [list(map(str, input().split())) for i in range(queue_count)]
d_child = 0
for q in queue:

        if q[0] == '-':
            if (icecream_packs - int(q[1])) < 0:
                d_child+=1
            else:
                icecream_packs-= int(q[1])

        if q[0] == '+':
            icecream_packs += int(q[1])

print(icecream_packs,d_child)