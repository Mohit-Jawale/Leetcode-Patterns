class Solution:
    def reorganizeString(self, s: str) -> str:

        counter = Counter(s)
        maxHeap = [(-counter[i],i) for i in counter.keys()]
        heapq.heapify(maxHeap)
        ans = ""
        #### handle if there is only one char "a" or "aaaaaa" in both case ans will be different this is edge case
        if len(maxHeap)==1 and maxHeap[0][0]==1:
            return maxHeap[0][1]
        elif len(maxHeap)==1 and maxHeap[0][0]>1:
            return ans

        while len(maxHeap)>=2:

                count1,first = heapq.heappop(maxHeap)
                ans+=first
                count1+=1
                if maxHeap:
                    count2,second = heapq.heappop(maxHeap)
                    ans+=second
                    count2+=1
                    if count2!=0:
                        heapq.heappush(maxHeap,(count2,second))

                if count1!=0:
                    heapq.heappush(maxHeap,(count1,first))
                
        ### checking if heap has one character left and that char+ the answer is equal to the s then add it to the ans otherwise empty
        if maxHeap and len(maxHeap)+len(ans)!=len(s):
            return ""
        elif maxHeap and len(maxHeap)+len(ans)==len(s):
            return ans+maxHeap[0][1]
        else:
          #### This the perfect case where max heap is empty ans we have traverse through all char
            return ans
            

       
        

            

        
