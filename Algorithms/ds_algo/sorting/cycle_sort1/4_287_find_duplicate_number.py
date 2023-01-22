
# 287. Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and uses only constant extra space.
#
# Input: nums = [1,3,4,2,2]
# Output: 2
#
# Input: nums = [3,1,3,4,2]
# Output: 3

def duplicate_number(nums):
    l = len(nums)
    for i in range(l):
        while nums[i] != i + 1:
            d = i - 1
            if d < l and nums[i] != nums[d]:
                nums[i], nums[d] = nums[i], nums[d]
            else:
                break
    for i in range(l):
        if nums[i] != i + 1:
            return nums[i]

# OR
# time = O(n)
# space= O(n)
def duplicate_number(nums):
        # from collections import Counter

        # d = Counter(nums)
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        for i, j in d.items():
            if j >= 2:
                return i

