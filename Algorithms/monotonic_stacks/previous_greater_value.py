

# PREVIOUS LARGE VALUE : for previous, iterate from left side, check >= only
# PREVIOUS SMALL VALUE : for previous, iterate from left side, check >= only
# NEXT LARGE VALUE : for next, iterate from right side. and then reverse at the end. check >= only
# NEXT SMALL VALUE : for next, iterate from right side. and then reverse at the end. check >= only

def previous_greater_value(values):
    stack = []
    result = []
    for i in range(len(values)):
        while stack and values[i] >= stack[-1]:
            stack.pop()
        if stack:
            result.append(stack[-1])
        else:
            result.append(0)
        stack.append(values[i])
    return result



values = [71, 60, 75, 52, 66, 99, 42, 44]
print(previous_greater_value(values))  # [0, 71, 0, 75, 75, 0, 99, 99]