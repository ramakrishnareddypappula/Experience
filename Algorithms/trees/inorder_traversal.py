

# Inorder Traversal Of A Binary Tree

#        0
#       / \
#      1   2
#     / \
#     3 4
#
#[3, 1, 4, 0, 2]

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

def helper(node, output):
    if node:
        helper(node.left, output)
        output.append(node.value)
        helper(node.right, output)
    return output

def inorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    #return []
    return helper(root, [])