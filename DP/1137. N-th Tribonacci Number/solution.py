def tribonacci(self, n: int) -> int:
    storage = [-1] * 38
    storage[0], storage[1], storage[2] = 0, 1, 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1

    for i in range(3, n + 1):
        storage[i] = storage[i - 1] + storage[i - 2] + storage[i - 3]

    return storage[n]


if __name__ == "__main__":
    print(tribonacci(6))
