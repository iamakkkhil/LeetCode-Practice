def LCS(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    if X[m - 1] == Y[n - 1]:
        return 1 + LCS(X, Y, m - 1, n - 1)
    else:
        return max(LCS(X, Y, m, n - 1), LCS(X, Y, m - 1, n))


def kPalindrome(str, n, k):
    X = str
    Y = X[::-1]
    lenMaxpalindrome = LCS(X, Y, len(X), len(Y))
    if n - lenMaxpalindrome <= k:
        return True
    return False


X = "abcdecba"
print(kPalindrome("abcdecba", len(X), 4))
