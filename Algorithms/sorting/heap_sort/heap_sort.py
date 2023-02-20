
# Max heap

def heapify(arr, n, i):
    largest = i
    left = 2 * i
    right = 2 * i + 1
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i], = arr[i], arr[largest]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n/2 - 1, -1, -1):   # After n/2 - 1 all are leaf nodes and don't to be heapfied.
        heapify(arr, n, i)          # if 5 elements, only 2 times heapify must be done.

    #  As it is max heap, swap first and last, and keep the last element, then heapify the remaining elements.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]

        heapify(arr, i, 0)



    return arr

arr1 = [6,1,5,2,4]
arr2 = [6,1,5,-2,4]
arr3 = [5, 3, -44, 1, 0, -12, 6, 7, 3, 10,  -12]
print(heap_sort(arr1))
print(heap_sort(arr2))
print(heap_sort(arr3))


