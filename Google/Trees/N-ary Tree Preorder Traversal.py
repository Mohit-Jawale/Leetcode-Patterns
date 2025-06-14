"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        pre_order = []

        def dfs(node):

            nonlocal pre_order

            if not node:
                return

            pre_order.append(node.val)
            
            for child in node.children:
                dfs(child)
        
        dfs(root)
        return pre_order
            


        
