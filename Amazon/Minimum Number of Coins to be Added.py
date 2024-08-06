###https://www.youtube.com/watch?v=RAdaP-JcLA0

### so the intuition if n+1 coin is not present in the given Sumrange you can add that coin and increase the range to larger number.
### eg-  [1,2]-> has range till 3 if I add 4 my Sumrange goes to 7.

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:

        coins.sort()
        sumRange=0
        coin = 0
        coinsNeeded = 0

        while sumRange<target:

            if coin<len(coins) and coins[coin]<=sumRange + 1:
                sumRange+=coins[coin]
                coin+=1
            else:
                sumRange += (sumRange+1)
                coinsNeeded+=1

        return coinsNeeded
          
            










        
