
# Given a number n, generate all possible binary strings of length n.
#
# input:
# {
# "n": 3
# }
#
#
# output: ["000", "001", "010", "011", "100", "101", "110", "111"]

def helper(n, i, slate, result):
    if i == n:
        result.append("".join(slate[:]))
        return
    else:
        slate.append("0")
        helper(n, i + 1, slate, result)
        slate.pop()
        slate.append("1")
        helper(n, i + 1, slate, result)
        slate.pop()
    return result

def get_binary_strings(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    # Write your code here.
    #return []
    return helper(n, 0, [], [])

print(get_binary_strings(3))