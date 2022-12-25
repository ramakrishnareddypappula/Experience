
# Given two integers n and k, find all the possible unique combinations of k numbers in range 1 to n.

# input:
# {
# "n": 5,
# "k": 2
# }
#
# output:
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
import copy
def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    # import pdb
    # pdb.set_trace()
    return helper(n, k, 1, [], [])


def helper(n, k, i, slate, result):
    if k == 0:
        #result.append(slate.copy()) # 3.x
        result.append(slate[:])

    else:

        for j in range(i, n - k + 1 + 1):
            slate.append(j)
            helper(n, k - 1, j + 1, slate, result)
            slate.pop()

    return result



print(find_combinations(4, 2)) # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]