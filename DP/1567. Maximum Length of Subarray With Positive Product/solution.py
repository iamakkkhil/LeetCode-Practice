def getMaxLen(nums) -> int:
    n = len(nums)
    pos, neg = 0, 0
    if nums[0] > 0:
        pos = 1
    if nums[0] < 0:
        neg = 1

    ans = pos

    for i in range(1, n):
        if nums[i] > 0:
            pos = 1 + pos
            neg = 1 + neg if neg > 0 else 0
        elif nums[i] < 0:
            print("above:", pos, neg)
            temp = pos
            pos = 1 + neg if neg > 0 else 0
            neg = 1 + temp
            print("below:", pos, neg)
        else:
            pos, neg = 0, 0
        ans = max(ans, pos)
    return ans


if __name__ == "__main__":
    print(getMaxLen([1, -2, 3, -4, 5, -6, 7, -8, 9, -10]))
