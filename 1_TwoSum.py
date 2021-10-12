class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i,n in enumerate(nums):
            if (target - n) in d: return [i, d[target - n]]
            else: d[n] = i
