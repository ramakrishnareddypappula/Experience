from collections import deque

# MAY BE WRONG.
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
    print(graph)
    for i in range(n):
        if not is_visited[i]:
            dfs_helper(i, graph, is_visited, answer)

    return answer


def dfs_helper(start_node, graph, is_visited, answer):
    is_visited[start_node] = True
    answer.append(start_node)
    q_list = deque()
    q_list.append(start_node)
    while q_list:
        u = q_list.popleft() # 0
        for i in graph[u]:
            if not is_visited[i]:
                is_visited[i] = True
                answer.append(i)
                q_list.append(i)
    return


print(dfs_traversal(6, [[0, 1],[0, 2],[1, 4],[3, 5]])) # output = [0, 1, 4, 2, 3, 5]