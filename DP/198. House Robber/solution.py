def rob(nums) -> int:
    if len(nums) < 3:
        return max(nums)

    f = [0] * len(nums)

    f[-1], f[-2] = nums[-1], nums[-2]
    f[-3] = nums[-3] + f[-1]

    for i in range(len(nums) - 4, -1, -1):
        f[i] = nums[i] + max(f[i + 2], f[i + 3])

    return max(f[0], f[1])


if __name__ == "__main__":
    print(rob([1, 2, 3, 1]))
    print(rob([2, 7, 9, 3, 1]))
    print(rob([2, 1, 1, 2]))
