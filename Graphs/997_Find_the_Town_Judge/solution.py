def findJudge(n, trust):
    # if n==1:
    #     return 1
    
    # people = []
    # judge = []
    # for group in trust:
    #     people.append(group[0])
    #     judge.append(group[1])
        
    # judge_Set = set(judge)
    # for i in judge_Set:
    #     if (i not in people) and (judge.count(i)==n-1):
    #         return i
    # return -1

    arr = [0]*n
    for a,b in trust:
        arr[a-1] -= 1
        arr[b-1] += 1

    if  max(arr) == n - 1: 
        return arr.index(n - 1) + 1
    return -1
    
    
        
n = 3
trust = [[1,3],[2,3],[3,1]]
print(findJudge(n, trust))