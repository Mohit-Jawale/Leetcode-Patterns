#### imagine there is number line with root at 0, for left -1 and for right +1 dist way as we traverse the tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        vOrder = defaultdict(list)
        queue = collections.deque([[root,0]])

        while queue:
            node,dist = queue.popleft()

            vOrder[dist].append(node.val)
        
            if node.left:
                queue.append([node.left,dist-1])
            if node.right:
                queue.append([node.right,dist+1])
        
        sorted_dict = dict(sorted(vOrder.items()))

        return sorted_dict.values()
        
