

# Explanation in strings.txt

# Time complexity = O(N)
# space complexity = O(1)
def kadane(list_num):
    local_max = list_num[0]
    global_max = list_num[0]
    for i in range(1, len(list_num)):
        local_max = max(list_num[i], list_num[i] + local_max)
        global_max = max(global_max, local_max)
    return global_max

print(kadane([1,3,-2,-1, 5]))
