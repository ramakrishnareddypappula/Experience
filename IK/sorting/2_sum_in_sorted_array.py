# Given an array sorted in non-decreasing order and a target number, find the indices of the two values from the array that sum up to the given target number.
#
# {
# "numbers": [1, 2, 3, 5, 10],
# "target": 7
# }
# Output:
#
# [1, 3]


def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    i = 0
    j = len(numbers) - 1
    while i < j:
        if numbers[i] + numbers[j] == target:
            return [i, j]
        elif numbers[i] + numbers[j] > target :
            j -= 1
        else:
            i += 1
    return [-1, -1]