"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr = head

        dummyHead = Node(-1,None,None,None)

        ansHead = dummyHead

        prev = None

        stack = []

        while curr:

            ansHead.next = Node(curr.val,prev,None,None)
        
            if curr.child:
                if curr.next:### only put in stack if we will come back otherwise we will exit the exit condition of while
                    stack.append(curr)
                curr = curr.child
            else:
                if curr.next:
                    curr = curr.next
                else:
                    if stack:
                        curr = stack.pop()
                    curr = curr.next
            
            
            ansHead = ansHead.next
            prev = ansHead

        return dummyHead.next
            
        
