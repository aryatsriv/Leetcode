#19. Remove Nth Node From End of List
#Solved
#Medium
#Topics
#Companies
#Hint
#Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# 
#
#Example 1:
#
#
#Input: head = [1,2,3,4,5], n = 2
#Output: [1,2,3,5]
#Example 2:
#
#Input: head = [1], n = 1
#Output: []
#Example 3:
#
#Input: head = [1,2], n = 1
#Output: [1]
# 
#
#Constraints:
#
#The number of nodes in the list is sz.
#1 <= sz <= 30
#0 <= Node.val <= 100
#1 <= n <= sz

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        curr=head
        count=0
        while curr and count<n:
            curr=curr.next
            count+=1

        if count!=n:
            return dummy.next

        prev=dummy
        while curr:
            curr=curr.next
            prev=prev.next

        prev.next=prev.next.next

        return dummy.next
        
