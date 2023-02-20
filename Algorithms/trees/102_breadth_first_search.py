
# breadth First Search or Level Order Traversal.

# Time complexity = O(N) each node is traversed 1 time.
# Auxiliary space = O(N) , for queue, at the bottom level queue will be of size O(n/2) max.
#                         But also in n-ary tree there can be 1 parent and n child. So queue size can be max O(n).

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
from collections import deque # we need to remove from left. double ended queue.
def level_order_traversal(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = []
    if not root: return result
    queue = deque()
    queue.append(root)
    while queue:
        temp = []
        l = len(queue)
        for i in range(l):
            node = queue.popleft()
            temp.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(temp)
    return result