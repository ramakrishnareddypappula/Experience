

def kth_smallest(arr, k):

    def partition(arr, low, high, k):
        pivot = arr[high]
        for i in range(low, high):
            if pivot >= arr[i]:
                arr[i], arr[low] = arr[low], arr[i]
                low += 1
        arr[high], arr[low] = arr[low], arr[high]
        if k > low:
            return partition(arr, low + 1, high, k)
        elif k < low:
            return partition(arr, 0, low - 1, k)
        else:
            return arr[k]

    return partition(arr, 0, len(arr) - 1, k - 1)   # Algorithm is same. Here just k-1


print(kth_smallest([3, 4, 1, 2], 2))
print(kth_smallest([-5, 10, 2, 4, 7, 9], 2))
print(kth_smallest([5, 4, 3, 2, 1], 2))
print(kth_smallest([5, 44, -3, -2, -1], 2))
print(kth_smallest([5, 0, -3, 0, -1], 2))
print(kth_smallest([5, 3, -44, 1, 0, -12, 6, 7, 3, 10,  -12], 11))


def kth_largest(arr, k):
    k = len(arr) - k   # here k = l(arr) - k

    def partition(arr, low, high, k):
        pivot = arr[high]
        for i in range(low, high):
            if pivot >= arr[i]:
                arr[i], arr[low] = arr[low], arr[i]
                low += 1
        arr[high], arr[low] = arr[low], arr[high]
        if k > low:
            return partition(arr, low + 1, high, k)
        elif k < low:
            return partition(arr, 0, low - 1, k)
        else:
            return arr[k]

    return partition(arr, 0, len(arr) - 1, k)

print(kth_largest([3, 4, 1, 2], 2))
print(kth_largest([-5, 10, 2, 4, 7, 9], 2))
print(kth_largest([5, 4, 3, 2, 1], 3))
print(kth_largest([5, 3, -44, 1, 0, -12, 6, 7, 3, 10,  -12], 1))