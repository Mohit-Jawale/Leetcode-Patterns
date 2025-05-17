# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        queue = collections.deque([(root,0)])

        level_order_dict = collections.defaultdict(list)

        right_side_view = []

        while queue:

            node,level = queue.popleft()

            level_order_dict[level].append(node.val)

            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
        
        for level,nodes in level_order_dict.items():
            right_side_view.append(nodes[-1])
        
        return right_side_view
        

        
