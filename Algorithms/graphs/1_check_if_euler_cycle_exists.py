
# Check If Eulerian Cycle Exists

# Check if there exists any eulerian cycle in a given undirected connected graph.
# The Euler cycle is a path in the graph that visits every edge exactly once and starts and finishes at the same vertex.

# input
# {
# "n": 5,
# "edges": [
# [0, 1],
# [0, 2],
# [1, 3],
# [3, 0],
# [3, 2],
# [4, 3],
# [4, 0]
# ]
# }
# output: True
#
# input:
# {
# "n": 6,
# "edges": [
# [0, 4],
# [0, 5],
# [1, 2],
# [2, 3],
# [3, 1],
# [4, 3],
# ]
# }
# output = False



     # 1 - 0  - 3   # each vertex has 2 edges.
     # |        |
     # 2 -  6 - 4

# An Eulerian cycle exists if and only if the degrees of all vertices are even.
# T = O(n + e) = n = vertices and e = edges
# Auxiliary space: O(n)
# input space = O(n + e)
def check_if_eulerian_cycle_exists(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     bool
    """
    # Write your code here.
    # calculate the degree at each vertex.
    vertices = [0 for _ in range(n)] # initialize all vertices with 0.
    for i, j in edges: # for every edge start point and end point, incrment by 1.
        vertices[i] += 1
        vertices[j] += 1

    # vertex_edges will have example: 0th vertex has 2 edges, 1st index(vertex) has 4 etc.
    for vertex_edge_count in vertices: # if a vertex has odd edge, its not euler cycle, return False.
        if vertex_edge_count % 2 == 1:
            return False
    return True # If there is no odd vertex found, return True.


print(check_if_eulerian_cycle_exists(5, [[0, 1],[0, 2],[1, 3],[3, 0],[3, 2],[4, 3],[4, 0]])) #True
print(check_if_eulerian_cycle_exists(6,[[0, 4],[0, 5],[1, 2],[2, 3],[3, 1],[4, 3]])) #False