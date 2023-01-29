

# 503. Next Greater Element II
#
# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]),
# return the next greater number for every element in nums.
#
# The next greater number of a number x is the first greater number to its traversing-order next in the array,
# which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
#
#
# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number.
# The second 1's next greater number needs to search circularly, which is also 2.
#
# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]


class Solution:
    def nextGreaterElements(self, values):
        stack = []
        result = []
        # standard monotonic stack code.
        # if we do 1 loop, we get the values in decreasing order and use the same stack again.
        for i in range(len(values) - 1, -1, -1):
            while stack and values[i] >= stack[-1]:
                stack.pop()
            stack.append(values[i])

        # next greater_value program
        for i in range(len(values) - 1, -1, -1):
            while stack and values[i] >= stack[-1]:
                stack.pop()
            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)
            stack.append(values[i])
        result.reverse()
        return result

s = Solution()
print(s.nextGreaterElements([1,2,3,4,3]))