
# Given a base a and an exponent b. Your task is to find a^b. The value could be large enough. So, calculate ab % 1000000007.

# Brute force:
# Time complexity = O(b)
# Auxillary space = O(1) # 1 variable used.
# Space complexity = O(1) # func params are 2 integers which take O(1) space.

def a_power_b(a, b):
    result = 1
    for i in range(b):
        result = result * a % 1000000007
    return int(result)

print(a_power_b(2, 10))

# Basically a ^ b = a ^ ( b / 2 + b / 2 )
# b is odd = a ^ (b/2 + b/2 + 1)
# b is even = a ^ (b/2 + b/2)
# if b == 0 , return 1

# Time complexity = O(log b)
# Auxillary space = O(1)
# space complexity = O(1)


def a_power_b_1(a, b):
    if b == 0:
        return 1
    a = a  % 1000000007
    tmp = a_power_b_1(a, b//2)
    if b % 2 == 0:
        return tmp * tmp % 1000000007
    else:
        return tmp * tmp * a  % 1000000007

print(a_power_b_1(2, 10))