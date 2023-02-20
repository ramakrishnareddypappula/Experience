
# Time complexity : O(n)
# space complexity : O(1)
def palindrome_number(num):
    temp = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = 10 * rev + digit
        num = num // 10
    if temp == rev:
        return True
    return False

print(palindrome_number(121))
print(palindrome_number(1221))
print(palindrome_number(1231))