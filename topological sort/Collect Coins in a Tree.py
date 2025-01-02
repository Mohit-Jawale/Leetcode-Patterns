class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:

        ### step 1: select any vertex to start ?
        ####-> O(N^2) -> start with middle  
        #### even 1-2-3-4 - > two centers and odd -1-2-3 will have one center.

        #### 1.b -> how to find center of the tree?
        #### ->topological sort with onion peeling method

        #### step2: how would I know how many coins are there in the range <=2 from my curr pos?
        ### -> from curr pos I can look into th coins arr

        #### step3: which position to move from here so that ans is min?
        ####->>> 
        ### step4: when to stop the search ? base case -> all coins are collected

        ### step5 : return back or how far I'm from the start position? 
        ###-> maintain a var


        #### 

        if not edges:
            return 0

        n = len(coins)
        adjList = defaultdict(list)
    
        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
       

        ### find leaf node
        leaves = collections.deque([])
        
        for key,value in adjList.items():

            if len(value)==1:
                leaves.append(key)          
        

        for leaf in leaves:
            while len(adjList[leaf])==1 and coins[leaf]==0:
                adjNode = adjList[leaf].pop()
                del adjList[leaf]
                adjList[adjNode].remove(leaf)
                leaf = adjNode
        
        remaining_node = len(adjList)

        for _ in range(2):

            leaves = [node for node in adjList if len(adjList[node])==1]
            remaining_node-=len(leaves)

            for leaf in leaves:
                adjNode = adjList[leaf].pop()
                del adjList[leaf]
                adjList[adjNode].remove(leaf)
                if len(adjList)<2:
                    return 0

        return 2*(len(adjList)-1) 
        




        





        
