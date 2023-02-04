

# BFS Traversal Of A Graph
# Given an undirected graph, perform a Breadth-First Search Traversal on it.
#
#         1
#        /
#       0            5
#      / \
#     2  4
#    /
#   3

# {
# "n": 6,
# "edges": [
# [0, 1],
# [0, 2],
# [0, 4],
# [2, 3]
# ]
# }
#
# output = [0, 1, 2, 4, 3, 5]


# /*
# Asymptotic complexity in terms of the number of vertices `v` and number of edges `e` in the graph:
# * Time: O(v + e).
# * Auxiliary space: O(v + e).
# * Total space: O(v + e).
# */
from collections import deque
def bfs_traversal(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_int32
    """
    # Write your code here.

    graph = [[] for _ in range(n)]
    is_visited = [False for _ in range(n)]
    answer = []
    # making a graph from input edges.
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        graph[u].append(v)
        graph[v].append(u)
    print(graph)
    for i in range(n):
        # import pdb
        # pdb.set_trace()
        if not is_visited[i]:
            print(i)
            bfs_traversal_helper(i, graph, answer, is_visited)

    return answer


def bfs_traversal_helper(start_node, graph, answer, is_visited):
    is_visited[start_node] = True
    answer.append(start_node)
    q_list = deque()
    q_list.append(start_node)
    while q_list:
        u = q_list.popleft()
        for v in graph[u]:
            if not is_visited[v]:
                answer.append(v)
                q_list.append(v)
                is_visited[v] = True
    return



print(bfs_traversal(6, [[0, 1],[0, 2],[0, 4],[2, 3]])) # [0, 1, 2, 4, 3, 5]