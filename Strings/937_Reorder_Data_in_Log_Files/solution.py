def myFunc(e):
    return e[1:]


def reorderLogFiles(logs):
    # Splitting the a log by space
    for i, log in enumerate(logs):
        logs[i] = log.split(" ")

    # Seperating words log and digits log
    words_log = []
    digits_log = []
    for i in range(len(logs)):
        if logs[i][1].isnumeric():
            digits_log.append(logs[i])
        else:
            words_log.append(logs[i])

    # Sort words log lexiographically
    words_log.sort()
    words_log.sort(key=myFunc)

    # joining the words again
    for i, word in enumerate(words_log):
        words_log[i] = " ".join(word)

    for i, digit in enumerate(digits_log):
        digits_log[i] = " ".join(digit)

    print(words_log + digits_log)


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
reorderLogFiles(logs)
