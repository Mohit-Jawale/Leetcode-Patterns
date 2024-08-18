# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reversell(node):

            prev,curr = None,node

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr=next
            
            return prev
        

        head = reversell(head)
    
        tempHead = head
        dummyHead = ListNode(-1)
        temp = dummyHead
        carry = 0
        while tempHead:

            currNum = ((tempHead.val*2) + carry)%10
            carry = ((tempHead.val*2) + carry)//10

            temp.next = ListNode(currNum)
            temp=temp.next
            tempHead = tempHead.next
        
        if carry>0:
            temp.next = ListNode(carry) 
      
        head = reversell(dummyHead.next)
        return head



