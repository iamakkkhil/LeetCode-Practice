def check_satisfy(balanced_count, count_chars):
    for i in count_chars:
        if count_chars[i] > balanced_count:
            return False
    return True


def balancedString(s: str) -> int:
    balanced_count = len(s) / 4
    substring_count = len(s)
    p1, p2 = 0, 0
    count_chars = {"Q": 0, "W": 0, "E": 0, "R": 0}
    for i in s:
        count_chars[i] += 1

    while p2 >= p1 and p2 < len(s) + 1:
        if check_satisfy(balanced_count, count_chars):
            count_chars[s[p1]] += 1
            p1 += 1
            if substring_count > (p2 - p1 + 1):
                substring_count = p2 - p1 + 1

        else:
            if p2 >= len(s):
                return substring_count
            var = s[p2]
            count_chars[var] -= 1
            p2 += 1

    return substring_count


if __name__ == "__main__":
    s = "WQWRQQQW"
    print(balancedString(s))
