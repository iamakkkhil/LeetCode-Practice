def maxSubArray(nums) -> int:
    max_sum = -10000
    max_here = 0

    for num in nums:
        max_here += num
        if max_sum < max_here:
            max_sum = max_here
        if max_here < 0:
            max_here = 0

    return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))
