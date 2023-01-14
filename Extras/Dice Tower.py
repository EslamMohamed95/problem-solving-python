import sys

n = int(input())
face_num = int(input())
for i in range(n):
    x, y = map(int, input().strip().split())
    if x == face_num or x == 7 - face_num or y == face_num or y == 7 - face_num:
        print('NO')
        sys.exit(0)

print('YES')
