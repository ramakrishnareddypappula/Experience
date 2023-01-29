
# 349. Intersection of Two Arrays
#
#
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

class Solution:
    def intersection(self, arr1, arr2):
        d = {}
        output = []
        for i in range(len(arr1)):
            if arr1[i] in d:
                d[arr1[i]] += 1
            else:
                d[arr1[i]] = 1

        for i in range(len(arr2)):
            if arr2[i] in d:
                output.append(arr2[i])
                d[arr2[i]] -= 1
                if d[arr2[i]] == 0:
                    del d[arr2[i]]
        return set(output)


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
s = Solution()
print(s.intersection(nums1, nums2))


# OR

class Solution:
    def intersection(self, arr1, arr2):
        return list(set(arr1) & set(arr2))


# OR

class Solution:
    def intersection(self, arr1, arr2):
        if len(arr1) > len(arr2):
            l = len(arr2)
            k = arr2
            x = arr1
        else:
            l = len(arr1)
            k= arr1
            x = arr2
        i = 0
        output = []
        while i < l:
            if k[i] in x:
                output.append(k[i])
            i += 1
        return set(output)