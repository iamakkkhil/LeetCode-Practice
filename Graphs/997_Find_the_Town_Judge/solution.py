def findJudge(self, n: int, trust: List[List[int]]) -> int:
    if n==1:
        return 1
    
    people = []
    judge = []
    for group in trust:
        people.append(group[0])
        judge.append(group[1])
        
    judge_Set = set(judge)
    for i in judge_Set:
        if (i not in people) and (judge.count(i)==n-1):
            return i
    return -1
        