
# 643. Maximum Average Subarray I
#
# You are given an integer array nums consisting of n elements, and an integer k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.
#
# Input: nums = [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75000
# Explanation: Maximum
# average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
#
#
# Input: nums = [5], k = 1
# Output: 5.00000


class Solution:

    def findMaxAverage(self, nums, k):
        first_k_sum = sum(nums[:k])
        max_avg = first_k_sum / k
        total_sum = first_k_sum
        for i in range(k, len(nums)):
            total_sum = total_sum + nums[i] - nums[i-k]
            avg = total_sum / k
            max_avg = max(max_avg, avg)
        return max_avg