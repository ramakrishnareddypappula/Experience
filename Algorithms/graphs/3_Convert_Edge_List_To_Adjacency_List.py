

# Convert the given edge list to the adjacency list of an undirected connected graph.
# An adjacency list represents a graph as a list of lists.
# The list index represents a vertex, and each element in its inner list represents the other vertices that form an edge with the vertex.
#
# {
#     "n": 5,
#     "edges": [
#         [0, 1],
#         [1, 4],
#         [1, 2],
#         [1, 3],
#         [3, 4]
#     ]
# }
#
#
# [
# [1],
# [0, 2, 3, 4],
# [1],
# [1, 4],
# [1, 3]
# ]


# TIME OUT IS HAPPENING FOR LARGE INPUT. Else it is correct.
def convert_edge_list_to_adjacency_list(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    #return []
    output = []
    for i in range(n):
        new_list = []
        for each in edges:
            if i in each:
                index = each.index(i)
                if index == 0:
                    new_list.append(each[1])
                else:
                    new_list.append(each[0])
        new_list.sort()
        output.append(new_list)
    return output


# * Time: O(n * log(e)).
# * Auxiliary space: O(1).
# * Total space: O(n + e).
def convert_edge_list_to_adjacency_list(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    #return []
    output = [[] for i in range(n)]
    for i in range(len(edges)):
        output[edges[i][0]].append(edges[i][1])
        output[edges[i][1]].append(edges[i][0])
    for each in output:
        each.sort()
    return output

# * Time: O(n * log(e)).
# * Auxiliary space: O(1).
# * Total space: O(n + e).
def convert_edge_list_to_adjacency_list(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    adj_list = [[] for i in range(n)]
    for i, j in edges:
        adj_list[i].append(j)
        adj_list[j].append(i)
    for each in adj_list:
        each.sort()
    return adj_list