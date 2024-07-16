# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def dfs(left,right):

            if left == right:
                return [TreeNode(left)]
            if left>right:
                return [None]

            result = []
            ### here if you think the order of leftsubtree and rightsubtree doesnt matter
            for val in range(left,right+1):

                for rightsubtree in dfs(val+1,right):
                    for leftsubtree in dfs(left,val-1):
                    
                        root = TreeNode(val,leftsubtree,rightsubtree)
                        result.append(root)
            
            return result

        return dfs(1,n)


            

        
