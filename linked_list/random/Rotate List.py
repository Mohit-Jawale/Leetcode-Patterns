# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head
        ##step1 connect tail to head and count total elements
        temp = head
        count = 1
        while temp.next:
            temp = temp.next
            count+=1

        ##step2 assign tail to head and dummyNode to head
        temp.next = head
        temp = head
        prev = None
        
        ## step 3 reach the breaking point
        k = k % count

        for _ in range(count-k-1):
            temp = temp.next

        head = temp.next
        temp.next = None
        return head  



        
