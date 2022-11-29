
# For positive and negative values.

def counting_sort(arr):
    output = [0 for _ in range(len(arr))]
    minval = min(arr)
    maxval = max(arr)

    # create a temp list with 0 to max + 1 values.
    temp = [0 for _ in range(minval, maxval + 1)]

    # Whenever you see value in array, in temp list add +1 to that index.
    for i in range(len(arr)):
        temp[arr[i] - minval] += 1

    # from index 1 in temp list, add the previous values to current value and keep at that index.
    for j in range(1, len(temp)):
        temp[j] = temp[j] + temp[j - 1]

    # 1. Get the value from input array from right side.
    # 2. At that in temp array, reduce value by 1.
    # 3. the value that you get from above, at the index in output list, store the input value.
    for k in range(len(arr) - 1, -1, -1):
        val = arr[k]
        temp[val - minval] = temp[val- minval] - 1
        output[temp[val - minval]] = val
    return output

print(counting_sort([2, 10, 1, 3, 2]))
print(counting_sort([10, 0]))
print(counting_sort([10, 5, 4, 2, 1]))
print(counting_sort([4, 5, 2, 1, 0]))
print(counting_sort([-2, 0, -1, 5, -1]))
print(counting_sort([4000, -4000, 1]))
