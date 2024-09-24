# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        fast,slow = head,head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        dummyHead = ListNode(-1)
        dummyHead.next = slow
        
        if prev:
            prev.next = None

        
        prev,curr = None,dummyHead.next
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        dummyHead = prev


        while head and dummyHead:
            if head.val != dummyHead.val:
                return False
            head = head.next
            dummyHead = dummyHead.next
        
        return True
        
        
            




        
        
        
