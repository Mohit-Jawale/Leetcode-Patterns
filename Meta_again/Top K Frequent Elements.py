class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        position = defaultdict(list)
        for i in counter.keys():
            position[counter[i]].append(i)
        ans = []
        for i in reversed(range(pow(10,5))):
            if position[i]:
                for j in position[i]:
                    k-=1
                    ans.append(j)
                if k==0:
                    break
        return ans



        
