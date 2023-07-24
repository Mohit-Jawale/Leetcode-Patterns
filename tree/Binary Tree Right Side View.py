# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def bfs(node):
            queue = []
            queue.append(node)
            ans = []
            while queue:
                n = len(queue)
                if queue[-1]:
                    ans.append(queue[-1].val)
                
                for i in range(n):
                    a = queue.pop(0)
                    if a and a.left:
                        queue.append(a.left)
                    if a and a.right:    
                        queue.append(a.right)
                      
            return ans

        return bfs(root)    
