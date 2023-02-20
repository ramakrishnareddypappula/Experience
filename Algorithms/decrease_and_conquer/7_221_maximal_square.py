

# 221. Maximal Square
#
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
# Input: matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
#                  ["1", "0", "0", "1", "0"]]
# Output: 4
#
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
#
# Input: matrix = [["0"]]
# Output: 0



# Intuition: Initially make 0th index of every row and column to 1 if matrix[row][col] == 1.
# Then iterate from 1st row and 1st col, if matrix[row][col] == 1, then get min of [row-1][col], [row-1][col-1], [row][col-1]

# Time = O(n * m)
# auxiliary = O(n * m)
class Solution:
    def maximalSquare(self, matrix):
        global_max = 0
        m = len(matrix) # rows
        n = len(matrix[0]) # cols
        table = [[0 for _ in range(n)] for _ in range(m)] # create a temp table.

        # 0th index in every row, make 1 in temp if value is "1".
        for row in range(m):
            if matrix[row][0] == "1":
                table[row][0] = 1
                global_max = 1

        # 0th index in every column, make 1 in temp if value is "1".
        for col in range(n):
            if matrix[0][col] == "1":
                table[0][col] = 1
                global_max = 1

        # After above operations, 0th indices in each row and col are 1 if "1" was there.

        # Now from 1th index in row and column, if 1 is found, check its previous row, column and diagonal above. If all of them are 1, then it becomes square. If any of them is 0, then total is 0. assign that value to table[row][col] and assign same to global_max
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == "1":
                    table[row][col] = 1 + min(table[row][col - 1], table[row - 1][col - 1], table[row - 1][col])
                    global_max = max(global_max, table[row][col])

        # global_max is the side. To calculate the area:  side * side.
        return global_max * global_max

