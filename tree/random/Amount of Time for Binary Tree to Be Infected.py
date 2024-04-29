# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:


        adjList = collections.defaultdict(list)

        def dfs(node):

            if not node:
                return
            
            dfs(node.left)
            if node.left:
                adjList[node.val].append(node.left.val)
                adjList[node.left.val].append(node.val)
            dfs(node.right)
            if node.right:
                adjList[node.val].append(node.right.val)
                adjList[node.right.val].append(node.val)

            return
        
        dfs(root)

        ##BFS

        queue = collections.deque([[start,0]])
        visited = set()
        maxMinutes = 0
        while queue:

            node,minutes = queue.popleft()
            maxMinutes = max(maxMinutes,minutes)
            if node in visited:
                continue

            visited.add(node)

            for neighbour in adjList[node]:
                if neighbour not in visited:
                    queue.append([neighbour,minutes+1])
        
        return maxMinutes
        




        
