class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        

        adjList = collections.defaultdict(set)
        indegree = collections.defaultdict(int)


        for i in recipes+supplies:
            adjList[i]
            indegree[i]

        for r in range(len(recipes)):
            for ingredient in ingredients[r]:
                adjList[ingredient].add(recipes[r])
                indegree[recipes[r]]+=1
        
        queue = collections.deque([])

        for key, value in indegree.items():
            if value==0:
                queue.append(key)
        
        ans = []

        while queue:
            node = queue.popleft()
            if node in recipes:
                ans.append(node)
            for neighbour in adjList[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
        

        return ans




