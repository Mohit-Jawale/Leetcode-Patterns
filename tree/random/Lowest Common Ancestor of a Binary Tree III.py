"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        pPath, qPath = collections.deque([]), collections.deque([])

        def findRoot(node,path):
            path.appendleft(node)
            if node.parent == None:
                return node,path
            node,path = findRoot(node.parent,path)
            return node,path
        
        pRoot,pPath = findRoot(p,pPath)
        qRoot,qPath = findRoot(q,qPath)

        ans = []
        n =  len(qPath) if len(pPath)>len(qPath) else len(pPath)
        for i in range(n):
            if pPath[i] == qPath[i]:
                ans.append(pPath[i])
        return ans[-1]
        

        
        
