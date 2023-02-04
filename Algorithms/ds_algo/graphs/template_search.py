#
#
# BFS
#
# def bfs(s):
#     #visited, captured and parent are initialized to [], [] and null.
#     captured[s] = 1
#     visited[s] = 1
#     q = Queue()
#     q.push()
#     while q:
#         v = q.popleft()
#         captured[v] = 1
#         for w in ajlist[v]:
#             if visited[w] == 0:
#                 visited[w] = 1
#                 parent[w] = v
#                 q.append(w)
#
#
#
# DFS:
#
# In DFS, replace queue with stack and do last in first out.
#
#
# def dfs(s):
#     # visited, captured and parent are initialized to [], [] and null.
#     captured[s] = 1
#     visited[s] = 1
#     q = [] # change here
#     q.push()
#     while q:
#         v = q.pop() # here.
#         captured[v] = 1
#         for w in ajlist[v]:
#             if visited[w] == 0:
#                 visited[w] = 1
#                 parent[w] = v
#                 q.append(w)