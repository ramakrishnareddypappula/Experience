
class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        max_val = sum(customers[:minutes])
        total_max = max_val
        low = 0
        high = minutes
        for i in range(minutes, len(customers)):
            max_val = max_val + customers[i] - customers[i - minutes]
            if max_val > total_max:
                total_max = max_val
                low = i - minutes
                high = i
        print(total_max)
        print(low)
        print(high)
        print("*****")
        total_sum = 0
        for j in range(0, low):
            if grumpy[j] == 0:
                total_sum = total_sum + customers[j]
        print(total_sum)
        for m in range(high , len(customers)):
            if grumpy[m] == 0:
                total_sum = total_sum + customers[m]
        return total_sum + total_max



s = Solution()
#print(s.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))
print(s.maxSatisfied([1], [0], 1))