
        #     5
        #    / \
        #   3   6
        #  / \
        #  2  4
        #  /
        # 1


# Solution 1 :
#        Do inorder traversal and append to the list. list is by default sorted. for a number get next element, that is the successor.
#
# Solution 2:
#        Do BST and get all the elements. sort them and then get the next to the element, that is the successor.


# Solution 3:
# If root node is the p, then its successor will always be in right side.
# if p is left most child, then its successor is it parent.
# if p is the right most child, then there is no successor.
# if p is in between, there are cases.

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""

# time complexity is O(n)
# space complexity is O(1)
def successor(root, p):
    success = None

    current = root
    while current:
        if p.value >= current.value: # node has greater value than root. Successor will on right side.
            current = current.right
        else: #  successor is on left side.
            success = current  # It is tracking the parent node.
            current = current.left
    return success

    # p = 4, root = 5
    # successor = 5, current = 3
    # current = 4
    # p = 4, current = 4 , successor = 5



    #     5
    #    / \
    #   3   6
    #  / \
    #  2  4
    #  /
    # 1

# time complexity is O(n)
# space complexity is O(1)
def predecessor(root, p):
    predecess = None
    current = root
    while current:
        if p.value >= current.value:
            predecess = current # track the previous node.
            current = current.right
        else:
            current = current.left
    return predecess
