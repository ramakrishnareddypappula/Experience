
# quick sort

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def sorting(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        sorting(arr, low, p - 1)
        sorting(arr, p + 1, high)
    return arr


def quicksort(arr):
    h = len(arr)
    a = sorting(arr, 0, h - 1)
    return a



arr1 = [6,1,5,2,4]
arr2 = [6,1,5,-2,4]
arr3 = [5, 3, -44, 1, 0, -12, 6, 7, 3, 10,  -12]
print(quicksort(arr1))
print(quicksort(arr2))
print(quicksort(arr3))