

# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#
# Given an array of integers arr and two integers k and threshold,
# return the number of sub-arrays of size k and average greater than or equal to threshold
#
#
# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
#
#
# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6
# Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.


from collections import deque
class Solution:
    def numOfSubarrays(self, arr, k: int, threshold):
        first_k = arr[:k]
        total_sum = sum(first_k)
        queue = deque()
        queue.extend(first_k)
        max_avg_list = 0
        if (total_sum / k) >= threshold:
            max_avg_list += 1
        for i in range(k, len(arr)):
            total_sum = total_sum + arr[i] - arr[i - k]
            if (total_sum / k) >= threshold:
                max_avg_list += 1
        return max_avg_list