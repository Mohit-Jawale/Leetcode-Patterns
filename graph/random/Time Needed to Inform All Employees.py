### this is dfs -:Time taken to reach all nodes or share information to all graph nodes type question
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        adjList = defaultdict(list)

        for empID,managerID in enumerate(manager):

            adjList[managerID].append(empID)
        
        ans = 0

        def dfs(empID,currTime):

            nonlocal ans

            if empID not in adjList:
                return

            currTime+=informTime[empID]
            ans = max(currTime,ans)

            for empoyessID in adjList[empID]:
                dfs(empoyessID,currTime)

        
        dfs(headID,0)
        return ans

        
        
