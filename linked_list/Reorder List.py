# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = None
        slow.next = None

        while second:
            Next = second.next
            second.next = prev
            prev = second
            second = Next

        left,right = head, prev

        while right:
            temp1,temp2 = left.next,right.next
            left.next = right
            right.next = temp1
            left = temp1
            right = temp2

        
        
        


       
  










