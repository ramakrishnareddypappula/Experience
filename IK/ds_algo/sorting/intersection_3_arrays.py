
# Given 2 sorted arrays, return the elements found in common.
# arr1 = [1,2,3,4,5, 9] arr2 = [1,2,5,7,9, 10].
# output = [1,2, 5]

#Brute force : For each value in arr1, iterate all elements in arr2. O(n ^ 2) for 2 arrays.


# 2 pointer approach: 1 pointer to each array. If values in both arrays are equal then add to list and increment both i and j.
# else if arr2 value is high then increment i, else if arr1 is high increment j.
# Time = O(n + m), space complexity = min(arr1, arr2)
def find_intersection(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    if not arr1:
        return [-1]
    if not arr2:
        return [-1]
    if not arr3:
        return [-1]
    def intersection(arr1, arr2):
        i = 0
        j = 0
        k = len(arr1) - 1 # 2
        l = len(arr2) - 1 # 3
        output = []
        while i <= k and j <= l:
            if arr1[i] == arr2[j]:
                output.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                i += 1
        return output
    out = intersection(arr1, arr2)
    out1 = intersection(out, arr3)
    return out1 if out1 else [-1]

print(find_intersection([1, 2, 2, 2, 9],[1, 1, 2, 2],[1, 1, 1, 2, 2, 2]))

