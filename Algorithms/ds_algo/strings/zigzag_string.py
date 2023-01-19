
# A word can be written in a vertical zigzag fashion in a given number of lines, e.g. KICKSTART in three lines looks like this:

# letters of kickstart are written in Z shape horizontally. nlines is number of rows.
# K     S    T
# I  K  T  R
# C     A


# Intuition
# Create a dictionary of length as nlines. keys are numbers(1,2,3) and values are strings append.
# Iterate through every character
# Initialize 2 variables, top -> points to top row and row -> points to current row
# First "K" is placed in row 1 and row is incremented to 2.
# "I" is placed in row 2 and row is incremented to 3.
# "C" is placed in row 3. Now row is not less than nlines, so row is decremented to 2 and top is made false.
# "K" is placed in row 2, since top is still false, row is decremented to 1.
# "S" is placed in row 1, Now row == 1 and hence again row is incremented to 2 and top=True.
# similarly.

# Time complexity is O(N)
# space complexity = O(2 * N) # for dict and result = O(N)

def zigzag(nlines, word):
    """
    Args:
     nlines(int32)
     word(str)
    Returns:
     str
    """
    # Write your code here.
    # return ''
    if nlines == 1:
        return word

    d = {row : "" for row in range(1, nlines + 1)}
    top = True
    row = 1
    for letter in word:
        d[row] += letter
        if (row == 1) or (row < nlines and top == True):
            row += 1
            top = True
        else:
            row -= 1
            top = False

    result = ""
    for key in d:
        result += d[key]

    return result