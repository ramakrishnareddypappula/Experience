
# This is example. not executable problem.

# sample the disk usage of the top folder.
#
#                 /usr/
#                 / \
#             fol_a fol_b
#             /    \
#           file_a file_b
#             10MB    10 MB

def helper(node):
    if not node:
        return
    du = node.space # pre order calculation
    for child in node.children:
        du = du + helper(child)
    return du # post order return.