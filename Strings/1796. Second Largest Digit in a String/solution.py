def secondHighest(self, s: str) -> int:
    numbers = []
    for i in s:
        if i.isdigit():
            numbers.append(int(i))

    numbers = set(numbers)
    numbers = sorted(numbers)

    return numbers[-2] if len(numbers) >= 2 else -1


if __name__ == "__main__":
    s = "dee12edbbcc45312cbdaa"
    print(secondHighest(s))