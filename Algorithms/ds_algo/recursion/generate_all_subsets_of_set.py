
# problem similar to 78_subsets.

#
# Generate ALL possible subsets of a given set. The set is given in the form of a string s containing distinct lowercase characters 'a' - 'z'.
#
# input:
# {
# "s": "xy"
# }
#
# output:
# ["", "x", "y", "xy"]


def helper(s, i, slate, result):
    if i == len(s):
        result.append("".join(slate[:]))
        return
    else:
        slate.append(s[i])
        helper(s, i+1, slate, result)
        slate.pop()
        helper(s, i+1, slate, result)
    return result

def generate_all_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    if s == "":
        return [""]
    return helper(s, 0, [], [])