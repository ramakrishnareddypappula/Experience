

# Check trees.txt for explanation.
# inorder traversal of BST always prints in ascending order.

# inorder : left, root, right
# preorder: root, left, right
# postorder: left, right, root

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


# Time complexity = O(n)
# Auxiliary space: O(h) # h is height of tree.
# first traverse left subtree then visit the root then traverse right subtree.
def inorder(root):
    if root:
        # Traverse left subtree
        inorder(root.left)
        # visit node
        print(root.value)
        # traverse right subtree
        inorder(root.right)


# Time complexity = O(n)
# Auxiliary space: O(h) # h is height of tree.
# first visit the root then traverse left subtree and then traverse right subtree.
def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

# Time complexity = O(n)
# Auxiliary space: O(h) # h is height of tree.
# first traverse left subtree then traverse right subtree and then visit root.
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)