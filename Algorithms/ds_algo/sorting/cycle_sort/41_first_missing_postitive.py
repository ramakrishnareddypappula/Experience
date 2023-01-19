
# 41. First Missing Positive
# Given an unsorted integer array nums, return the smallest missing positive integer.
#
# You must implement an algorithm that runs in O(n) time and uses constant extra space.
#
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
#
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
#
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

class Solution:
    def firstMissingPositive(self, nums) -> int:
        # remove negative numbers + 0 which are noise.
        l = len(nums)
        neg_val = -1  # index
        for i in range(l):
            if nums[i] <= 0:
                neg_val += 1  # increment index
                nums[i], nums[neg_val] = nums[neg_val], nums[i]


        # now from neg_val index + 1 to len(l) will only contain positive values.
        nums = nums[neg_val + 1:]

        # if only negatives and 0 were present, return 1 as missing positive.
        if not nums:
            return 1
        l = len(nums)

        # sort positive values using cyclic sort.
        for i in range(l):
            while nums[i] != i + 1:
                d = nums[i] - 1
                if d < len(nums) and nums[d] != nums[i]:
                    nums[i], nums[d] = nums[d], nums[i]
                else:
                    break

        # from 0 to n, if anything is missing, that is missing value.
        for i in range(l):
            if i + 1 != nums[i]:
                return i + 1
        # else last + 1 is missing value.
        return nums[-1] + 1


# OR even simpler:

class Solution:
    def firstMissingPositive(self, nums):
        l = len(nums)
        # sort values using cyclic sort.
        for i in range(l):
            while nums[i] != i + 1:
                d = nums[i] - 1
                if 0 <= d < len(nums) and nums[d] != nums[i]:
                    # for negative, 0 and numbers greater than index, ignore them. So their values be at same index.
                    nums[i], nums[d] = nums[d], nums[i]
                else:
                    break
        # After sorting, negative and 0 numbers will be at same position, which is a
        # mismatch and return i + 1 index.

        # After sorting from 1 to n, if anything is missing, that is missing value.
        # like at index 6, if -1 is present, then 6 is first missing positive.
        for i in range(l):
            if i + 1 != nums[i]:
                return i + 1
        # else last + 1 is missing value.
        return nums[-1] + 1