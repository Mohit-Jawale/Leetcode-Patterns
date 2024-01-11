# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        numbers = []
        def dfs(node,number):

            if not node:
                return
   
            if not node.left and not node.right:
                numbers.append(number+str(node.val))
                return 
            
            dfs(node.left,number+str(node.val))
            dfs(node.right,number+str(node.val))

            return 
        
        dfs(root,"")
        ans = 0
        for number in numbers:
            ans+=int(number)
        return ans            
            
        
