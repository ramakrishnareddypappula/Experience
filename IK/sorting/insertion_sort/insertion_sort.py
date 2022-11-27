

def insertion_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here. # [5, 8, 3, 9, 4, 1, 7]
    for i in range(len(arr)):
        pivot = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > pivot:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = pivot
    return arr