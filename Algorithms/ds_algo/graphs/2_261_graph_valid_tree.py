


# Valid Tree = Tree is a connected graph with no cycles.
# Given n nodes from 0 to n - 1 and list of undirected edges write a function to check whether these edges make up a valid tree
#
# input =
# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
#
# output = True
#
# n = 5 edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# output = False

# If we detect a cross edge, then there is a cycle.
# cross edge can be inbetween nieghbours in same level or 1 level up.

from collections import deque
def valid_tree(n, edges):
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
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        graph[u].append(v)
        graph[v].append(u)

    connect_components = 0
    for i in range(n):
        if not is_visited[i]:
            connect_components += 1
            if connect_components > 1:
                return False # more than 1 connected components
            if bfs_traversal_helper(i, graph, answer, is_visited):
                return False # if cycle is present.

    return True  # no cycle, only 1 connected component

def bfs_traversal_helper(start_node, graph, answer, is_visited):
    is_visited[start_node] = True
    answer.append(start_node)
    q_list = deque()
    q_list.append(start_node)
    #parent = {}
    parent = [0 for _ in range(len(is_visited))]
    while q_list:
        node = q_list.popleft()
        for neighbour in graph[node]:
            if not is_visited[neighbour]:
                answer.append(neighbour)
                parent[neighbour] = node
                q_list.append(neighbour)
                is_visited[neighbour] = True
            else: # if neighbour is visited
                if neighbour != parent[node]:  # neighbour is visited, but he is not our parent, Then its cross edge and we conclude there is cycle.
                    return True
    return False

print(valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])) # True
print(valid_tree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])) # False
