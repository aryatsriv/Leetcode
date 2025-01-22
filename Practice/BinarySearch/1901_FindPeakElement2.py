# 1901. Find a Peak Element II
# Solved
# Medium
# Topics
# Companies
# Hint
# A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.
# 
# Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].
# 
# You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
# 
# You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.
# 
#  
# 
# Example 1:
# 
# 
# 
# Input: mat = [[1,4],[3,2]]
# Output: [0,1]
# Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.
# Example 2:
# 
# 
# 
# Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
# Output: [1,1]
# Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
#  
# 
# Constraints:
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 500
# 1 <= mat[i][j] <= 105
# No two adjacent cells are equal.
# 
class Solution:
    def findMaxElement(self,mat,c):
        maxElement=mat[0][c]
        maxElementIndex=0
        for i in range(0,len(mat)):
            if mat[i][c]>maxElement:
                maxElement=mat[i][c]
                maxElementIndex=i
        
        return maxElementIndex

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        cs=0
        ce=len(mat[-1])

        while cs<=ce:
            mid=(cs+ce)//2
            maxElementIndex=self.findMaxElement(mat,mid)
            maxElement=mat[maxElementIndex][mid]
            left=mat[maxElementIndex][mid-1] if mid>0 else -1
            right=mat[maxElementIndex][mid+1] if mid<len(mat[0])-1 else -1   
            if left<maxElement and right<maxElement:
                return [maxElementIndex,mid]
            elif left>maxElement:
                ce=mid-1
            else:
                cs=mid+1
        
        return [-1,-1]