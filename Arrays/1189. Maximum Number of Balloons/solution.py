def maxNumberOfBalloons(text):
    countBallon = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
    for char in text:
        if char in countBallon.keys():
            countBallon[char] += 1

    return min(
        countBallon["b"],
        countBallon["a"],
        countBallon["l"] // 2,
        countBallon["o"] // 2,
        countBallon["n"],
    )


if __name__ == "__main__":
    print(maxNumberOfBalloons("ballllooonns"))