class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        k_frequent = [[] for i in range(len(nums)+1)]

        counter = {}
        for i in nums:
            counter[i]= 1+counter.get(i,0)

        for key,value in counter.items():
            k_frequent[value].append(key)   

        ans = []        
        for i in range(len(k_frequent)-1,0,-1):
            if k_frequent[i]:
                for n in  k_frequent[i]:
                    ans.append(n)
            if len(ans)==k:
                break
        return ans        
