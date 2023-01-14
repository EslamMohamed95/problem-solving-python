import string

letters_count = int(input())
word = input()

alphabet = set(string.ascii_lowercase)

if set(word.lower()) == alphabet:
    print('YES')
else:
    print('NO')
