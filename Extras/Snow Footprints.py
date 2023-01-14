n = int(input())
steps = list(input())

if 'L' in steps and 'R' in steps:
    s = steps.index('R') + 1
    t = steps.index('L')
elif 'L' in steps and 'R' not in steps:
    s = n - steps[::-1].index('L')
    t = steps.index('L')
elif 'R' in steps and 'L' not in steps:
    s = steps.index('R') + 1
    t = (n - steps[::-1].index('R')) + 1

print(s, t)
