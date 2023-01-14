matrix = [list(map(int, input().split())) for i in range(5)]
for i in range(1,6):
    for j in range(1,6):
        if matrix[i-1][j-1] == 1:
            print(abs(i - 3) + abs(j - 3))
            break

