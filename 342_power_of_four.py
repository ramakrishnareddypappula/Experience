class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<0):
            return False
        b = bin(n)
        if(b.count("1") == 1 and (b[3:].count("0")%2 == 0)):
            return True
        return False