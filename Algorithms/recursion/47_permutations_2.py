#
# Given a collections of numbers that might contain duplicates, return all possible unique permutations

# input = [1,1,2]

# we can solve using 46_permutations problem and then check if element is repeated ignore that. That way removing duplicate elements.

# Below returning error.

from collections import Counter

#@dataclass
class ValCount:
    val = 0
    n_avail = 0

def helper(S: list[ValCount], slate: list[int], result: list[list[int]]):
    if len(S) == 0:
        result.append(slate[:])
        return
    else:
        for i in range(len(S)):
            entry = S[i]
            entry.n_avail -= 1
            if entry.n_avail == 0:
                S[-1], S[i]= S[i], S[-1]
                S.pop()
            slate.append(entry.val)

            helper(S, slate, result)
            slate.pop()
            if entry.n_avail == 0:
                S.append(entry)
                S[-1], S[i] = S[i], S[-1]
            entry.n_avail += 1
    return result

def overall(S):
    return helper([ValCount(k,v) for k, v in Counter(S).items()], [], [])

print(overall([1,1,2]))