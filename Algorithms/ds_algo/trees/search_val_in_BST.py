"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def search_node_in_bst(root, value):
    """
    Args:
     root(BinaryTreeNode_int32)
     value(int32)
    Returns:
     bool
    """
    # Write your code here.
    current = root
    while current is not None:
        if current.value == value:
            return True
        elif current.value > value:
            current = current.left
        else:
            current = current.right
    return False
