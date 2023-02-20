
# Given an array of numbers, rearrange them in-place so that even numbers appear before odd ones.
# {
# "numbers": [1, 2, 3, 4]
# }
# Output:
#
# [4, 2, 3, 1]


def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    i = 0
    j = len(numbers) - 1
    while i <= j:
        if (numbers[i] % 2 == 1) and (numbers[j] % 2 == 0):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
            j -= 1
        elif (numbers[i] % 2 == 0):
            i += 1
        elif (numbers[j] % 2 == 1):
            j -= 1
    return numbers