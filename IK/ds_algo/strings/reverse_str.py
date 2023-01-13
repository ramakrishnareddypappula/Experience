
# s = "my dog ran"
# output = "nar god ym"

# Time complexity = O(n)
# space complexity = O(n) # since python string is immutable
def string_rev(s):
    output = ""
    for i in range(len(s) - 1, -1, -1):
        output = output + s[i]

    return output

print(string_rev("my dog ran"))

# Time complexity = O(n)
# space complexity = O(n) # since python string is immutable
def string_rev1(s):
    output = ""
    for c in s:
        output = c + output

    return output

print(string_rev1("my dog ran"))

# mutable swap: 2 pointers, start and end. swap their values and increment start and decrement end. until start > end.
# This will have O(1) space complexity.