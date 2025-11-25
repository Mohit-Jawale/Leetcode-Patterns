# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        ans = []

        def dfs(node,number):

            nonlocal ans

            if not node:
                return
            if not node.left and not node.right: ### this is imp bcz we will calculate the sum twice on root which we dont want
                ans.append(number+str(node.val))
                return 

            dfs(node.left,number+astr(node.val))
            dfs(node.right,number+str(node.val))
        

        dfs(root,"")
        total = 0
        for num in ans:
            total+=int(num)

        return total
            


        
