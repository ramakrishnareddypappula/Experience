
# N Choose K Combinations
# Given two integers n and k, find all the possible unique combinations of k numbers in range 1 to n.
#
# {
# "n": 5,
# "k": 2
# }
#
# [
# [1, 2],
# [1, 3],
# [1, 4],
# [1, 5],
# [2, 3],
# [2, 4],
# [2, 5],
# [3, 4],
# [3, 5],
# [4, 5]
# ]
#
# {
# "n": 6,
# "k": 6
# }
#
# [
# [1, 2, 3, 4, 5, 6]
# ]

# def find_combinations(n, k):
#     """
#     Args:
#      n(int32)
#      k(int32)
#     Returns:
#      list_list_int32
#     """
#     # Write your code here.
#     # return []
#     return helper(n ,k, 1, [], [])
#
# def helper(n ,k, i, slate, result):
#
#     if k == 0:
#         result.append(slate.copy())
#     else:
#
#         for j in range(i , n - k + 1 +1):
#             slate.append(j)
#             helper(n, k- 1, j + 1, slate, result)
#             slate.pop()
#
#     return result

# def helper(n, k, i, slate, result):
#     if k == len(slate):
#         result.append(slate[:])
#         return
#     if n + 1 == i:
#         return
#     slate.append(i)
#     helper(n, k, i + 1, slate, result)
#     slate.pop()
#     helper(n, k, i + 1, slate, result)
#
#     return result
#
# def find_combinations(n, k):
#     return helper(n, k, 1, [], [])
#
# print(find_combinations(6, 6))

def helper(n, k, i, slate, result):
    if k == 0:
        result.append(slate[:])
        return
    else:
        for j in range(i, n+ 1):
            slate.append(j)
            helper(n, k - 1, j + 1, slate, result)
            slate.pop()
    return result

def find_combinations(n, k):
    return helper(n, k, 1, [], [])

print(find_combinations(5, 2))

x = []
for i in range(1, 5 + 1):
    for j in range( i + 1 , 5 + 1):
      x.append([i, j])
#print(x)
#[[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]