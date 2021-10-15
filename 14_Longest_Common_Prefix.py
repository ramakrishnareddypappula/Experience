class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        com_prefix = ""
        if not strs:
            return com_prefix
        index = 0
        for c in strs[0]:
            for i in range(1, len(strs)):
                if index >= len(strs[i]) or c != strs[i][index]:
                    return com_prefix
            com_prefix += c
            index += 1
        return com_prefix