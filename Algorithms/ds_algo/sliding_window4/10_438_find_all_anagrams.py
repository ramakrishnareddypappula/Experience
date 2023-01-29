
# 438. Find All Anagrams in a String
#
# Given two strings s and p, return an array of all the start indices of
# p's anagrams in s. You may return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly once.
#
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
# Input: s = "abab", p = "ab"
# Output: [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

class Solution:
    def findAnagrams(self, s: str, p: str):
        output = []
        if len(s) < len(p):
            return output
        d1 = {}
        d2 = {}
        for i in range(len(p)):
            if p[i] in d1:
                d1[p[i]] += 1
            else:
                d1[p[i]] = 1
        for i in range(len(p)):
            if s[i] in d2:
                d2[s[i]] += 1
            else:
                d2[s[i]] = 1
        if d1 == d2:
            output.append(0)
        k = len(p)
        for i in range(k, len(s)):
            d2[s[i - k]] -= 1
            if d2[s[i - k]] == 0:
                del d2[s[i-k]]
            if s[i] in d2:
                d2[s[i]] += 1
            else:
                d2[s[i]] = 1
            if d1 == d2:
                output.append(i - k + 1)
        return output