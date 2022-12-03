
# we can keep i = 0 and iterate j from len - 1 to i. Compare j and j - 1. swap if j is lowest.
# Keep lowest element on left side after every j completion.
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


# we can keep i = 0 and iterate j from 0 to len - i. Compare j and j + 1. Keep highest element on right side after every j completion.

def bubble_sort2(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort2([5, 3, -44, 1, 0, -12, 6, 7, 3, 10,  -12]))