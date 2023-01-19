


# 448. Find All Numbers Disappeared in an Array

# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.
#
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]


class Solution:
    def findDisappearedNumbers(self, nums):
        l = len(nums)
        for i in range(l):
            # 0th index should contain 1
            while nums[i] != i + 1:  # given that i starts from [1, n] hence i + 1
                d = nums[i] - 1  # if nums[i] = 4 , then d = 3.
                if d < len(nums) and nums[d] != nums[i]: # some numbers are repeated, hence 5 is already at 4th, then dont swap.
                    nums[i], nums[d] = nums[d], nums[i]
                else:
                    break
        # After cyclic sort, repeated numbers will settle down at elements not present.
        # [1, 2, 3, 4, 3, 2, 7, 8] , 2, 3 will settle down at 5, 6 locations.
        result = []
        for i in range(l):
            if i + 1 != nums[i]: # 0th index + 1 != 1 , then add to list.
                result.append(i+1)
        return result

s = Solution()
s.findDisappearedNumbers([4,3,2,7,8,2,3,1])



# OR
class Solution:
    def findDisappearedNumbers(self, nums):
        l = len(nums)
        s = set(nums)
        result = []
        for i in range(1, l + 1):
            if i not in s:
                result.append(i)
        return result