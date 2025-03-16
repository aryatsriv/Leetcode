#101. Symmetric Tree
#Solved
#Easy
#Topics
#Companies
#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#
# 
#
#Example 1:
#
#
#Input: root = [1,2,2,3,4,4,3]
#Output: true
#Example 2:
#
#
#Input: root = [1,2,2,null,3,null,3]
#Output: false
# 
#
#Constraints:
#
#The number of nodes in the tree is in the range [1, 1000].
#-100 <= Node.val <= 100
# 
#
#Follow up: Could you solve it both recursively and iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def rec(left,right):
            if left==None and right==None:
                return True
            if left==None or right==None:
                return False
            if left.val==right.val:
                return rec(left.left,right.right) and rec(left.right,right.left)
            
            return False
        
        return rec(root.left,root.right)
