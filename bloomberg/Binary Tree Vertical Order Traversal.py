Binary Tree Vertical Order Traversal# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return None
        hashmap = defaultdict(list)

        queue = collections.deque([(root,0)])
        level = 0
        min_col = max_col = 0

        while queue:
            node,level = queue.popleft()

            hashmap[level].append(node.val)
            min_col = min(min_col,level)
            max_col = max(max_col,level)

            if node.left:
                queue.append((node.left,level-1))
            if node.right:
                queue.append((node.right,level+1))
        
        
        return [hashmap[i] for i in range(min_col,max_col+1)]


        
