from typing import List, Any

dir = input()
coded_msg = list(input())
keyboard = list("qwertyuiop[]asdfghjkl;'zxcvbnm,./")


new_word = [keyboard[keyboard.index(coded_msg[i]) - 1] if dir == 'R' else keyboard[keyboard.index(coded_msg[i]) + 1] for
            i in range(len(coded_msg))]
print("".join(new_word))
