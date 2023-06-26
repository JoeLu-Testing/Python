def twoSum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

nums = [1, 3, 5, 7, 9]
target = 6
result = twoSum(nums, target)
print(result)
