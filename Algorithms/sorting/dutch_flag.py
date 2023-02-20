
# Arrage letters should R is first then G then B.

def dutch_flag_sort(balls):
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    i = 0
    j = len(balls) - 1  # 7
    k = 0
    while i <= j:
        if balls[i] != "R":
            i += 1
        else:
            balls[i], balls[k] = balls[k], balls[i]
            k += 1
            i += 1
    m = k
    print(k)
    while m <= j:
        if balls[m] != "G":
            m += 1
        else:
            balls[m], balls[k] = balls[k], balls[m]
            k += 1
            m += 1
    return balls

print(dutch_flag_sort(["G", "B", "G", "G", "R", "B", "R", "G"]))