
# 1100 find k-length substrings with no repeated characters.
# given a string, return the substrings of length k with no repeated characters.

# example: s = "havefunonleetcode", k = 5
# output = 6
# havef
# avefu
# vefun
# efuno
# etcod
# tcode


from collections import deque
def substring_no_repititions(s, k):
    max_count = 0
    if len(s) < k:
        return max_count
    first_k = deque(s[:k])
    if sorted(deque(set(first_k))) == sorted(first_k): # after deque(set()), the order is not maintained hence, sorted() is used.
        print("".join(first_k))
        max_count += 1
    for i in range(k, len(s)):
        first_k.popleft()
        first_k.append(s[i])
        if sorted(deque(set(first_k))) == sorted(first_k):
            print("".join(first_k))
            max_count += 1

    return max_count

print(substring_no_repititions("havefunonleetcode", 5))
print(substring_no_repititions("home", 5))



def substring_no_repititions1(s, k):
    max_count = 0
    if k > len(s):
        return max_count
    hmap = {}
    for i in range(k):
        if s[i] in hmap:
            hmap[s[i]] += 1
        else:
            hmap[s[i]] = 1
    if len(hmap) == k: # means everything char is unique.
        max_count += 1

    # First append the current char
    # reduce -1 to s[i-k] char
    # if s[i-k] == 0, remove from dict
    # calculate length
    for i in range(k, len(s)):
        if s[i] in hmap:
            hmap[s[i]] += 1
        else:
            hmap[s[i]] = 1
        hmap[s[i-k]] -= 1
        if hmap[s[i-k]] == 0:
            del hmap[s[i-k]]
        if len(hmap) == k:
            max_count += 1

    return max_count


print(substring_no_repititions1("havefunonleetcode", 5))
print(substring_no_repititions1("home", 5))
print(substring_no_repititions1("abcabcabcabc", 4))
print(substring_no_repititions1("abcdabcdabcdabcd", 4))