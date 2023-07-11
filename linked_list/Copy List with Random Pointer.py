"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        prev = None
        curr = head
        copy_head = Node(-1)
        copy_curr = copy_head
        lookup = {}

        while curr:
            copy_curr.val = curr.val
            if curr.next != None:
                copy_curr.next = Node(-1)
            else:
                copy_curr.next = None    
            copy_curr.random = curr.random
            lookup[curr] = copy_curr
            
            copy_curr = copy_curr.next
            curr = curr.next
        
        temp = copy_head

        while temp:
            if temp.random != None:
                temp.random = lookup[temp.random]
            temp = temp.next
    
        return copy_head        


        
