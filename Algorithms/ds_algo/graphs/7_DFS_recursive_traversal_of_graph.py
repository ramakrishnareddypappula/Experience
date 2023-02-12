
# Given an undirected graph, perform a Depth-First Search Traversal on it.
#
#     0 --- 1
#     |     |
#     |     |
#     2     4
#
#
#     3 -- 5
#
# input:
# {
# "n": 6,
# "edges": [
# [0, 1],
# [0, 2],
# [1, 4],
# [3, 5]
# ]
# }
#
# output = [0, 1, 4, 2, 3, 5]
#
# Below are some other valid outputs if the DFS traversal starts from the vertex 0:
#
# [0, 2, 1, 4, 5, 3]
# [0, 2, 1, 4, 3, 5]
# [0, 1, 4, 2, 5, 3]
# DFS starting from any other node will also be considered valid.

# Asymptotic complexity in terms of the number of vertices `v` and number of edges `e` in the graph:
# * Time: O(v + e).
# * Auxiliary space: O(v + e).
# * Total space: O(v + e).

# Time complexity = O(n)(push pop vertices) + O(m)(looking at adj_list of each vertex)
# Aux space = O(degree(u)) = 2m(look graph.txt) = O(m)
# space = O(n) # height of tree.

def dfs_traversal(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    # return []
    graph = [[] for _ in range(n)]
    answer = []
    is_visited = [False for i in range(n)]
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    for i in range(n):
        if not is_visited[i]:
            dfs_helper(i, graph, is_visited, answer)

    return answer

def dfs_helper(start_node, graph, is_visited, answer):
    is_visited[start_node] = True
    answer.append(start_node)
    for v in graph[start_node]:
        if not is_visited[v]:
            dfs_helper(v, graph, is_visited, answer)
    return