

# Time out error will occur.
# Time complexity = O(2 ^ n)
# Fib(5) -> Fib(4) Fib(3) -> fib(3) fib(2) , Fib(2) fib(1)
#
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))


# There will be no timeout error.
def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    b1 = 0
    b2 = 1
    if n == 0:
        return b1
    if n == 1:
        return b2
    i = 2
    while i <= n:
        b = b1 + b2
        b1 = b2
        b2 = b
        i += 1
    return b2

# memoization
from functools import lru_cache

@lru_cache(1000)
def fibonacci1(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci1(n - 1) + fibonacci1(n - 2)



print(fibonacci1(0))
print(fibonacci1(1))
print(fibonacci1(2))
print(fibonacci1(3))
print(fibonacci1(4))
print(fibonacci1(5))
print(fibonacci1(6))
print(fibonacci1(7))