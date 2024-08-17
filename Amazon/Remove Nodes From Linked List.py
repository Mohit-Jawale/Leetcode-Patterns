# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseLL(node):
            
            curr,prev = node,None

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
    
            return prev


        head = reverseLL(head)

        curr = head

        prev = ListNode(-float('inf'))

        while curr:
            if curr.val>=prev.val:
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next
        

        return reverseLL(head)
