# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:



        def dfs(pre,ind):

            if not pre:
                return None
            if not ind:
                return None     

            root = pre.pop(0)
            node = TreeNode(root)    
    
            node.left = dfs(pre,ind[:ind.index(root)])
            node.right = dfs(pre,ind[ind.index(root)+1:])
            
            return node
         
        return dfs(preorder, inorder)


             
        
