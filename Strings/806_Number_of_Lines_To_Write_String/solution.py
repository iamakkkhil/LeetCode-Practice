def numberOfLines(widths, s):
    line_count = 0
    count = 0
    for i in range(len(s)):
        index_to_s = ord(s[i])-97
        width_to_word = widths[index_to_s]
        if (count+width_to_word) <= 100:
            count += width_to_word
        else:
            line_count += 1
            count = 0
            count += width_to_word
        
    print(line_count+1, count)
        

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"
numberOfLines(widths, s)