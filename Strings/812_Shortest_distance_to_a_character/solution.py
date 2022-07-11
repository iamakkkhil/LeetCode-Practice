def shortest_distance(s, c):
    ans = []
    inf = float("inf")
    prev = inf

    # for-loop from start -> end
    for i in range(len(s)):
        if s[i] == c:
            prev = i
        if prev == inf:
            ans.append(inf)
        else:
            ans.append(abs(prev - i))

    # for-loop from end -> start
    prev = inf
    for i in range(len(s) - 1, -1, -1):
        if s[i] == c:
            prev = i
        ans[i] = min(abs(prev - i), ans[i])

    return ans


print(shortest_distance("loveleetcode", "e"))
