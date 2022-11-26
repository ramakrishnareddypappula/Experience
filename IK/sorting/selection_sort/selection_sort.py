

def selection_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """   # [2, 5 , 3, 1]
    l = len(arr)
    for i in range(l):
        minval = arr[i]
        minindex = i
        for j in range(i+1, l):
            if arr[j] < minval:
                minval = arr[j]
                minindex = j
        arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr
