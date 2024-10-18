class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        
        #### if monsters[j] <= heroes[i].

        # h = [1,4,2]

        # m = [1,1,5,2,3]. -> [1,1,2,3,5]
        ### sort the coins with monsters - done
        ### binary serach to find the min - upper limit
        ## prefix sum of coins - done

        mon_coins = [(i,j) for i,j in list(zip(monsters,coins))]
        mon_coins.sort()

        prefixSum = [0]*len(mon_coins)
        prefixSum[0]=mon_coins[0][1]

        i = 1
        for mon,coin in mon_coins[1:]:

            prefixSum[i] =  prefixSum[i-1]+coin
            i+=1
        
        def binary_search(target,leftBais):

            left,right = 0,len(mon_coins)
            ans = 0
            while left<right:

                mid = left + (right-left)//2

                if mon_coins[mid][0] <= target:
                    left = mid+1
                else:
                    right = mid
                    
            return left
        
        results = []
    
        for hero in heroes:
            idx = binary_search(hero,False)

            if idx>0 and idx-1<len(prefixSum):
                results.append(prefixSum[idx-1])
            else:
                results.append(0)

        return results

                


