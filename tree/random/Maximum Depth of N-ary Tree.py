"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:



        def dfs(node):

            if not node:
                return 0

            maxDepth = 1
            
            for next_node in node.children:

                maxDepth = max(dfs(next_node)+1,maxDepth)
            
            return maxDepth
        
        return dfs(root)

        
