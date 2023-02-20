
# Solution 1: Brute force(bubble sort). For each element iterate over all the elements. Time complexity is O(n2).

# Solution 2 : Time is O(n), Space is O(n) dict.
def twosum1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Time complexity is O(n) since we need to iterate for n elements.
    # Space complexity is O(n) since dict of is created with atmost n elements.
    d = {}
    for index, value in enumerate(nums):
        act_val = target - value
        if act_val in d: # O(1)
            return d[act_val], index
        else:
            d[value] = index
    return False

print(twosum1([4, 9, 6,5], 10))

# Solution 3: Time = O(n), space = O(n)
def twosum2(a, target):
    nums = sorted(a)
    i = 0
    j = len(nums) - 1
    while i <= j:
        if nums[i] + nums[j] == target:
            return a.index(nums[i]), a.index(nums[j])
        elif nums[i] + nums[j] > target:
            j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
    return False

print(twosum2([4, 9, 6, 5], 10))