def minimumBribes(q):
    bribes = 0

    for i in range(len(q) - 1, -1, -1):
        diff = (q[i] - 1) - i
        if diff > 2:
            print("Too chaotic")
            return

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)
