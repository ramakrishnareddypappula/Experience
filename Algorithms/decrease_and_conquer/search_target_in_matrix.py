


# Given a matrix of numbers , each row elements are in ascending order.
# Find if target is present in the matrix.

# from right of row1, check value is greater or smaller or equal. If smaller, then check in that row. if greater, go to next row.

# T = O(n) + max length of 1 col = O(n) n = number of rows.
# s = O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        row_length = len(matrix)
        col_length = len(matrix[0])
        for i in range(row_length):
            row_ith_last = matrix[i][col_length - 1]
            if target == row_ith_last:
                return True
            elif target > row_ith_last:
                continue
            else:
                for j in range(col_length - 2 , -1 , -1):
                    if target == matrix[i][j]:
                        return True
                else:
                    return False
        return False

s = Solution()
print(s.searchMatrix([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]], 5)) # True
print(s.searchMatrix([[3,5, 8], [9,12, 15]], 12)) # True
print(s.searchMatrix([[3,5, 8], [9,12, 15]], 9)) # True
print(s.searchMatrix([[3,5, 8], [9,12, 15]], 6)) # False
print(s.searchMatrix([[3,5, 8], [9,12, 15]], 2)) # False
print(s.searchMatrix([[3,5, 8], [9,12, 15]], 16)) # False