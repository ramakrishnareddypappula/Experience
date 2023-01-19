



#recursive way.
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def helper(root, result):
    if root:
        helper(root.left, result)
        helper(root.right, result)
        result.append(root.value)
    return result

def postorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    # return []
    return helper(root, [])


# or

# Iterative way.
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def postorder(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    # return []
    result = []
    if not root:
        return result
    stack = []
    stack.append(root)
    while stack:
        current = stack.pop()
        result.append(current.value)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    result.reverse()
    return result