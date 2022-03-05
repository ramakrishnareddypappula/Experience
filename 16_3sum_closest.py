class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 3 for loops O(N3) : Time limit exceeded for large values.
        # min_sum = 0
        # closest_sum = 2 ** 64
        # for i in range(len(nums) -2):
        #     for j in range(i + 1, len(nums) - 1):
        #         for k in range(j+ 1, len(nums)):
        #             sum1 = nums[i] + nums[j] + nums[k]
        #             closest = abs(target - sum1)
        #             if closest < closest_sum:
        #                 closest_sum = closest
        #                 min_sum = sum1
        # return min_sum
        import sys
        nums.sort()
        n = len(nums)
        current = sys.maxsize
        result = nums[0] + nums[1] + nums[2]
        for k in range(0, n-2):
            t = target - nums[k]
            i, j = k+1, n-1
            while i < j:
                temp = nums[i] + nums[j]
                if current > abs(t - temp):
                    current = abs(t-temp)
                    result = temp + nums[k]
                if temp == t:
                    return temp + nums[k]
                if temp < t:
                    i += 1
                else:
                    j -= 1
        return result
