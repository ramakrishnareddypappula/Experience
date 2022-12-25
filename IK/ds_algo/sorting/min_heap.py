
def heapify(arr, n, i):
    smallest = i
    left = 2 * i
    right = 2 * i + 1

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        heapify(arr, n, smallest)

def min_heap(arr):
    n = len(arr)

    for i in range(n/2 - 1, -1, -1):
        heapify(arr, n, i)


    # for i in range(n - 1, 0, -1):
    #     arr[i], arr[0] = arr[0], arr[i]
    #
    #     heapify(arr, i, 0)

    for i in range(1, n-1):
        arr[i], arr[n-1] = arr[n-1], arr[i]
        heapify(arr, n-1, i)
    return arr

arr = [5, 3, -44, 1, 0, -12, 6, 7, 3, 10,  -12]
print(min_heap(arr))
