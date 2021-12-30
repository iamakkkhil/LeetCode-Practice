def fib(self, n: int) -> int:
    storage = [-1] * 31
    storage[0], storage[1] = 0, 1

    if n == 0:
        return 0
    elif n == 1:
        return 1

    for i in range(2, n + 1):
        storage[i] = storage[i - 1] + storage[i - 2]

    return storage[n]


if __name__ == "__main__":
    print(fib(6))
