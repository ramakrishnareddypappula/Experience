
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

from functools import lru_cache


class Solution:
    @lru_cache(1000) # sometimes timeout will occur. To avoid this memoization(caching) is done.
    def climbStairs(self, n: int) -> int:
        if n == 2:
            return 2
        if n == 1:
            return 1
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n-2)

s = Solution()
print(s.climbStairs(10))
