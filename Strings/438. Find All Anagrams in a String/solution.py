def findAnagrams(s: str, p: str):
    p_len = len(p)
    p_dict = {}
    output = []

    for i in p:
        if i not in p_dict:
            p_dict[i] = 1
        else:
            p_dict[i] += 1

    s_len = len(s)
    s_dict = {}

    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = 1
        else:
            s_dict[s[i]] += 1

        if i >= p_len:
            char_remove = s[i - p_len]

            s_dict[char_remove] -= 1

            if s_dict[char_remove] == 0:
                del s_dict[char_remove]

        if s_dict == p_dict:
            output.append(i - p_len + 1)

    return output
