#  Given collection of distinct integers, return all possible permutations
#  no repititions
# input = [1,2,3]






def helper(input1, slate, result):
    if len(input1) == 0:
        result.append(slate[:])
        return result
    else:
        curr_choices = input1[:] # in order not to change the list using append and remove we are making copy.
        for choice in curr_choices:
            slate.append(choice)
            input1.remove(choice)
            helper(input1, slate, result)
            slate.pop()
            input1.append(choice)
    return result

def permutations(input1):
    return helper(input1, [], [])

print(permutations([1,2,3]))


# Swap and pop method

def helper1(input2, i, slate, result):
    if len(input2) == 0:
        result.append(slate[:])
        return
    else:
        for j in range(len(input2)): # order is maintained as swap is done.
            input2[j], input2[-1] = input2[-1], input2[j] # swap last with current element
            slate.append(input2.pop()) # remove last element
            helper1(input2, i + 1, slate, result)
            input2.append(slate.pop()) # append element at the last.
            input2[j], input2[-1] = input2[-1], input2[j] # swap current element with last. bringing to the same position.
    return result

def permutations1(input2):
    return helper1(input2, 0, [], [])

print(permutations1([1,2,3]))


# Even simpler swap method
def helper2(s, i, result):
    if i == len(s):
        result.append(s[:])
        return
    else:
        for j in range(i, len(s)):
            s[j], s[i] = s[i], s[j]
            helper2(s, i + 1, result)
            s[j], s[i] = s[i], s[j]
    return result

def permutations2(s):
    return helper2(s, 0, [])

print(permutations2([1,2,3]))
