
# 496. Next Greater Element I
#
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
#
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
#
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine
# the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
#
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
#
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
#
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        output = []
        for each in nums1:
            x = nums2.index(each)
            for i in range(x + 1, len(nums2)):
                if nums2[i] > each:
                    output.append(nums2[i])
                    break
            else:
                output.append(-1)
        return output

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
s = Solution()
print(s.nextGreaterElement(nums1, nums2))


# WE CAN DO THE FOLLOWING ON SIMILAR LINES:
# PREVIOUS LARGE VALUE : for previous, iterate from left side, check >= only
# PREVIOUS SMALL VALUE : for previous, iterate from left side, check >= only
# NEXT LARGE VALUE : for next, iterate from right side. and then reverse at the end. check >= only
# NEXT SMALL VALUE : for next, iterate from right side. and then reverse at the end. check >= only

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        result = {}
        for i in range(len(nums2) - 1, -1, -1):
            # find next great element of nums2[i]
            while stack and nums2[i] >= stack[-1]:
                stack.pop()

            if stack:
                result[nums2[i]] = stack[-1]
            else:
                result[nums2[i]] = -1
            stack.append(nums2[i])
        ans = []
        for num in nums1:
            ans.append(result[num])
        return ans
