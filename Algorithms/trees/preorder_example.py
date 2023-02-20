
# This is example. not executable problem.

# Table of contents:
#     Chapter 1
#         Section 1.1
#         Section 1.2
#             Section 1.1.1
#             Section 1.1.2
#
#                 TOC
#                 / \
#             chap 1 chap 2
#             / \
#           sec 1.1 sec 1.2
#             /    \
#            1.1.1 1.1.2
#

def helper(node, level): # level to indicate the space
    if not node:
        return
    print(" " * level + str(node.key))
    for child in node.children:
        helper(child, level + 1)

def dfs(root):
    return helper(root, 0)