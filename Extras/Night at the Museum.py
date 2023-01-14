import string

word = list(input())
curr_letter = 'a'
next_letter = ''
clc_moves = 0
anticlc_moves = 0
total_moves = 0
letters_wheel = list(string.ascii_lowercase)


def rotateClck(wheel, start, end):
    count = 0
    while wheel[0] != start:
        wheel = (wheel[-1:] + wheel[:-1])  # rotates one step clock-wise
    while wheel[0] != end:
        wheel = (wheel[-1:] + wheel[:-1])  # rotates one step clock-wise
        count += 1
    return wheel, count


def rotateAntiClock(wheel, start, end):
    count = 0
    while wheel[0] != start:
        wheel = (wheel[1:] + wheel[:1])  # rotates one step anti clock-wise
    while wheel[0] != end:
        wheel = (wheel[1:] + wheel[:1])  # rotates one step anti clock-wise
        count += 1
    return wheel, count


for l in word:
    next_letter = l
    letters_wheel, clc_moves = rotateClck(letters_wheel, curr_letter, next_letter)
    if clc_moves > 13:
        letters_wheel, anticlc_moves = rotateAntiClock(letters_wheel, curr_letter, next_letter)
        total_moves += anticlc_moves
    else:
        total_moves += clc_moves

    curr_letter = next_letter

print(total_moves)
