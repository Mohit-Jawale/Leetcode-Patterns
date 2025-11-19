# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(node,minValue,maxValue):

            if not node:
                return True
            
            if not(node.val>minValue and node.val<maxValue):
                return False
            

            leftIsValidBST = dfs(node.left,minValue,node.val)
            rightIsValidBST = dfs(node.right,node.val,maxValue)


            return leftIsValidBST and rightIsValidBST
        

        return dfs(root,-float('inf'),float('inf'))




                
        
