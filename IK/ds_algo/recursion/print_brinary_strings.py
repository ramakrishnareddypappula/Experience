

# print binary strings of length n
# l = 0, ""
# l = 1, 0, 1
# l = 2 , 00, 01, 10, 11

def bshelper(num, slate):
    # import pdb
    # pdb.set_trace()
    if num == 0:
        print(slate)
    else:
        bshelper(num - 1, slate + "0") #
        bshelper(num - 1, slate + "1")


def print_binary_strings(n): #
    bshelper(n, "")



print_binary_strings(2)