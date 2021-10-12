def minDeletionSize(strs):
    count = []
    for length in range(len(strs[0])):
        prev = ord(strs[0][length])
        for i in range(1, len(strs)):
            if prev >  ord(strs[i][length]):
                count.append(length)
            prev = ord(strs[i][length])
            
    return len(set(count))