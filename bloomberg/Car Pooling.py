class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        


        rides = []

        for people,start,end in trips:
            rides.append((start,1,people))
            rides.append((end,-1,people))
        
        rides.sort(key = lambda x:(x[0],x[1]))

        total_people = 0

        for time,event_type,people in rides:

            if event_type == 1:
                total_people+=people
            else:
                total_people-=people
            
            if total_people>capacity:
                return False
        
        return True
            
                

