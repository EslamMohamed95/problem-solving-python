import string

n, k = list(map(int, input().strip().split()))[:2]

letters = list(string.ascii_lowercase)
password = ''
for i in range(n):
    password += ''.join(letters[i % k])

print(password)
