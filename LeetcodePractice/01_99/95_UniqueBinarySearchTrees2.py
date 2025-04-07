#95. Unique Binary Search Trees II
#Solved
#Medium
#Topics
#Companies
#Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
#
# 
#
#Example 1:
#
#
#Input: n = 3
#Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
#Example 2:
#
#Input: n = 1
#Output: [[1]]
# 
#
#Constraints:
#
#1 <= n <= 8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
    (1,4)

        def generate(left,right):
            if left>right:
                return [None]
            if left==right:
                return [TreeNode(left)]
            res=[]
            for i in range(left,right+1):
                for leftTree in generate(left,i-1):
                    for rightTree in generate(i+1,right):
                        res.append(TreeNode(i,leftTree,rightTree))
            return res
        return generate(1,n)
    
