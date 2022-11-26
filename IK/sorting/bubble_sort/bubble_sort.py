
def bubble_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    l = len(arr)
    for i in range(l):
        for j in range(l-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr
