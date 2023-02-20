
# find the maximum value.

# For balanced binary tree, worst case time complexity = O(log n)
# For unbalanced binary tree, worst case time complexity = O(height)
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def get_maximum_value(root): # right will have max value and left will have min value.
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    # Write your code here.
    # return 0
    if root == None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.value
