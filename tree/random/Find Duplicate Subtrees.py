# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        count,duplicates = defaultdict(int),[]

        def dfs(node):
            if not node:
                return "."
            
            subtree = str(node.val) + '-' + dfs(node.left) + '-' + dfs(node.right)

            if count[subtree]==1:
                duplicates.append(node)
            count[subtree]+=1

            return subtree
        
        dfs(root)
        return duplicates

        
