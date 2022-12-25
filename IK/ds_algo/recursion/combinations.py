
# Choose combinations
# C(n, k) = n!/ (n - k)! * k!

# If we choose 1 person, then out of n-1 persons, k-1 combinations can be formed.
# if we don't choose that person, then out n-1 persons, k combinations can be formed.

# base cases
# if n <= 1 , return 1
# if k == 0, return 1
# if k == n , return 1

def choose_combinations(n, k):
    if n <= 1 or k == 0 or k == n:
        return 1
    else:
        return choose_combinations(n-1, k-1) + choose_combinations(n-1, k)


print(choose_combinations(5, 2))