def longestEvenWord(sentence):
    # splitting the words into list present in the sentance
    single_words = sentence.split()

    # list to store even word
    even_word_list = []
    longest_even_word, max_even_length = "", 0

    # iterating word by word
    for word in single_words:
        # only checking the even words and len of even word 
        # greater than max length of even word present.
        if len(word) % 2 == 0 and len(word) > max_even_length:
            max_even_length = len(word)
            longest_even_word = word

    print("ans: ", longest_even_word)


longestEvenWord("It is a pleasant day today")
