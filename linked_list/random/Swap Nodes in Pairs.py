# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode(-1)
        prev,curr = dummyNode,head

        while curr and curr.next:
            next = curr.next
            if next:
                curr.next = next.next
                next.next = curr
            prev.next = next
            prev = curr
            curr = prev.next

        return dummyNode.next  if dummyNode.next != None else head  
