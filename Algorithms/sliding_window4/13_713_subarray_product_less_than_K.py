

# 713. Subarray Product Less Than K
#
# Given an array of integers nums and an integer k,
# return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
#
#
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
#
# Input: nums = [1,2,3], k = 0
# Output: 0

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        base_product = 1
        left = 0
        global_count = 0
        for i in range(len(nums)):
            base_product *= nums[i]
            while base_product >= k and left <= i:
                base_product = base_product // nums[left]
                left += 1
            global_count =  global_count + (i - left + 1)
        return global_count


# base_product = 10, 50, 100 -> 10, 60
# i = 0, 1 , 2, 3
# left = 0, 0, 1, 1
# global_C = 1 + 2 + 2 + 3 = 8