

# 113. Path Sum II
#
# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where
# the sum of the node values in the path equals targetSum. Each path should be returned as a list
# of the node values, not node references.
#
#
# root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time - For each path it will be log n. for all paths, it will be O(n log n) because of result.append(slate[:]).
# space - O(n log n).
class Solution:
    def pathSum(self, root, targetSum: int):
        result = []
        if not root:
            return result
        def helper(root, target, slate, result):
            if root.val == target and root.left == None and root.right == None:
                slate.append(root.val)
                result.append(slate[:])
                slate.pop()
                return
            slate.append(root.val)
            if root.left:
                helper(root.left, target - root.val, slate , result)
            if root.right:
                helper(root.right, target - root.val, slate, result)
            slate.pop()
        helper(root, targetSum, [], result)
        return result