
# Preorder Traversal Of A Binary Tree
#        0
#       / \
#      1   2
#     / \
#     3 4
#

# [0, 1, 3, 4, 2]

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
# * Time: O(n).
# * Auxiliary space: O(n).
# * Total space: O(n).
# RECURSIVE SOLUTION
def helper(node, output):
    if node:
        output.append(node.value)
        helper(node.left, output)
        helper(node.right, output)
    return output
def preorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    return helper(root, [])

# OR

# ITERATIVE WAY:
# * Time: O(n).
# * Auxiliary space: O(n).
# * Total space: O(n).
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def preorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here. # [0, 2, 4, 3]
    if not root:
        return None
    stack = []
    stack.append(root)
    result = []
    while stack:
        node = stack.pop() # pop from right
        result.append(node.value)
        if node.right:    # push the right element first and then left element.
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


