#54. Spiral Matrix
#Solved
#Medium
#Topics
#Companies
#Hint
#Given an m x n matrix, return all elements of the matrix in spiral order.
#
# 
#
#Example 1:
#
#
#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [1,2,3,6,9,8,7,4,5]
#Example 2:
#
#
#Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#
#Constraints:
#
#m == matrix.length
#n == matrix[i].length
#1 <= m, n <= 10
#-100 <= matrix[i][j] <= 100

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,r,t,b=0,len(matrix[0])-1,0,len(matrix)-1
        res=[]
        while l<=r and t<=b:
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t+=1
            
            for i in range(t,b+1):
                res.append(matrix[i][r])
            r-=1

            if t<=b:
                for i in range(r,l-1,-1):
                    res.append(matrix[b][i])
                b-=1

            if l<=r:
                for i in range(b,t-1,-1):
                    res.append(matrix[i][l])
                l+=1

        return res

