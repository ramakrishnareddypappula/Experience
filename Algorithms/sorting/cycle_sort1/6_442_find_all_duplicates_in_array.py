
# 442. Find All Duplicates in an Array
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer
# appears once or twice, return an array of all the integers that appears twice.
#
# You must write an algorithm that runs in O(n) time and uses only constant extra space.
#
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
#
# Input: nums = [1,1,2]
# Output: [1]
#
# Input: nums = [1]
# Output: []


class Solution:
    def findDuplicates(self, nums):
        l = len(nums)
        for i in range(l):
            while nums[i] != i + 1:
                d = nums[i] - 1
                if d < l and nums[i] != nums[d]:
                    nums[i], nums[d] = nums[d], nums[i]
                else:
                    break
        result = []
        for i in range(l):
            if nums[i] != i + 1:
                result.append(nums[i])
        return result


#OR

from collections import Counter
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = Counter(nums)
        out = []
        for each in d:
            if d[each] >= 2:
                out.append(each)
        return out