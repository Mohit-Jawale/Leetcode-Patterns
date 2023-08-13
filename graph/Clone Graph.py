"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        old_to_new = {}
        def dfs(node):
            if not node:
                return None
            if node in old_to_new:
                return old_to_new[node]
            
            clone =  Node(node.val)
            old_to_new[node]= clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)              

        
        
