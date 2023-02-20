

# Given a binary tree, return the level order traversal of its nodes values.


         #        1
         #    /   |  \
         #   3    2   4
         #  / \
         # 5  6

#output = [[1], [3,2,4], [5, 6]]

# time = O(n)
# space = O(n)

from collections import deque
def level_order_traversal(root):
    result = []
    if not root:
        return result
    queue = deque()
    queue.append(root)
    toggle = False
    while queue:
        temp = []
        l = len(queue)
        for i in range(l):
            node = queue.popleft()
            temp.append(node.value)
            for child in node.children:
                queue.append(child)
        if toggle:  # to print in zigzag fashion. Like, first temp left to right, then right to left and so on.
            temp.reverse()
        toggle = not toggle
        # result.append(temp[-1]) # if we want to see the right side view of the tree.
        result.append(temp)
    # result.reverse() # bottom to top traversal. [[5, 6],[3,2,4], [1]]
    return result

# if we want bottom to top traversal instead of top to bottom traversal, just reverse the output
# result.reverse() # bottom to top traversal. [[5, 6],[3,2,4], [1]]

# To see the right side view of the tree:
#  result.append(temp[-1])









