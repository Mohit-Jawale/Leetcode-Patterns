# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = [(0,root)] ###(index,root)
        ans = 0

        while queue:
            n = len(queue)

            temp = []

            for _ in range(n):
                index,node = queue.pop(0)
                temp.append(index)
                if node.left:
                    queue.append((2*index+1,node.left))
                if node.right:
                    queue.append((2*index+2,node.right))
            
            ans = max(ans,max(temp)-min(temp))
        
        return ans+1
        
