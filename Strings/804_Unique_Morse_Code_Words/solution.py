def uniqueMorseRepresentations(words):
    morse_words = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
    ]
    morse_answers = []
    for i in range(len(words)):
        word = ""
        for j in range(len(words[i])):
            word += morse_words[ord(words[i][j]) - 97]
        morse_answers.append(word)

    return len(set(morse_answers))


words = ["gin", "zen", "gig", "msg"]
print(uniqueMorseRepresentations(words))
