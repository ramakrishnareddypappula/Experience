

# This will work for only non-negative integers.

def counting_sort(arr, position):
    l = len(arr)
    output = [0] * l
    bucket = [0] * 10
    for i in range(len(arr)):
        element = arr[i] // position
        bucket[element % 10] += 1
    for i in range(1, len(bucket)):
        bucket[i] = bucket[i] + bucket[i - 1]
    for k in range(len(arr) - 1, -1, -1):
        val = arr[k]
        e = val // position
        e1 = e % 10
        bucket[e1] -= 1
        output[bucket[e1]] = val
    for j in range(0, l):
        arr[j] = output[j]


def radix_sort(arr):
    maxval = max(arr)
    position = 1
    while maxval // position >= 1:
        counting_sort(arr, position)
        position *= 10

    return arr

print(radix_sort([201, 102, 504, 342, 798]))
print(radix_sort([201, 102, 504, 342, 798]))
print(radix_sort([1000, 1, 5, 100000, 4, 54, 6]))