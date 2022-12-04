

def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    result = [0] * len(temperatures)
    stack = [] # (index, temparature)
    for index, temp in enumerate(temperatures): # (0, 73), (1, 74)
        while stack and temp > stack[-1][1]:
            stackindex, stacktemp = stack.pop()
            result[stackindex] = index - stackindex
        stack.append((index, temp))
    return result

print(dailyTemperatures([73,74,75,71,69,72,76,73]))