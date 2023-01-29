
# 1176. Diet plan performance
#
# A dieter consumes calories[i] calories on the i-th day.
# Given an integer k, every consecutive sequence of k days(calories[i], calories[i+1], ..calories[i+k-1]
# for all 0<=i<=n-k) they look at T, the total calories consumed during the sequence of k days(calories[i], calories[i+1], ..calories[i+k-1])
#
# if T < lower : They lose 1 point
# if T > upper : They gain 1 point
# else no point.

# initially no calories. return the total calories.

# input calories= [3, 2], k=2, lower=0, upper=1
# output = 3 + 2 = 5 > upper . Hence 1 point.

# input calories = [1,2,3,4,5], k= 1, lower=3, upper=3
# output = 1 < 3(lower) = -1
# 2 < 3(lower) = -2
# 3 == 3(lower) = - 2
# 4 > 3(upper) = -1
# 5 > 3(upper) = 0

class Solution:

    def diet_plan(self, calories, k, lower, upper):
        first_k = calories[:k]
        total_calories = sum(first_k)
        dieter_points = 0
        if total_calories < lower:
            dieter_points -= 1
        elif total_calories > upper:
            dieter_points += 1
        for i in range(k, len(calories)):
            total_calories = total_calories + calories[i] - calories[i - k]
            if total_calories < lower:
                dieter_points -= 1
            elif total_calories > upper:
                dieter_points += 1
        return dieter_points

s = Solution()
print(s.diet_plan([1,2,3,4,5], 1, 3, 3))
print(s.diet_plan([3, 2], 2, 0, 1))
print(s.diet_plan([6, 5, 0,0], 2, 1, 5))

