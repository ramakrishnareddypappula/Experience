

def replace_max_with_right(arr):
    for i in range(len(arr)):
        temp = arr[i]
        if i < len(arr) - 1:
            j = i + 1
            maxval = arr[j]
            while j < len(arr) - 1:
                if maxval < arr[j+1]:
                    maxval = arr[j + 1]
                j += 1
            arr[i] = maxval
        if i == len(arr) - 1:
            arr[i] = -1
    return arr

print(replace_max_with_right([17, 18, 5, 4, 6, 1]))

def replace_max_with_right1(arr):
    for i in range(len(arr)):
        if i < len(arr) - 1:
            maxval = max(arr[i + 1:])
            arr[i] = maxval
        if i == len(arr) - 1:
            arr[i] = -1
    return arr

print(replace_max_with_right1([17, 18, 5, 4, 6, 1]))

# new[0] = max(arr[1:5])
# new[1] = max(arr[2:5])
# new[0] = max(new[1], arr[1]])

# Step 1: iterate from right
# Step 2: initialize rightmax =  -1
# Step 3: newmax = max(rightmax, arr[i])

def replace_max_with_right2(arr):
    rightmax = -1
    for i in range(len(arr) -1, -1, -1):
        maxval = max(rightmax, arr[i])
        arr[i] = rightmax
        rightmax = maxval
    return arr

print(replace_max_with_right2([17, 18, 5, 4, 6, 1]))