

# 1456. Maximum Number of Vowels in a Substring of Given Length
#
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
#
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
#
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
#
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'} # sets are faster than tuples as they are implemented using hash tables.
        local_max = 0
        # for k chars check vowels, if char is vowel, add + 1.
        for i in range(k):
            if s[i] in vowels:
                local_max += 1
        global_max = local_max

        # for remaining(k , len(s)) elements, if vowel add + 1 for current char and reduce - 1 for i-k element

        for i in range(k, len(s)):
            if s[i] in vowels:
                local_max += 1
            if s[i - k] in vowels:
                local_max -= 1
            global_max = max(global_max, local_max)
        return global_max

s = Solution()
print(s.maxVowels("abciiidef", 3))