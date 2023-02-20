

def online_median(stream):
    """
    Args:
     stream(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    #return []
    output = []
    for i in range(len(stream)):
        l = stream[:i+1]
        if len(l) % 2 == 1:
            k = (len(l) // 2) # [3, 8, 5]
            l.sort()
            output.append(l[k])
        else:
            k = len(l)//2
            l.sort()
            p = (l[k] + l[k-1]) // 2
            print(p)
            output.append(p)
    return output


print(online_median([3, 8, 5, 2]))