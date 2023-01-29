
# 209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
#
#
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
#
# Input: target = 4, nums = [1,4,4]
# Output: 1
#
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

# Time complexity = O(n)
# outer for loop runs entire array.
# In while loop potentially runs n times as well.
# Operations inside while are constant time operations, Hence overall it is O(n)

import sys
class Solution:
    def minSubArrayLen(self, target: int, nums):
        window_sum = 0
        left = 0
        global_min = sys.maxsize
        # for loop goes from left to right adding each element.
        # when it hits the target, while then subtracts each value from index 0, calculating global_min every time.
        # this goes for for loop until the end.
        # Lasts say we find 3 elements sum > target initially, later if we find only 2 elements later, so global_min will have this.
        for i in range(len(nums)):
            window_sum += nums[i]
            while window_sum >= target and left <= i:
                window_sum -= nums[left]
                global_min = min(global_min, i - left + 1)
                left += 1
        if global_min == sys.maxsize:
            return 0
        return global_min


s = Solution()
print(s.minSubArrayLen([12,28,83,4,25,26,25,2,25,25,25,12], 213))