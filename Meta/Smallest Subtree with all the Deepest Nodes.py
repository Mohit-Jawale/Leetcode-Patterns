# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        ## smallest subtree -> all the deepest nodes 

        ### depth 0->1->2->3  bfs with parent node in queue

        
        graph = {}

        queue = collections.deque([root])
    
        while queue:

            n = len(queue)
            A,B = queue[0],queue[-1]

            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    graph[node.left]=node
                if node.right:
                    queue.append(node.right)
                    graph[node.right]=node

        while A != B:
            A = graph[A]
            B = graph[B]
        
        return A
        
            

