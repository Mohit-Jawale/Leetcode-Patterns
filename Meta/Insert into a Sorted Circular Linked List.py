"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        ### that head is not the start 
        ### find the breaking point or start point
        ### pos-pos,nega,negat

        if not head:
            head = Node(insertVal)
            head.next = head
            return head

        prev,curr = head,head.next
        toInsert = False

        while True:

            if prev.val<=insertVal<=curr.val:
                toInsert = True

            elif prev.val>curr.val:
                if insertVal>=prev.val or insertVal<=curr.val:
                    toInsert=True
            if toInsert:
                prev.next = Node(insertVal,curr)
                return head
            
            prev,curr = curr, curr.next

            if prev == head:
                break
        
        prev.next = Node(insertVal,curr)
        return head
            
