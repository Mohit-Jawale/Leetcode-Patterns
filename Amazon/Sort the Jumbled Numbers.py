class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        ans = []
        for index,number in enumerate(nums):
            temp = ""
            for i in (str(number)):
                temp+=str(mapping[int(i)])

            ans.append((int(temp),index,number))
        
        ans.sort()

        ans = [k for i,j,k in ans]
        return ans
