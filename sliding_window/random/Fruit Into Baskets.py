class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        ### this basket has two types of unique fruits
        basket = {}


        left,right = 0 ,0
        ans = 0

        while right<len(fruits):
            
            if not basket:
                basket[fruits[right]]=1
            elif len(basket)<=2 and fruits[right] in basket:
                basket[fruits[right]]+=1
            elif len(basket)<=2 and fruits[right] not in basket:
                basket[fruits[right]]=1

            while len(basket)>2:
                basket[fruits[left]]-=1
                if basket[fruits[left]]==0:
                    del basket[fruits[left]]
                left+=1    

            ans =  max(ans,right-left+1)
            right+=1

        return ans               
