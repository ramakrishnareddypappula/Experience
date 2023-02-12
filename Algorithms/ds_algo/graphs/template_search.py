#
# 1. Edge list to Adjacency list:
#
#     graph = [[] for _ in range(n)]
#
#     for src, dst in edge_list:
#         graph[src] = dst
#         graph[dst] = src  --> if undirected, this is also coded, else no.
#     visited = [False for i in range(n)] # If Adjacency map is created instead on adjacency list, then visited will be set instead of list.
#
#
#2.
# BFS
#
# def BFS(source):
#     q = deque()
#     q.append(source)
#     visited[source] = True
#     while q:
#         node = q.pop()
#         for neighbour in graph[node]:
#             if not visited[neighbour]: # In trees, we will not have this.
#                 visited[neighbour] = True
#                 q.append(neighbour)
#
#
#
# DFS
# def DFS(source):
#     visited[source] = True   # In trees, we will not have this.
#     for neighbour in graph[source]:
#         if not visited[neighbour]:
#             DFS(neighbour)
#
#
#
#3. outer loop
# for i in range(n):
#     if not visited[i]:
#         DFS(i) or BFS(i)


# Space complexity is Size of queue for BFS vs hieght of the tree in DFS.