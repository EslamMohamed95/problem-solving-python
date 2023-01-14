while True:
    try:
        x = int(input())
    except EOFError:
        break
    y = int(input())
    print(x * y)