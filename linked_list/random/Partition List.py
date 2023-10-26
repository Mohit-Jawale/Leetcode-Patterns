# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        dummyHead1 = ListNode(-1)
        dummyHead2 = ListNode(-1)
        beforeDummyNode = dummyHead1
        afterDummyNode =  dummyHead2

        temp = head
        while temp:
            if temp.val<x:
                beforeDummyNode.next = temp
                beforeDummyNode = beforeDummyNode.next
            else:
                afterDummyNode.next = temp
                afterDummyNode = afterDummyNode.next

            temp= temp.next

        beforeDummyNode.next = dummyHead2.next
        afterDummyNode.next = None
        return dummyHead1.next
        
