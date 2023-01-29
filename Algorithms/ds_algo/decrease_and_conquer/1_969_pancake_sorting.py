


# Given an array of integers arr, sort the array by performing a series of pancake flips.
#
# In one pancake flip we do the following steps:
#
# Choose an integer k where 1 <= k <= arr.length.
# Reverse the sub-array arr[0...k-1] (0-indexed).
# For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.
#
# Return an array of the k-values corresponding to a sequence of pancake flips that sort arr.
# Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.
#
#
# Input: arr = [3,2,4,1]
# Output: [4,2,4,3]
# Explanation:
# We perform 4 pancake flips, with k values 4, 2, 4, and 3.
# Starting state: arr = [3, 2, 4, 1]
# After 1st flip (k = 4): arr = [1, 4, 2, 3]
# After 2nd flip (k = 2): arr = [4, 1, 2, 3]
# After 3rd flip (k = 4): arr = [3, 2, 1, 4]
# After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.
#
#
# Input: arr = [1,2,3]
# Output: []
# Explanation: The input is already sorted, so there is no need to flip anything.
# Note that other answers, such as [3, 3], would also be accepted.

# T = O(n^ 2)
# s = O(1)
class Solution:
    def pancakeSort(self, arr):
        result = []
        # Assume numbers are unique and start from 1 to len(arr)
        for i in range(len(arr) - 1, 0, -1): # start from right, top most is always sort.
            if arr[i] != i + 1: # if at index 3, 3 number is not present.
                for j in range(i - 1, -1, -1): # from index 2, 0
                    if arr[j] == i + 1: # if number 3 is found
                        break          # break
                arr[: j + 1] = arr[ : j + 1][::-1] # from where 3 is found, reverse it, so that, 3 goes to top.
                arr[: i + 1] = arr[ : i + 1][::-1] # reverse the whole list so that i+1 == arr[i] and that index is finalized, then iterate to previous element.
                result.append(j+1) # j + 1 elements flipped.
                result.append(i+1) # i + 1 elements flipped.
        # 1 -j + 1 flip--> 3  - i + 1 flip -> 2
        # 3  j + 1 flip -> 1  - i + 1 flip -> 1
        # 2  j + 1 flip -> 2  - i + 1 flip -> 3 -----> 3 is sorted.
        # 4  j + 1 flip -> 4  - i + 1 flip -> 4
        #return result
        return arr


s = Solution()
print(s.pancakeSort([3,2,4,1]))
print(s.pancakeSort([3,2,4,1, 5, 8, 10, 9, 6, 7]))