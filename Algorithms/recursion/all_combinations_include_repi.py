
# Given a string, return all permutations

def helper(alphabets, slate, results):
    if len(alphabets) == len(slate):
        results.append(slate[:])
        return
    else:
        for each in alphabets:
            helper(alphabets, slate + each, results)
    return results

def perm(alphabets):
    return helper(alphabets, "", [])


l = perm("abc") # ['aaa', 'aab', 'aac', 'aba', ...], total 27
print(l) # 3 ^ 3 = 27
print(len(l))
