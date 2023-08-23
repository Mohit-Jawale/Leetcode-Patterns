class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:


        adj_list = defaultdict(list)
        start ="JFK"
        for i,j in tickets:
            adj_list[i].append(j)

        for key in adj_list:
            adj_list[key].sort()

        ans = []

        def dfs(start):
            while start in adj_list and adj_list[start]:
                dfs(adj_list[start].pop(0))
            ans.append(start)

        dfs(start)
        return ans[::-1]        

