
def counting_sort_with_positive_values(arr):
    output = [0 for _ in range(len(arr))]
    minval = 0
    maxval = max(arr)
    temp = [0 for _ in range(minval, maxval + 1)]
    for i in range(len(arr)):
        temp[arr[i]] += 1
    for j in range(1, len(temp)):
        temp[j] = temp[j] + temp[j - 1]

    for k in range(len(arr) - 1, -1, -1):
        val = arr[k]
        temp[val] = temp[val] - 1
        output[temp[val]] = val
    return output

print(counting_sort_with_positive_values([2, 10, 1, 3, 2]))
print(counting_sort_with_positive_values([10, 0]))
print(counting_sort_with_positive_values([10, 5, 4, 2, 1]))
print(counting_sort_with_positive_values([4, 5, 2, 1, 0]))


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


