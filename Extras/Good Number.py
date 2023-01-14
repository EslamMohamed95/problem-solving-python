n, k = map(int, input().strip().split())
num_list = [input() for i in range(n)]
check_num = [str(x) for x in range(k + 1)]
check_num = ''.join(check_num)
counter = 0
for n in num_list:
    n = list(n)
    n = list(set(n))
    n.sort()
    n = ''.join(n)
    
    if check_num in n:
        counter += 1
print(counter)
