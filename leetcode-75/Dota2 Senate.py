class Solution:
    def predictPartyVictory(self, senate: str) -> str:


        dQueue = deque([])
        rQueue = deque([])

        n = len(senate)

        for i in range(n):
            if senate[i]=="R":
                rQueue.append(i)
            elif senate[i]=="D":
                dQueue.append(i)

        while dQueue and rQueue:
            
            r_turn = rQueue.popleft()
            d_turn = dQueue.popleft()
            
            if r_turn<d_turn:
                rQueue.append(r_turn+n)
            else:
                dQueue.append(d_turn+n)
             
    

        if rQueue:
            return "Radiant"
        else:
            return "Dire"






 

       





        
