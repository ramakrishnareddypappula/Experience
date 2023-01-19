
# number of subsets in a set:
# empty set is subset of every set.
# {} = {} = 1
# {a} = {0}, {a} = 2
# {a, b} = {0}, {a}, {b}, {a, b} = 4
# {a, b, c} = {}, {a}, {b}, {c}, {a, b}, {a, c}, {b, c}, {a, b, c} = 8
# n will have 2 ^ n subsets.


# decrease and conquer
# Time comlexity:  O(n)
def subsets(n):
    if n == 0:
        return 1
    else:
        return 2 * subsets(n - 1)

print(subsets(3))


# divide and conquer
# Time complexity :

# problem n is divided to 2 subproblems of (n-1), inturn 4 subproblems of (n-2) so on
# if n == 0, then 1
# if n == 1, then 2
# if n == 2, then 4
# if n == 3, then 8
# if n then O(2 ^ n)

def subsets1(n):
    if n == 0:
        return 1
    else:
        return subsets(n - 1) + subsets(n - 1) # It will be like a binary tree. at level 0, 1 element, level 1, 2 elements
                                                # level 2, 4 elements. level 3, 8 elements and so on.
                                                # level n will have 2^N elements.

print(subsets1(3))

