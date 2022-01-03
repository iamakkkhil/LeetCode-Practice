def jump(nums) -> int:
    jump = 0
    l, r = 0, 0

    while r < len(nums) - 1:
        farthest_jump = 0
        for i in range(l, r + 1):
            farthest_jump = max(farthest_jump, i + nums[i])

        l = r + 1
        r = farthest_jump
        jump += 1

    return jump


if __name__ == "__main__":
    print(jump([2, 3, 1, 1, 4]))
    print(jump([3, 2, 1, 0, 4]))
