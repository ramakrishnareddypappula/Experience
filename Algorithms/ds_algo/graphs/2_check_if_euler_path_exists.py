
#
# Given an undirected connected graph, check if there exists any eulerian path in it.
# The Eulerian Path is a path in the graph that visits every edge exactly once (allowing for revisiting vertices).
#
#
# {
# "n": 4,
# "edges": [
# [0, 1],
# [1, 2],
# [1, 3],
# [2, 0],
# [3, 2]
# ]
# }
#
# output = True
#
# {
# "n": 5,
# "edges": [
# [0, 3],
# [1, 2],
# [1, 3],
# [3, 2],
# [4, 1],
# [4, 2]
# ]
# }
#
# output = False

# as per graphs.txt, if vertices with odd degree are 0 or 2, then its eulerian path.

# T = O(n + e) = n = vertices and e = edges
# Auxiliary space: O(n)
# input space = O(n + e)
def check_if_eulerian_path_exists(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     bool
    """
    # Write your code here.
    #return False
    vertex_edges = [0 for _ in range(n)] # initialize all vertices with 0.
    for i, j in edges: # for every edge start point and end point, incrment by 1.
        vertex_edges[i] += 1
        vertex_edges[j] += 1

    vertices_with_odd_degree = 0
    # vertex_edges will have example: 0th vertex has 2 edges, 1st index(vertex) has 4 etc.
    for each_vertex in vertex_edges:
        if each_vertex % 2 == 1: # if a vertex has odd edge, increment by 1
            vertices_with_odd_degree += 1
    if vertices_with_odd_degree == 0 or vertices_with_odd_degree == 2: # if vertices are 0 or 2 with odd degree, return True.
        return True
    return False