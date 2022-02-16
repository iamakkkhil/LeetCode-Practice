def permute(nums):
    if len(nums) == 1:
        temp_array = []
        temp_array.append(nums)
        return temp_array

    result_array = self.permute(nums[1:])
    ans = []

    for array in result_array:
        for i in range(len(array) + 1):
            temp = array[:]
            temp.insert(i, nums[0])
            ans.append(temp)

    return ans
