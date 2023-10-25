# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        def reverseList(head):

            curr,prev = head,None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            return prev
        leftHead,rightTail = head,head
        leftPrev,rightPrev = None,None
        for _ in range(left-1):
            leftPrev = leftHead
            leftHead = leftHead.next

        for _ in range(right):
            rightPrev = rightTail
            rightTail = rightTail.next

        rightPrev.next = None
        reverseHead = reverseList(leftHead)


        if leftPrev:
            leftPrev.next = reverseHead
        else:
            head = reverseHead    

        if leftHead:   
            leftHead.next = rightTail

        return head 


        
