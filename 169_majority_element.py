
# Time complexity = O(n)
# space complexity = O(n)

from collections import Counter


def majorityElement1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    d = Counter(nums)
    m_value = max(d.values())
    for i in d:
        if d[i] == m_value:
            return i

print(majorityElement1([3,2,3]))
print(majorityElement1([2,2,1,1,1,2,2]))

# Boyer moore algorithm: Time complexity: O(n) and space complexity: O(1)
# Algorithm:
# Step 1: Initialize 2 variables. value=list[0] and count=1.
# Step 2: from index 1, If value == list[index], increment count = 2
# Step 3: if value != list[index], decrement count -= 1.
# step 4: If count = 0, remove old value and assign current value value = list[i] and keep count to 1.

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    value = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if value == nums[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            value = nums[i]
            count = 1
    return value

print(majorityElement([3,2,3]))  # 3
print(majorityElement([2,2,1,1,1,2,2]))  # 2