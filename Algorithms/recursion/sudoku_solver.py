# input = [
# [8, 4, 9, 0, 0, 3, 5, 7, 0],
# [0, 1, 0, 0, 0, 0, 0, 0, 0],
# [7, 0, 0, 0, 9, 0, 0, 8, 3],
# [0, 0, 0, 9, 4, 6, 7, 0, 0],
# [0, 8, 0, 0, 5, 0, 0, 4, 0],
# [0, 0, 6, 8, 7, 2, 0, 0, 0],
# [5, 7, 0, 0, 1, 0, 0, 0, 4],
# [0, 0, 0, 0, 0, 0, 0, 1, 0],
# [0, 2, 1, 7, 0, 0, 8, 6, 5]
# ]
#
# output = [
#     [8, 4, 9, 1, 6, 3, 5, 7, 2],
#     [3, 1, 5, 2, 8, 7, 4, 9, 6],
#     [7, 6, 2, 4, 9, 5, 1, 8, 3],
#     [1, 5, 3, 9, 4, 6, 7, 2, 8],
#     [2, 8, 7, 3, 5, 1, 6, 4, 9],
#     [4, 9, 6, 8, 7, 2, 3, 5, 1],
#     [5, 7, 8, 6, 1, 9, 2, 3, 4],
#     [6, 3, 4, 5, 2, 8, 9, 1, 7],
#     [9, 2, 1, 7, 3, 4, 8, 6, 5]]

# Time complexity: O(9 ^ k) where k is number of unfilled cells. if 1 unfilled cell, then 9 numbers can be inserted
# Auxiliary space: O(k). k =unfilled cells. At every level of recursion fills one cell.
# Space complexity: O(n ^ 2), when n * n is board size. We can also say  O(1), where n = 9 always.

# is it safe to insert a number in a row, column.
def is_safe(board, row, col, num):
    for i in range(0, 9):
        if board[row][i] == num:
            return False

    for j in range(0, 9):
        if board[j][col] == num:
            return False

    # within a 3 * 3 ensure num is present only once.
    box_row_start = row - (row % 3)
    box_col_start = col - (col % 3)

    for i in range(box_row_start, box_row_start + 3):
        for j in range(box_col_start, box_col_start + 3):
            if board[i][j] == num:
                return False
    return True

def recursive_backtracking(board):
    row = 0
    col = 0
    found_unfilled_cell = False

    # check the board which has value = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                row = i
                col = j
                found_unfilled_cell = True
                break
        if found_unfilled_cell:
            break

    # if board with 0 is not found.
    if not found_unfilled_cell:
        return True

    # if board has 0, check if we can insert a number from 1 to 9.
    for num in range(1, 10):
        # is it safe to insert a number.
        if is_safe(board, row, col, num):

            # if yes, then update the board with that number.
            board[row][col] = num


            if recursive_backtracking(board):
                return True
            else:
                # if we insert 5. f does not lead to a solution. so we backtrack, insert to it so that it can be used again.
                board[row][col] = 0

    # if no solution is possible then return False.
    return False


def solve_sudoku_puzzle(board):
    recursive_backtracking(board)
    return board


board = [
[8, 4, 9, 0, 0, 3, 5, 7, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0],
[7, 0, 0, 0, 9, 0, 0, 8, 3],
[0, 0, 0, 9, 4, 6, 7, 0, 0],
[0, 8, 0, 0, 5, 0, 0, 4, 0],
[0, 0, 6, 8, 7, 2, 0, 0, 0],
[5, 7, 0, 0, 1, 0, 0, 0, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 2, 1, 7, 0, 0, 8, 6, 5]
]

print(solve_sudoku_puzzle(board))