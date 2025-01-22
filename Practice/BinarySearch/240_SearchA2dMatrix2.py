# 240. Search a 2D Matrix II
# Solved
# Medium
# Topics
# Companies
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
 

# Example 1:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
# Example 2:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -109 <= matrix[i][j] <= 109
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -109 <= target <= 109


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)-1
        m=len(matrix[0])-1
        r=0
        c=m

        while r<=n and c>=0:
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                c=c-1
            else:
                r=r+1