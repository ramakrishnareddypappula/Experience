
# Given string S, transform every letter to lower case or uppercase and create string.

# example: s = "a1b2"
# output = ["a1b2", "A1b2", "a1B2", "A1B2"]

# s = ["3z4"]
# output = ["3z4", "3Z4"]

# Solution:
# - If letter, then there are 2 cases 1) upper case and 2) lower case
# - if digit, then there is only 1 case.
# - A slate is for partial solution.


# Time complexity: slate will have O(N) for n decisions. But in worst case, if all strings(abc) are given, then the
# result will be a binary tree which will have O(2 ^ N). Then total will be O(N 2 ^ N)
# In general Total is O(2 ^ N).

# space complexity: Input, axillary, output
# input = input
# axillary = slate = O(N ^ 2)
# output = results = O(2 ^ N)

# Total space complexity = O(N ^ 2)

# Immutable slate
def helper(input1, i, slate, results):
    if len(input1)== i:
        results.append(slate[:])
    else:
        character = input1[i]
        if character.isalpha():
            helper(input1, i + 1, slate + chr(ord(character) - 32), results)
        helper(input1, i + 1, slate + character, results)

    return results

def letter_case_permutation(input1):
    return helper(input1, 0, "", [])

print(letter_case_permutation("a1b2"))
print(letter_case_permutation("3z4"))

# mutable slate: To improve the space complexity
# space complexity = O(N)
def helper_mut(input2, i, slate, results):
    if i == len(input2):
        results.append("".join(slate[:])) #  [['A', '1', 'B', '2'], ['A', '1', 'b', '2'], ['a', '1', 'B', '2'], ['a', '1', 'b', '2']]
        return
    else:
        character = input2[i]
        if character.isalpha():
            slate.append(character.upper())   # upper case
            helper_mut(input2, i + 1, slate, results)
            slate.pop()
        slate.append(character.lower())  # lower case or letter.
        helper_mut(input2, i + 1, slate, results)
        slate.pop()
    return results



def letter_case_permutation_mut(input2):
    return helper_mut(input2, 0, [], [])

print(letter_case_permutation_mut("a1b2"))
print(letter_case_permutation_mut("3z4x"))