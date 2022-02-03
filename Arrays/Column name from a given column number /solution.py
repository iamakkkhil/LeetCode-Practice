def colName(n):
    ans = ""
    while n > 0:
        rem = n % 26
        if rem == 0:
            ans += "Z"
            n = (n // 26) - 1
        else:
            ans += chr(rem + 64)
            n = n // 26

    return ans[::-1]
