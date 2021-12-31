def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2

    prev = 2
    last_prev = 1
    for i in range(3, n + 1):
        current = prev + last_prev
        last_prev = prev
        prev = current

    return current


if __name__ == "__main__":
    print(climbStairs(8))
