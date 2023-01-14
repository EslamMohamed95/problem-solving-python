while True:
    try:
        step, mod = list(map(int, input().strip().split()))[:2]
        seed = [0] * mod
        for i in range(1, mod):
            seed[i] = (seed[i - 1] + step) % mod
        if len(set(seed)) == len(seed):
            print("%10d" % step, "%10d" % mod, "    ", 'Good Choice')
            print('\n')
        elif len(set(seed)) < len(seed):
            print("%10d" % step, "%10d" % mod, "    ", 'Bad Choice')
            print('\n')

    except EOFError:
        break
