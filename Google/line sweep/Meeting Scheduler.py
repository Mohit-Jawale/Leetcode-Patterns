class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        

        line = Counter()
        meetings = slots1 + slots2
    

        for s,e in meetings:
            line[s]+=1
            line[e]-=1
        

        count = 0
        startPoint = None

        for key in sorted(line.keys()):
            
            count+=line[key]
     
            if count==2 and startPoint is None:
                startPoint=key
            
            if line[key]<0:### its a ending interval
                if startPoint is not None and (key-startPoint)>=duration:
                    return [startPoint,startPoint+duration]
                startPoint = None
           
        return []

            





        
   
        

