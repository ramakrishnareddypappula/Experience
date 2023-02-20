
# print all decimal strings of length n.


def decimal_strings(n, str1):
    if len(str1) == n:
        print(str1)
    else:
        for i in range(10):
            decimal_strings(n, str1 + str(i))

decimal_strings(2, "")