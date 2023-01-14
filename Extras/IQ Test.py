import sys

paper = [list(input()) for i in range(4)]
count = 0
for i in range(3):
    for j in range(3):

        if [paper[0 + i][0 + j], paper[0 + i][1 + j], paper[1 + i][0 + j], paper[1 + i][1 + j]].count('.') == 2 \
                or [paper[0 + i][0 + j], paper[0 + i][1 + j], paper[1 + i][0 + j], paper[1 + i][1 + j]].count('#') == 2:
            continue
        elif [paper[0 + i][0 + j], paper[0 + i][1 + j], paper[1 + i][0 + j], paper[1 + i][1 + j]].count('#') >= 3 \
                or [paper[0 + i][0 + j], paper[0 + i][1 + j], paper[1 + i][0 + j], paper[1 + i][1 + j]].count('.') >= 3:
            print('YES')
            sys.exit(0)

print('NO')
