
# arr1 = [1,2,3,0,0], arr2 = [2, 5, 6]
# Time complextity = O(n log n), space complexity = O(n + m)

class Solution:
    def merge(self, arr1, m: int, arr2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # There is no return, only in place sorting is required.
        for i in range(n):
            arr1[i +m] = arr2[i]
        arr1.sort()