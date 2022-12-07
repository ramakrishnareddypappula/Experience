
# arr1 = [1,2,3,0,0], arr2 = [2, 5, 6]
# Time complextity = O(n log n), space complexity = O(n + m)
# Merge smallest array from the end to the largest array.
def merge_sorted_arrays(arr1, arr2):
    l1 = len(arr1) - 1
    l2 = len(arr2) - 1
    i = l1 if l1 < l2 else l2
    while i >= 0:
        arr1[l1], arr2[l2] = arr2[l2], arr1[l1]
        l1 -= 1
        l2 -= 1
        i -= 1

    return sorted(arr1) if len(arr1) >= len(arr2) else sorted(arr2)


print(merge_sorted_arrays([1,2,3,0,0, 0],[2, 5, 6]))
print(merge_sorted_arrays([1,2,3,-1, 0,0, 0],[2, 5, 6]))
print(merge_sorted_arrays([2, 5, 6], [1,2,3,0,0, 0]))
print(merge_sorted_arrays([2, 5, 6], [1,2,3,-1, 0,0, 0]))



# Wrong
def merge_sorted_arrays2(arr1, arr2):
    e2 = len(arr2) - 1
    e1 = len(arr1) - 1
    l = e1
    while l >= 0:
        if arr1[l] != 0:
            break
        l -= 1
    # import pdb
    # pdb.set_trace()
    while e2 >= 0 and e1 != l:
        if arr2[e2] > arr1[l]:
            arr1[e1] = arr2[e2]
            arr2[e2] = 0
           # arr2[e2], arr1[e1] = arr1[e1], arr2[e2]
            e2 -= 1
            e1 -= 1
        else:
            arr1[l + 1] = arr1[l]
            arr1[l] = 0
            #l -= 1
    return arr1



#print(merge_sorted_arrays2([1, 2, 3, 0, 0, 0], [2, 5, 6]))