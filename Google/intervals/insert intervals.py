class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:


        counter = Counter()
        intervals+=[newInterval]


        for s,e in intervals:
            counter[s]+=1
            counter[e]-=1
        

        merge_intervals = []
        count = 0
        new_interval = None


        for key in sorted(counter.keys()):

            if count==0:
                new_interval = key

            count+=counter[key]

            if count==0 and new_interval is not None:
                merge_intervals.append([new_interval,key])
                new_interval = None
          

        return merge_intervals




        

        




        
