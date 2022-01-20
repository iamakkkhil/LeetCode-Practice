def counts(teamA, teamB):
    ans = []
    for i in range(len(teamB)):
        print(i,"--------------")
        # Binary search
        l, r = 0, len(teamA)
        while l < r:
           
            mid = (l + r) // 2
            print(l, r, mid)
            if teamA[mid] > teamB[i]:
                r = mid
            else:
                l = mid + 1

        print("bahar", l, r, mid)
        if l == r:
            lb = l
        else:
            lb = mid

        ans.append(lb)

    print(ans)


teamA = [1, 2, 3]
teamB = [2, 4]

counts(teamA, teamB)
