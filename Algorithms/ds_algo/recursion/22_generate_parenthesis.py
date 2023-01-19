
# Given n pairs of parenthesis, write a function to generate all combinations of well formed parenthesis
# input n = 3
# output = ['((()))', '(()())', '(())()', '()(())', '()()()']

def helper(n, n_open, n_close, slate, result):
    if n_close == n:
        result.append("".join(slate))
        return
    else:
        if n_open < n:
            slate.append("(")
            helper(n, n_open + 1, n_close, slate, result)
            slate.pop()
        if n_close < n_open:
            slate.append(")")
            helper(n, n_open, n_close + 1, slate, result)
            slate.pop()

    return result

def overall(n):
    return helper(n, 0, 0, [], [])

print(overall(3))
print(overall(1))