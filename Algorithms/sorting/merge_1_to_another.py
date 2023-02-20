# First array has n positive numbers, and they are sorted in the non-descending order.
#
# Second array has 2n numbers: first n are also positive and sorted in the same way but the last n are all zeroes.
#
# Merge the first array into the second and return the latter. You should get 2n positive integers sorted in the non-descending order.
#
# {
# "first": [1, 3, 5],
# "second": [2, 4, 6, 0, 0, 0]
# }
# Output:
#
# [1, 2, 3, 4, 5, 6]

def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    # i = len(first) - 1
    j = len(first) - 1
    for i in range(len(second) - 1, -1 , -1):
        second[i] = first[j]
        j -= 1
        if j == -1:
            break
    second.sort()
    return second