

# example: at 0th index if 0 is not present, then swap element at 0th index with 0 until 0 is at 0th index.
def cycle_sort(nums):
    for i in range(len(nums)):
        while nums[i] != i:
            d = nums[i]  # number that needs to be swapped with that number.
            if d < len(nums):  # prevention check : example, len(nums) = 9, nums[9] will become index not in range exception.
                nums[i], nums[d] = nums[d], nums[i]
            else:
                break
    return nums

# It should start from 0 always.
print(cycle_sort([3, 4, 2, 5, 1, 0]))
print(cycle_sort([3, 4, 2, 1, 0]))


def cycle_sort1(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1:
            d = nums[i] - 1 # number that needs to be swapped with that number.
            if d < len(nums):  # prevention check : example, len(nums) = 9, nums[9] will become index not in range exception.
                nums[i], nums[d] = nums[d], nums[i]
            else:
                break
    return nums

print(cycle_sort1([3, 4, 2, 5, 1]))