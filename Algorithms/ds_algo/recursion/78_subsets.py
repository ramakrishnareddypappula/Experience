# Given set of distinct integers, return all possible subsets(). Note: solution must not contain duplicate subset

# nums = [1,2,3]
# output = [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]

# Solution:
# - At every number, we should decide whether to include or exclude that number.

# Time complexity = slate[:] will have O(n)
# In every node of the tree we need to decide to include the number of not.
# Then overall complexity is O(2 ^ N)

# With mutable parameters.
def helper(nums, i, slate, result):
    if i == len(nums):
        result.append(slate[:])
        return
    else:
        # using 3 below lines we include a number and with 4th line we exclude a number.
        slate.append(nums[i])             # include a number # = [1,2,3] here we decide to include or exclude.
        helper(nums, i + 1, slate, result) # include    # using append we include a number and then pop that.
        slate.pop()                        # include    #
        helper(nums, i + 1, slate, result) # exclude a number # we just ignore that number.
    return result

def subset(nums):
    return helper(nums, 0, [], [])

print(subset([1,2,3]))