

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

# Input: nums = [3,0,1]
# Output: 2


# Using = n(n + 1)/2
# To get the missing number in [3,0,1] , length = 3. sum of 3 numbers = 3 * ( 3+ 1)/ 2 = 6.
# But 1 number is missing, to find out = 6 - sum([3, 0, 1]) = 2
class Solution1:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        total_sum = n * (n + 1)// 2
        return total_sum - sum(nums)


# using cycle sort.
# Time complexity = O(n ^ 2)
# space = O(1)
class Solution:
    def missingNumber(self, nums) -> int:
        # sort the elements using cycle sort.
        # At i index, while nums[i] != i, swap.
        # example: at 0th index if 0 is not present, then swap element at 0th index with 0 until 0 is at 0th index.
        for i in range(len(nums)):
            while nums[i] != i:
                d = nums[i]  # number that needs to be swapped with that number.
                if d < len(nums): # prevention check : example, len(nums) = 9, nums[9] will become index not in range exception.
                    nums[i], nums[d] = nums[d], nums[i]
                else:
                    break
        # elements are in place order now.
        # if 8 is not present in 8th index, then 8 is the missing elements.
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums) # if all elements are present, then last element is the missing element.


