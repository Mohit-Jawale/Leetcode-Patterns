#### Remember here the problem is using memory to reduce time the trick of using array to count and keep it sorted is good.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        most_frequent = [[] for i in range(len(nums)+1)]
    
        counter = {}
        for n in nums:
            counter[n]= 1+counter.get(n,0)

        for key, value in counter.items():
            most_frequent[value].append(key)

        count = 0
        ans = []
        for i in range(len(most_frequent)-1,0,-1):
    
            if most_frequent[i]:
               for n in most_frequent[i]:
                   ans.append(n)
                   count+=1
                   if count == k:
                        break
               
            if count==k:
                break   

        return ans        

            
