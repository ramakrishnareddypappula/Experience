# given binary and sum, determine if tree has root-to-leaf such their sum is equal to target

# target = 22
#
#             5
#            / \
#           4   8
#           /   / \
#          11   13 4
#          / \      \
#         7  2      1


# 5 -> 4 -> 11 -> 2 = 22

# Time = O(n)
# Space = O(height)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False
        flag = [False]  # flag is a list to make persistant across functions.
        def helper(root, targetSum):
            if root.val == targetSum and root.left is None and root.right is None:
                # The sum should be from root to leaf. Hence only when left and right is empty,
                # and current node value == target, then its True, else False.
                flag[0] = True
                return
            if root.left:
                helper(root.left, targetSum - root.val)
            if root.right:
                helper(root.right, targetSum - root.val)
        helper(root, targetSum)
        return flag[0]

