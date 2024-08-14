class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:



        ### step1 find the closest number to the armor
        ### step2 get the sum of the remaining array

        damage.sort()

        idx = bisect.bisect_left(damage,armor)
        ### here the idx is the index equal to or jst less than armor
        if idx>=len(damage):
            idx = len(damage)-1
            
        sumRemaining = sum(damage[:idx])+sum(damage[idx+1:])
        
        remainDamage =  damage[idx]-armor  if damage[idx]-armor > 0 else 0

        sumRemaining+=remainDamage

        return sumRemaining+1
   



        


        
