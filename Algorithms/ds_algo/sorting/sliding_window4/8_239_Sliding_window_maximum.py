
# 239. Sliding Window Maximum
#
# You are given an array of integers nums, there is a sliding window of size k which is
# moving from the very left of the array to the very right. You can only see the k numbers in
# the window. Each time the sliding window moves right by one position.
#
# Return the max sliding window.
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]


# TIMES OUT FOR LARGE DATASETS.
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        output = []
        d = deque(nums[:k])
        max_val = max(d)
        output.append(max_val)
        for i in range(k, len(nums)):
            d.popleft()
            d.append(nums[i])
            max_val = max(d)
            output.append(max_val)
        return output


s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))


from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        d = deque()
        def push(val):
            while d and val > d[-1] : # Any number is added to the collection, any other number smaller than has no chance so should be pop().
                d.pop()  # current val will delete all elements lower than it. Max element is always at left=d[0]
            d.append(val)
        for i in range(k):
            push(nums[i])
        result = []
        result.append(d[0])
        for i in range(k, len(nums)):
            if d[0] == nums[i - k]: # if d[0] is Max element and during sliding, while going to next, we need to remove this.
                                    # Otherwise in above while loop of push function it should have anyways been deleted.
                d.popleft()
            push(nums[i])
            result.append(d[0])
        return result


s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))