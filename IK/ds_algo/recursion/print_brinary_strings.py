

# print binary strings of length n
# l = 0, ""
# l = 1, 0, 1
# l = 2 , 00, 01, 10, 11

def bshelper(num, slate, result):
    if num == 0:
        result.append(slate)
        return
    else:
        bshelper(num - 1, slate + "0", result)
        bshelper(num - 1, slate + "1", result)
    return result


def print_binary_strings(n):
    return bshelper(n, "", [])



print(print_binary_strings(2))