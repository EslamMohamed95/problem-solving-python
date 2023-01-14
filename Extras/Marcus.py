test_cases = int(input())
steps = list('IEHOVA#')
dirs = [[] for i in range(test_cases)]
for t in range(test_cases):
    n, m = map(int, input().strip().split())
    capstones = [input() for i in range(n)]
    curr_i = -1
    curr_j = capstones[-1].index('@')
    for s in range(len(steps)):

        try:
            if capstones[curr_i - 1][curr_j] == steps[s]:
                dirs[t].append('forth')
                curr_i -= 1
            elif capstones[curr_i][curr_j + 1] == steps[s]:
                dirs[t].append('right')
                curr_j += 1
            elif capstones[curr_i][curr_j - 1] == steps[s]:
                dirs[t].append('left')
                curr_j -= 1
        except IndexError:
            try:

                if capstones[curr_i][curr_j + 1] == steps[s]:
                    dirs[t].append('right')
                    curr_j += 1
                elif capstones[curr_i][curr_j - 1] == steps[s]:
                    dirs[t].append('left')
                    curr_j -= 1
            except IndexError:
                if capstones[curr_i][curr_j - 1] == steps[s]:
                    dirs[t].append('left')
                    curr_j -= 1

for c in range(len(dirs)):
    for dc in dirs[c]:
        print(dc, end=" ")
    print('\n')
