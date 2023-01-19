
# Brute force algorithm

# Time complexity = O(s) * O(s - p) = O(n) * O(n) = O(n ^ 2)
def substring(s, p):
    for i in range(len(s)):
        for j in range(len(p)):
            if s[i + j] != p[j]:
                break
        if j == len(p) - 1:
            return True
    return False

print(substring("abcdefg", "efg"))
print(substring("abcdefg", "exfg"))