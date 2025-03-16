#82. Remove Duplicates from Sorted List II
#Solved
#Medium
#Topics
#Companies
#Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
#
# 
#
#Example 1:
#
#
#Input: head = [1,2,3,3,4,4,5]
#Output: [1,2,5]
#Example 2:
#
#
#Input: head = [1,1,1,2,3]
#Output: [2,3]
# 
#
#Constraints:
#
#The number of nodes in the list is in the range [0, 300].
#-100 <= Node.val <= 100
#The list is guaranteed to be sorted in ascending order.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy

        while head:
            temp=head
            addTemp=True
            head=head.next
            while head and head.val==temp.val:
                addTemp=False
                head=head.next

            if addTemp:
                curr.next=temp
                curr=curr.next
            
        
        curr.next=None
        return dummy.next



