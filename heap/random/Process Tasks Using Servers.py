class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        

        for index,server in enumerate(servers):
            servers[index]= [server,index]

        heapq.heapify(servers)
        processingServers = []
        ans = []
        time,i = 0,0
        for task in tasks:
        
            while processingServers and processingServers[0][0]<=time:
                pt,serverWeight,index = heapq.heappop(processingServers)
                heapq.heappush(servers,[serverWeight,index])
  
            if servers:
                serverWt,index = heapq.heappop(servers)
                heapq.heappush(processingServers,[time+task,serverWt,index])
                ans.append(index)
            else:
               pt,serverWeight,index = heapq.heappop(processingServers) 
               heapq.heappush(processingServers,[pt+task,serverWeight,index]) 
               ans.append(index)  

            time+=1

        return ans

            
            


            

        
