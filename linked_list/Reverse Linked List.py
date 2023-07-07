#### Remember the concept of how cuur is going and saving the address in next and in next step updating its address in next step


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head

        while curr:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
            
        return prev    
