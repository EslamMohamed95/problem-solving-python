words_count = int(input())
words = []
for i in range(words_count):
    s = input()
    words.append(s)
str1= ''
for w in words:
    if len(w) >10:
        w = list(w)
        str1 = w[0] + str(len(w) - 2) + w[len(w) - 1]
        print(str1)
    else:
        print(w)
