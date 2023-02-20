
# 53. Maximum Subarray
# Given an integer array nums, find the  subarray with the largest sum, and return its sum.

# Explanation in strings.txt

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

# brute -force = exhaustively look for all subarrays. start and end index = 2 = NC2 = n(n-1)/2 = n^2 complexity.



# Use variable length sliding window:
# initialize local_max and global_max to first value.
# calculate sum with current value and without current value. check which is greater and make it local_max.
# compare max of local_max and global_max and assign to global_max.

# Intuition: find the max value with current index and without current index.
# Time complexity = O(N)
# space complexity = O(1)
def kadane(list_num):
    local_max = list_num[0]
    global_max = list_num[0]
    for i in range(1, len(list_num)): # start from 1.
        local_max = max(list_num[i], list_num[i] + local_max)
        global_max = max(global_max, local_max)
    return global_max

print(kadane([1,3,-2,-1, 5]))
