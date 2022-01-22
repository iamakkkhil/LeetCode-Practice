def minimumDeletions(self, s: str) -> int:
    a, b = s.count("a"), 0
    res = a + b
    for i in s:
        if i == "a":
            a -= 1
        else:
            b += 1
        res = min(res, a + b)

    return res


if __name__ == "__main__":
    s = "aabbabbba"
    print(minimumDeletions(s))