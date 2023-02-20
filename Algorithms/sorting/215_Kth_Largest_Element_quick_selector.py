


# 215. Kth Largest Element in an Array
#
# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# You must solve it in O(n) time complexity.
#
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
#
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4


def kth_smallest(arr, k):
    k = k - 1  # Algorithm is same. Here just k-1

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


print(kth_smallest([3, 4, 1, 2], 1))
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