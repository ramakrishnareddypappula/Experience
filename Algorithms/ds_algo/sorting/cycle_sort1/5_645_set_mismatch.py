

# 645. Set Mismatch
#
# You have a set of integers s, which originally contains all the numbers from 1 to n.
# Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
# which results in repetition of one number and loss of another number.
#
# You are given an integer array nums representing the data status of this set after the error.
#
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
#
# Input: nums = [1,2,2,4]
# Output: [2,3]
#
# Input: nums = [1,1]
# Output: [1,2]


class Solution:
    def findErrorNums(self, nums):
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
                result.append(i + 1)
        return result