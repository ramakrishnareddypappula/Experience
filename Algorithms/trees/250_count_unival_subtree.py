
# Given a binary tree, count the number of uni value subtrees.
# Univalue subtree means all nodes of the subtree have same value.

# root = [5, 1, 5, 5, 5, null, 5]
#             5
#            / \
#           1   5
#          / \   \
#          5  5   5

# output = 4

# bottom left 5 - 1 uni value
# bottom left right - 5 - 1 uni value
# bottom right 5 - 1 uni value
# right parent with 5 -> 5 , 1 uni value.
# root has 1 as its child. so no uni value.

