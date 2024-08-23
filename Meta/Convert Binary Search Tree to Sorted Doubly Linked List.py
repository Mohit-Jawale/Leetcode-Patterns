"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""



class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None
            
        head = Node(-1001)
        temp = head
        def dfs(node):
            nonlocal temp
            if not node:
                return 
            
            dfs(node.left)
            prev = temp
            temp.right = Node(node.val)
            temp = temp.right
            temp.left = prev
            dfs(node.right)

            return temp
        
        tailNode = dfs(root)
        tailNode.right = head.right
        head.right.left = tailNode

        return head.right

        
        
