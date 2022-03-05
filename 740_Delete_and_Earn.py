class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        maxElem = max(nums)
        arr = [0 for i in range(maxElem + 1)]
        
        counter = Counter(nums)
        
        for num in range(1, maxElem + 1):
            arr[num] = max(arr[num - 1], arr[num - 2] + counter[num]*num)
            
        return arr[-1]
