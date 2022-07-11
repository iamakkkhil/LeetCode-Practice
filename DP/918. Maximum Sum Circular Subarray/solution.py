def maxSubarraySumCircular(nums):
    if max(nums) <= 0:
        return max(nums)

    endmax = [i for i in nums]
    endmin = [i for i in nums]

    for i in range(1, len(nums)):
        if endmax[i - 1] > 0:
            endmax[i] += endmax[i - 1]

        if endmin[i - 1] < 0:
            endmin[i] += endmin[i - 1]

    return max(max(endmax), sum(nums) - min(endmin))


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubarraySumCircular(nums))
