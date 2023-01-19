

# input = "abcba"
# output = True

# input = "abebe"
# output = False

# Time complexity : O(n)
# space complexity : O(1)
def palindrome(s):
    s = s.lower()
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

print(palindrome("abcba"))
print(palindrome("abebe"))
print(palindrome("malayalam"))


def palindrome1(s):
    s = s.lower()
    return s == s[::-1]

print(palindrome("abcba"))
print(palindrome("abebe"))
print(palindrome("malayalam"))