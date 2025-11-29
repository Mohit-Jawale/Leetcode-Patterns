"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        if not head:
            head = Node(val = insertVal)
            head.next = head ##3 edge case to make list circular
            return head
        
        curr = head

        while True:

            nxt = curr.next

            if curr.val<=insertVal<=nxt.val:
                break
            
            elif curr.val > nxt.val:
                if insertVal>=curr.val or insertVal<=nxt.val:
                    break
            
            curr = nxt
            if curr == head: ### to insert if only one num is there
                break


        newNode = Node(insertVal,curr.next)
        curr.next = newNode

        return head

