
#
# 240. Search a 2D Matrix II
#
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
#
# Input: matrix = [[1,4,7,11,15],
#                  [2,5,8,12,19],
#                  [3,6,9,16,22],
#                  [10,13,14,17,24],
#                  [18,21,23,26,30]], target = 5
#
# Output: true
#
# Input: matrix = [[1,4,7,11,15],
#                  [2,5,8,12,19],
#                  [3,6,9,16,22],
#                  [10,13,14,17,24],
#                  [18,21,23,26,30]], target = 20
# Output: false


# Time = O(m + n)
class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        row_length = len(matrix)
        col_length = len(matrix[0])
        min_row = 0
        max_col = col_length - 1
        # from right side and row = 0, if that value is greater, then whole row can be eliminated and increase row by 1.
        # else if value is small, whole column can be eliminated and decrease column by 1.
        while max_col >= 0 and min_row <= row_length - 1:
            if target == matrix[min_row][max_col]:
                return True
            elif target > matrix[min_row][max_col]:
                min_row += 1
            else:
                max_col -= 1
        return False
