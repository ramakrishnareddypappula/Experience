class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # time = O(n) , j will iterate n times.
        # space: O(min(m, n))
        count = 0
        i = 0
        dicta = {}
        for j in range(len(s)):
            if s[j] in dicta:
                i = max(dicta[s[j]], i)
            
            count = max(count, j - i + 1)
            dicta[s[j]] = j + 1
        return count
