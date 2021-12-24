def numSteps(self, s: str) -> int:
    steps = 0

    while len(s) != 1:
        # even odd check
        if s[-1] == "0":
            s = s[:-1]
        else:
            s = bin(int(s, 2) + 1)
            s = s[2:]
        steps += 1

    return steps


if __name__ == "__main__":
    s = "1101"
    print(numSteps(s))