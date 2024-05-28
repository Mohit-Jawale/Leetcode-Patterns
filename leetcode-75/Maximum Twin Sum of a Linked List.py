# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:


        stack = []  
        dummyHead = ListNode(-1,next = head)

        slow,fast = dummyHead , head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            stack.append(slow)
        
        slow = slow.next
        maxVal = -float('inf')
        while stack:
            top = stack.pop()
            maxVal = max(maxVal,top.val+slow.val)
            slow = slow.next
        
        return maxVal
            

      
        
