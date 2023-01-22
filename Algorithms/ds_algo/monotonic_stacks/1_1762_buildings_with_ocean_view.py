
# 1762 : Building with ocean view.
# There are n buildings of height h.
# The ocean is right of buildings.
# The building has ocean view if the building is without obstructions.
# Formally, the building has ocean view if all the buildings to its right have smaller height
# return the index of those buildings.
#
# input : [4,2,3,1]
# output :[0, 2, 3]  # indices
#
# input : [4,3, 2,1]
# output : [0, 1, 2, 3]
#
# input : [1,3,2,4]
# output : [3]

# Naive way: working fine.
# Time complexity = O(n)
def ocean_view(building_heights):
    output = []
    output.append(len(building_heights) - 1) # right most building always has ocean view.
    max_h = building_heights[-1]
    for i in range(len(building_heights) - 2, -1, -1): # ignore the right most building.
        if building_heights[i] > max_h:
            output.append(i)
            max_h = building_heights[i]
    output.reverse() # O(n)   # arrange is sorted order.
    return output

print(ocean_view([4,2,3,1]))
print(ocean_view([4,3, 2,1]))
print(ocean_view([1,3,2,4]))
print(ocean_view([4,3,3,3,1]))

# optimal: with stacks
# time = O(n)
# space = O(n) # result.
# auxillary space: stack = O(n)
def ocean_view1(heights):
    stack = []
    for i in range(len(heights)):
        while stack and heights[i] >= stack[-1][0]:
            stack.pop()
        stack.append((heights[i], i))
    result = []
    for i in range(len(stack)):
        result.append(stack[i][1])
    return result

print(ocean_view1([4,2,3,1]))
print(ocean_view1([4,3, 2,1]))
print(ocean_view1([1,3,2,4]))
print(ocean_view1([4,3,3,3,1]))



