

# Given an array of numbers, build a binary search tree(BST) by inserting the values sequentially inside an initially empty BST.




#For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def build_a_bst(values):
    """
    Args:
     values(list_int32)
    Returns:
     BinaryTreeNode_int32
    """

    # Write your code here.
    def helper(node, value):
        newnode = BinaryTreeNode(value)
        if node == None: # for root, we return this.
            return newnode
        prev = None  # we are using prev just to keep track of last node, so that we can link at the end.
        current = node
        while current is not None:
            prev = current # prev points to prev node.
            if current.value == value:
                print("value is already present")
            elif current.value > value:
                current = current.left
            else:
                current = current.right
        if value > prev.value:
            prev.right = newnode  # linking is done.
        else:
            prev.left = newnode
        return node

    root = None
    for value in values:
        root = helper(root, value)
    return root