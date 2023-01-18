
# Given a stream of integers and window size, calculate the moving average of all integers in the window size.

# Example:
#
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) /2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3+ 5) / 3

# Data stream is different from array
# 1. In data stream, all values are not given in 1 shot.
# 2. Every time a new number is given, we have to re compute.
import collections
class Solution:
    def __init__(self, size):
        self.window_queue = collections.deque()
        self.maxsize = size
        self.total = 0

    def next(self, val):
        self.window_queue.append(val)
        self.total += val
        if len(self.window_queue) > self.maxsize:
            popped = self.window_queue.popleft()
            self.total -= popped

        return float(self.total) / len(self.window_queue)






