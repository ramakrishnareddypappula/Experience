class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time complexity is O(n) since we need to iterate for n elements.
        # Space complexity is O(n) since dict of is created with atmost n elements.
        d = {}
        for index, value in enumerate(nums):
            act_val = target - value
            if act_val in d: # O(1)
                return d[act_val], index
            else:
                d[value] = index
        return False
