# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        fslow,ffast,bslow,bfast = head,head,head,head

        for _ in range(k-1):
            ffast = ffast.next

        bslow,bfast = fslow,ffast
        
        while bfast.next:
            bslow = bslow.next
            bfast = bfast.next

        bslow.val,ffast.val = ffast.val,bslow.val
        return head   
