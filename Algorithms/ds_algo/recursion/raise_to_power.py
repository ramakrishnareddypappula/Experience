

# 2 ^ 4 = 2 * 2 * 2 * 2
# Time complexity = O(k)
# recursive solution
def raise_to_power(n, k):
    if k == 0:
        return 1
    else:
        return n * raise_to_power(n, k - 1)

print(raise_to_power(2, 4))


# iterative solution
# Time complexity = O(k)
def raise_to_power1(n, k):
    result = 1
    for i in range(k):
        result = result * n
    return result

print(raise_to_power1(2, 4))
