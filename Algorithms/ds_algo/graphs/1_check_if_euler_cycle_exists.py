
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

# From graphs.txt, A euler cycle has even vertices. which means even number of times edges starting/ending from vertex.

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
    # return False
    vertex_edges = [0 for _ in range(n)] # initialize all vertices with 0.
    for i, j in edges: # for every edge start point and end point, incrment by 1.
        vertex_edges[i] += 1
        vertex_edges[j] += 1

    # vertex_edges will have example: 0th vertex has 2 edges, 1st index(vertex) has 4 etc.
    for each_vertex in vertex_edges: # if a vertex has odd edge, its not euler cycle, return False.
        if each_vertex % 2 == 1:
            return False
    return True # If there is no odd vertex found, return True.