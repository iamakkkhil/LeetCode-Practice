def canJump(nums) -> bool:
    last = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        distance = last - i
        jump = nums[i]

        if jump >= distance:
            last = i

    if last == 0:
        return True
    return False


if __name__ == "__main__":
    print(canJump([2, 3, 1, 1, 4]))
    print(canJump([3, 2, 1, 0, 4]))