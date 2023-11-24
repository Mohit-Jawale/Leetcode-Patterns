### This problem is complex to code as it has lots of thinngs gng on. Solution is easy

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for index,task in enumerate(tasks):
            task.append(index)
        tasks.sort()
        minHeap, res= [],[]
        i,time= 0,tasks[0][0]

        while minHeap or i<len(tasks):
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(minHeap,(tasks[i][1],tasks[i][2]))
                i+=1

            if not minHeap:
                time = tasks[i][0]
            else:
                pt,index = heapq.heappop(minHeap)
                time+=pt
                res.append(index)    


        return res
