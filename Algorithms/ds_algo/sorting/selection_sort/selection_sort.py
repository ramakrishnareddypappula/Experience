# SELECT AN ELEMENT FROM LEFT. COMPARE LEFT + 1 TILL END WITH LEFT ELEMENT AND GET THE LOWEST VALUE INDEX. SWAP IT WITH LEFT
# ELEMENT. LOWEST IS SORTED. IN SECOND ITERATION, SELECT LEFT + 1, COMPARE LEFT + 2 TILL END TO LEFT + 1. SWAP IT WITH LEFT + 1
# ELEMENT.

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

print(selection_sort([5, 3, -44, 1, 0, -12, 6, 7, 3, 10,  -12]))

# SELECT RIGHT ELEMENT. FROM RIGHT - 1 TILL START COMPARE WITH RIGHT AND GET THE MAX VALUE INDEX. SWAP MAX VALUE INDEX WITH RIGHT.
# AND SO ON.

def selection_sort1(arr):
    for i in range(len(arr) - 1, -1, -1):
        maxval = arr[i]
        max_index = i
        for j in range(i - 1, -1, -1):
            if maxval < arr[j]:
                maxval = arr[j]
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

print(selection_sort1([5, 3, -44, 1, 0, -12, 6, 7, 3, 10,  -12]))