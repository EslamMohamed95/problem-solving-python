scale = input().split('|')
untouched_weight = list(input())
left_scale = list(scale[0])
right_scale = list(scale[1])

for x in untouched_weight:
    switch = 'r' if len(left_scale) > len(right_scale) else 'l'
    if switch == 'r':
        right_scale.append(x)
    else:
        left_scale.append(x)

print("".join(left_scale) + "|" + "".join(right_scale) if len(left_scale) == len(right_scale) else 'Impossible')
