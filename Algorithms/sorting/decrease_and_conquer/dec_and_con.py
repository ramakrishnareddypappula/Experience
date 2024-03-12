
# This function will return the max value = 5 by decreasing the list by half each time.
# after decreasing the length of list to 1, It compares the max values of sublists recursively. Which will return the max value. 

def decrease_and_conquer(x):
    if len(x) == 1:
        return x[0]
    mid = len(x) // 2
    left_list = x[:mid]
    right_list = x[mid:]
    
    left_max = decrease_and_conquer(left_list)
    right_max = decrease_and_conquer(right_list)
    
    return max(left_max, right_max)
    
x = [5, 1, 4, 1 , 2]
print(decrease_and_conquer(x))
