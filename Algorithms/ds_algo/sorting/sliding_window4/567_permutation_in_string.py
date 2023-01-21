

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
#
# example:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


# Create a dict out of s1. With len(s1) create another dict of s2.
# if both dicts keys and values are same, then s2 are a permutation of s1.
# from len(s1) to Len(s2), calculate by using sliding window.

# THIS TAKES LESS TIME.
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # initial check
        if len(s1) > len(s2):
            return False
        hmap_s1 = {}
        hmap_s2 = {}

        # Create dict1 out of s1
        for i in range(len(s1)):
            if s1[i] in hmap_s1:
                hmap_s1[s1[i]] += 1
            else:
                hmap_s1[s1[i]] = 1
        # Create dict2 out of s2 of len(s1)
        for i in range(len(s1)):
            if s2[i] in hmap_s2:
                hmap_s2[s2[i]] += 1
            else:
                hmap_s2[s2[i]] = 1
        if hmap_s1 == hmap_s2: # if dict1 == dict2: return True
            return True
        k = len(s1)
        # sliding window
        for i in range(k, len(s2)):
            hmap_s2[s2[i -k]] -= 1  # reduce value of left element
            if hmap_s2[s2[i -k]] == 0: # if val == 0, remove that element from dict.
                del hmap_s2[s2[i -k]]
            if s2[i] in hmap_s2: # Add the current element.
                hmap_s2[s2[i]] += 1
            else:
                hmap_s2[s2[i]] = 1
            if hmap_s1 == hmap_s2: # if dict1 == dict2: return True
                return True
        return False



# THIS TAKES MORE TIME.
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hmap_s1 = Counter(s1)
        hmap_s2 = Counter(s2[: len(s1)])
        if hmap_s1 == hmap_s2:
            return True
        k = len(s1)
        for i in range(k, len(s2)):
            hmap_s2[s2[i -k]] -= 1
            if hmap_s2[s2[i -k]] == 0:
                del hmap_s2[s2[i -k]]
            hmap_s2 = Counter(s2[i-k + 1: i + 1])
            if hmap_s1 == hmap_s2:
                return True
        return False