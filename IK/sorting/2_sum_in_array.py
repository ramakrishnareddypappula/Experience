
#Given an array and a target number, find the indices of the two values from the array that sum up to the given target number.
#
#{
#"numbers": [5, 3, 10, 45, 1],
#"target": 6
#}
#Output:
#
#[0, 4]


def two_sum(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    d = {}
    for i in range(len(numbers)):
        diff = target - numbers[i]
        if diff in d:
            return [i, d[diff]]
        else:
            d[numbers[i]] = i
    return [-1, -1]