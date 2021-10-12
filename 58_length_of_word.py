class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s = s.strip()
        # return len(s.split(" ")[-1])

        s = s.split(" ")
        for each in s[::-1]:
            if len(each):
                return len(each)