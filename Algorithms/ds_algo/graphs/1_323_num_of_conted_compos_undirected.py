# 323. Find the number of connected components in undirected graph.
#
# Given n nodes labeled from 0 to n - 1 and list of undirected edges(each edge has pair of nodes) write a function to find
# the number of connected components in undirected graph.
#
#
# input n = 5
# edges = [[0, 1], [1, 2], [3, 4]]
#
# output = 2
#
# input n = 5
# edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

# output = 1


# * Time: O(v + e).
# * Auxiliary space: O(v + e).
# * Total space: O(v + e).

def components(n, edges):
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

    connect_components = 0
    for i in range(n):
        if not is_visited[i]:
            connect_components += 1
            dfs_helper(i, graph, is_visited, answer)

    return connect_components

def dfs_helper(start_node, graph, is_visited, answer):
    is_visited[start_node] = True
    answer.append(start_node)
    for v in graph[start_node]:
        if not is_visited[v]:
            dfs_helper(v, graph, is_visited, answer)
    return

print(components(5, [[0, 1], [1, 2], [3, 4]])) # 2
print(components(5, [[0, 1], [1, 2], [2, 3], [3, 4]])) # 1