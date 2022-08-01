"""
https://leetcode.com/problems/unique-paths/
"""

def uniquePaths(self, m: int, n: int, memo=dict()) -> int:
    key_1 = f"{m},{n}"
    key_2 = f"{n},{m}"

    if key_1 in memo: return memo[key_1]
    if key_2 in memo: return memo[key_2]

    if m==1 and n==1: return 1
    if m==0 or n==0: return 0


    s1 = uniquePaths(m-1, n, memo)
    s2 = uniquePaths(m, n-1, memo)

    memo[f"{m-1},{n}"] = s1
    memo[f"{n},{m-1}"] = s1

    memo[f"{m},{n-1}"] = s2
    memo[f"{n-1},{m}"] = s2

    memo[key_1] = s1+s2
    memo[key_2] = s1+s2

    return memo[key_1]
  
