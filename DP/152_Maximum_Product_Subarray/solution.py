# solution_video = 'https://www.youtube.com/watch?v=lXVy6YWFcRM&ab_channel=NeetCode'


def maxProduct(nums):
    res = max(nums)
    # we are mainitaing two pointers of max product and min product
    curMax, curMin = 1, 1

    for i in nums:
        # if the current element is zero, we are going to update the min and max to 1,1 resetting it.
        if i == 0:
            curMax, curMin = 1, 1
            continue
        
        # tmp is created beacuse on line 17 curMx is getting updated and we need to keep the old value.
        tmp = curMax * i
        
        curMax = max(curMax * i, curMin * i, i)
        curMin = min(tmp, curMin * i, i)
        res = max(res, curMax)

    return res


if __name__ == "__main__":
    nums = [2, 3, -2, 4, 9, -5, 11]
    print(maxProduct(nums))
