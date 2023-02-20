
# 480. Sliding Window Median
# The median is the middle value in an ordered integer list. If the size of the list is even,
# there is no middle value. So the median is the mean of the two middle values.

# For examples, if arr = [2,3,4], the median is 3.
# For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
# You are given an integer array nums and an integer k. There is a sliding window of
# size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.
#
# Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.
#
# Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
# Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
# Explanation:
# Window position                Median
# ---------------                -----
# [1  3  -1] -3  5  3  6  7        1
# 1[3 - 1 - 3] 5 3 6 7            - 1  ...

#NOT TIMING OUT FOR ALL SCENARIOS: WORKING FINE.
class Solution:

    def medianSlidingWindow(self, nums, k: int):
        output = []
        first_k = nums[:k]
        sorted_list = sorted(first_k)
        if k % 2 == 0:
            l = len(sorted_list)
            output.append(float(sorted_list[l//2] + sorted_list[l//2 - 1]) / 2)
        else:
            l = len(sorted_list)
            output.append(float(sorted_list[l//2]))
        for i in range(k, len(nums)):
            first_k.pop(0)
            first_k.append(nums[i])
            sorted_list = sorted(first_k)
            if k % 2 == 0:
                l = len(sorted_list)
                output.append(float(sorted_list[l // 2] + sorted_list[l // 2 - 1]) / 2)
            else:
                l = len(sorted_list)
                output.append(float(sorted_list[l // 2]))
        return output

# Explains about min heap max heap : Take a look
# optional arrays.