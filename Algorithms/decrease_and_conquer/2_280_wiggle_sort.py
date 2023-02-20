
# 280. Wiggle sort
#
# Given an unsorted array nums, reorder it in place such that nums[0] <= nums[1] >= nums[2] <= nums[3]
#
# input = [3, 5, 2, 1, 6, 4] # numbers are unique. Not for repeated numbers
# 1 possible answer = [3,5,1,6,2,4], there can be multiple answers

# Logic : odd index will be greater than even index, if it is not , swap odd and even index.

# T = O(n)
# s = O(1)
def wiggle_sort(nums):
    for i in range(1, len(nums)): # starting from index 1.
        if ((i%2 == 1) and (nums[i] < nums[i - 1])) or ((i % 2 == 0) and (nums[i] > nums[i - 1])):
                    # if nums[1] < nums[0]                          nums[2] > nums[1] then swap
            nums[i], nums[i - 1] = nums[i - 1], nums[i]

    return nums

print(wiggle_sort([3, 5, 2, 1, 6, 4] )) # [3,5,1,6,2,4]
