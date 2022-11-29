
# This will work for both positive and negative values.

def counting_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    result = [0] * len(arr)
    low = min(arr)
    high = max(arr)
    count_array = [0 for i in range(low, high + 1)]
    for i in arr:
        count_array[i - low] += 1  # use an offset index #[1,,,,1, ]
    for j in range(1, len(count_array)):
        count_array[j] = count_array[j] + count_array[j - 1]
    for k in reversed(arr):
        result[count_array[k - low] - 1] = k  # here too
        count_array[k - low] -= 1  # and here
    return result