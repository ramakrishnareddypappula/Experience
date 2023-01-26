

# PREVIOUS LARGE VALUE : for previous, iterate from left side, check >= only
# PREVIOUS SMALL VALUE : for previous, iterate from left side, check >= only
# NEXT LARGE VALUE : for next, iterate from right side. and then reverse at the end. check >= only
# NEXT SMALL VALUE : for next, iterate from right side. and then reverse at the end. check >= only


def next_smaller_value(values):
    stack = []
    result = []
    for i in range(len(values) - 1, -1, -1):
        while stack and stack[-1] >= values[i]:
            stack.pop()
        if stack:
            result.append(stack[-1])
        else:
            result.append(0)
        stack.append(values[i])
    result.reverse()
    return result


values = [71, 60, 75, 52, 66, 99, 42, 44]
print(next_smaller_value(values)) # [60, 52, 52, 42, 42, 42, 0, 0]