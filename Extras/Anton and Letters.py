import re

letters = input()
letters = list("".join(re.split("[^a-z]*", letters)))

print(len(set(letters)))
