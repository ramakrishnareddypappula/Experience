
# IN EVERY ITERATION(J), COMPARE LAST AND LAST - 1. IF LAST IS LOWER, THEN SWAP. UNTIL I.

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


print(bubble_sort([5, 3, -44, 1, 0, -12, 6, 7, 3, 10,  -12]))


# IN EVERY ITERATION(J), COMPARE FIRST AND FIRST +1. IF FIRST IS HIGHER, THEN SWAP. UNTIL I - 1.

def bubble_sort2(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort2([5, 3, -44, 1, 0, -12, 6, 7, 3, 10,  -12]))