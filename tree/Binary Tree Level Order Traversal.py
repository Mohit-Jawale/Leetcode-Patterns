#### Think and write
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def bfs(node):
            queue = []
            queue.append(node)
            level_order = []

            while queue:
                temp = []
                n = len(queue)
                for i in range(n):
                    if queue[i]:
                        temp.append(queue[i].val)

                if temp:
                    level_order.append(temp)
                
                for i in range(n):
                    a = queue.pop(0)
                    if a:
                        queue.append(a.left)
                        queue.append(a.right)
            return level_order

        return bfs(root)        

        
