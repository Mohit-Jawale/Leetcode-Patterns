# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummyHead = ListNode(-1,next = head)
        slow,fast = dummyHead,head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummyHead.next
        
